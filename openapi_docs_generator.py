import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HTTP_METHODS = {'get', 'post', 'put', 'delete', 'patch', 'options', 'head'}


def load_yaml_module():
    """Import PyYAML only when a YAML spec is actually parsed."""
    try:
        import yaml
    except ImportError as exc:
        raise RuntimeError(
            "YAML input requires the 'pyyaml' module. "
            "Install it with 'pip install pyyaml' or use a JSON spec."
        ) from exc
    return yaml


def load_spec(file_path):
    """Load an OpenAPI or Swagger spec from JSON or YAML."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f'Spec file not found: {file_path}')

    if path.suffix.lower() in {'.yaml', '.yml'}:
        yaml = load_yaml_module()
        spec = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    elif path.suffix.lower() == '.json':
        spec = json.loads(path.read_text(encoding='utf-8'))
    else:
        raise ValueError('Unsupported file format. Please use .json, .yaml, or .yml.')

    if not isinstance(spec, dict):
        raise ValueError('OpenAPI spec must deserialize into an object at the document root.')

    return spec


def slugify(value):
    """Turn free-form text into a filesystem-safe slug."""
    text = re.sub(r'[^a-zA-Z0-9]+', '-', str(value).strip().lower())
    return text.strip('-') or 'item'


def compact_text(value):
    """Collapse whitespace for cleaner markdown output."""
    return re.sub(r'\s+', ' ', str(value or '')).strip()


def quote_frontmatter(value):
    """Write YAML-safe strings using JSON-style quoting."""
    return json.dumps(str(value))


def escape_table_cell(value):
    """Avoid broken markdown tables when values contain pipes or newlines."""
    text = compact_text(value)
    return text.replace('|', '\\|') if text else '—'


def resolve_json_pointer(document, ref):
    """Resolve a local JSON pointer such as #/components/schemas/User."""
    if not ref.startswith('#/'):
        return None

    current = document
    for token in ref[2:].split('/'):
        key = token.replace('~1', '/').replace('~0', '~')
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def resolve_reference(spec, value, seen=None):
    """Resolve local $ref pointers while preserving sibling overrides."""
    if not isinstance(value, dict) or '$ref' not in value:
        return value

    ref = value['$ref']
    if seen is None:
        seen = set()
    if ref in seen:
        return {key: item for key, item in value.items() if key != '$ref'}

    resolved = resolve_json_pointer(spec, ref)
    if not isinstance(resolved, dict):
        return {key: item for key, item in value.items() if key != '$ref'}

    merged = dict(resolved)
    merged.update({key: item for key, item in value.items() if key != '$ref'})
    return resolve_reference(spec, merged, seen | {ref})


def schema_type(schema, spec):
    """Create a concise human-readable schema summary."""
    schema = resolve_reference(spec, schema)
    if not isinstance(schema, dict) or not schema:
        return 'object'

    for composite_key, joiner in (('oneOf', ' | '), ('anyOf', ' | '), ('allOf', ' + ')):
        if composite_key in schema and schema[composite_key]:
            return joiner.join(schema_type(item, spec) for item in schema[composite_key])

    if schema.get('enum'):
        preview = ', '.join(str(item) for item in schema['enum'][:4])
        suffix = '…' if len(schema['enum']) > 4 else ''
        return f'enum ({preview}{suffix})'

    schema_name = schema.get('type')
    if not schema_name and 'properties' in schema:
        schema_name = 'object'

    if schema_name == 'array':
        return f"array<{schema_type(schema.get('items', {}), spec)}>"

    if schema_name == 'object' and schema.get('title'):
        return schema['title']

    if schema_name and schema.get('format'):
        return f"{schema_name} ({schema['format']})"

    return schema_name or 'object'


def example_from_schema(schema, spec, depth=0):
    """Generate a lightweight example payload from a schema."""
    if depth > 2:
        return 'value'

    schema = resolve_reference(spec, schema)
    if not isinstance(schema, dict) or not schema:
        return 'value'

    if 'example' in schema:
        return schema['example']
    if 'default' in schema:
        return schema['default']
    if schema.get('enum'):
        return schema['enum'][0]

    for composite_key in ('oneOf', 'anyOf', 'allOf'):
        if schema.get(composite_key):
            return example_from_schema(schema[composite_key][0], spec, depth + 1)

    schema_name = schema.get('type')
    if not schema_name and 'properties' in schema:
        schema_name = 'object'

    if schema_name == 'object':
        example = {}
        for index, (name, property_schema) in enumerate(schema.get('properties', {}).items()):
            if index >= 4:
                break
            example[name] = example_from_schema(property_schema, spec, depth + 1)
        return example or {'key': 'value'}

    if schema_name == 'array':
        return [example_from_schema(schema.get('items', {}), spec, depth + 1)]
    if schema_name == 'integer':
        return 42
    if schema_name == 'number':
        return 9.99
    if schema_name == 'boolean':
        return True

    return 'string'


def generate_markdown_table(headers, rows):
    """Render a markdown table from headers and row values."""
    if not rows:
        return '_No details provided._'

    header_row = '| ' + ' | '.join(headers) + ' |'
    separator_row = '| ' + ' | '.join(['---'] * len(headers)) + ' |'
    body_rows = []
    for row in rows:
        body_rows.append('| ' + ' | '.join(escape_table_cell(cell) for cell in row) + ' |')
    return '\n'.join([header_row, separator_row, *body_rows])


def merge_parameters(path_item, operation, spec):
    """Combine path-level and operation-level parameters with deduplication."""
    merged = []
    seen = set()

    for raw_parameter in path_item.get('parameters', []) + operation.get('parameters', []):
        parameter = resolve_reference(spec, raw_parameter)
        if not isinstance(parameter, dict):
            continue

        key = (parameter.get('name', ''), parameter.get('in', ''))
        if key in seen:
            continue
        seen.add(key)
        merged.append(parameter)

    return merged


def build_parameter_rows(parameters, spec):
    """Build table rows for path/query/header/cookie parameters."""
    rows = []
    visible_parameters = []

    for parameter in parameters:
        location = parameter.get('in', '')
        if location in {'body', 'formData'}:
            continue

        visible_parameters.append(parameter)
        rows.append(
            [
                f"`{parameter.get('name', '')}`",
                location or '—',
                'Yes' if parameter.get('required', False) else 'No',
                schema_type(parameter.get('schema', {}), spec),
                compact_text(parameter.get('description')) or '—',
            ]
        )

    return visible_parameters, rows


def first_example_value(examples, spec):
    """Extract the first example payload from an OpenAPI examples map."""
    if not isinstance(examples, dict) or not examples:
        return None

    first_key = next(iter(examples))
    example = resolve_reference(spec, examples[first_key])
    if isinstance(example, dict) and 'value' in example:
        return example['value']
    return None


def build_request_body_rows(spec, operation, parameters):
    """Build request-body documentation for OpenAPI 3 and Swagger 2."""
    rows = []
    examples = []

    request_body = resolve_reference(spec, operation.get('requestBody', {}))
    if isinstance(request_body, dict) and request_body:
        description = compact_text(request_body.get('description')) or '—'
        required = 'Yes' if request_body.get('required', False) else 'No'

        for media_type, raw_media in request_body.get('content', {}).items():
            media = resolve_reference(spec, raw_media)
            schema = media.get('schema', {})
            rows.append([f"`{media_type}`", schema_type(schema, spec), required, description])

            example = media.get('example')
            if example is None:
                example = first_example_value(media.get('examples'), spec)
            if example is None:
                example = example_from_schema(schema, spec)
            examples.append((media_type, example))

        return rows, examples

    body_parameters = [parameter for parameter in parameters if parameter.get('in') in {'body', 'formData'}]
    if not body_parameters:
        return rows, examples

    consumes = operation.get('consumes') or spec.get('consumes') or ['application/json']
    body_parameter = next((param for param in body_parameters if param.get('in') == 'body'), None)
    form_parameters = [param for param in body_parameters if param.get('in') == 'formData']

    if body_parameter:
        schema = body_parameter.get('schema', {})
        description = compact_text(body_parameter.get('description')) or '—'
        required = 'Yes' if body_parameter.get('required', False) else 'No'
        for media_type in consumes:
            rows.append([f"`{media_type}`", schema_type(schema, spec), required, description])
            examples.append((media_type, example_from_schema(schema, spec)))
        return rows, examples

    form_example = {}
    for parameter in form_parameters:
        form_example[parameter.get('name', 'field')] = example_from_schema(parameter.get('schema', {}), spec)

    required = 'Yes' if any(param.get('required', False) for param in form_parameters) else 'No'
    description = 'Form fields generated from Swagger formData parameters.'
    for media_type in consumes:
        rows.append([f"`{media_type}`", 'form fields', required, description])
        examples.append((media_type, form_example or {'field': 'value'}))

    return rows, examples


def build_response_rows(spec, operation):
    """Build response rows with response schema summaries."""
    rows = []

    for status_code, raw_response in (operation.get('responses') or {}).items():
        response = resolve_reference(spec, raw_response)
        description = compact_text(response.get('description')) or '—'

        schema_summary = '—'
        if 'content' in response:
            schema_parts = []
            for media_type, raw_media in response.get('content', {}).items():
                media = resolve_reference(spec, raw_media)
                schema_parts.append(f"{media_type}: {schema_type(media.get('schema', {}), spec)}")
            schema_summary = '; '.join(schema_parts) if schema_parts else '—'
        elif 'schema' in response:
            schema_summary = schema_type(response.get('schema', {}), spec)

        rows.append([f"`{status_code}`", description, schema_summary])

    return rows


def build_security_rows(spec, operation):
    """Build human-readable authentication guidance and curl headers."""
    requirements = operation.get('security', spec.get('security'))
    if requirements == [] or not requirements:
        return [['Public', 'No authentication required.']], []

    security_schemes = spec.get('components', {}).get('securitySchemes', {})
    if not security_schemes:
        security_schemes = spec.get('securityDefinitions', {})

    rows = []
    curl_headers = []
    seen_rows = set()
    seen_headers = set()

    for requirement in requirements:
        if not requirement:
            entry = ('Public', 'No authentication required.')
            if entry not in seen_rows:
                seen_rows.add(entry)
                rows.append(list(entry))
            continue

        for scheme_name, scopes in requirement.items():
            scheme = resolve_reference(spec, security_schemes.get(scheme_name, {}))
            scheme_type_name = scheme.get('type', 'security')
            description = compact_text(scheme.get('description'))

            if scheme_type_name == 'http':
                http_scheme = scheme.get('scheme', 'http').lower()
                if http_scheme == 'bearer':
                    description = description or 'Bearer token in `Authorization` header.'
                    seen_headers.add(('Authorization', 'Bearer <token>'))
                elif http_scheme == 'basic':
                    description = description or 'HTTP Basic authentication.'
                else:
                    description = description or f'HTTP {http_scheme} authentication.'
            elif scheme_type_name == 'apiKey':
                key_name = scheme.get('name', scheme_name)
                location = scheme.get('in', 'header')
                description = description or f'API key in `{location}` parameter `{key_name}`.'
                if location == 'header':
                    seen_headers.add((key_name, '<api-key>'))
            elif scheme_type_name == 'oauth2':
                description = description or 'OAuth 2.0 access token.'
                if scopes:
                    description = f"{description} Scopes: {', '.join(scopes)}."
                seen_headers.add(('Authorization', 'Bearer <token>'))
            else:
                description = description or scheme_type_name

            row = (f"`{scheme_name}`", description)
            if row not in seen_rows:
                seen_rows.add(row)
                rows.append(list(row))

    curl_headers.extend(sorted(seen_headers))
    return rows or [['Public', 'No authentication required.']], curl_headers


def build_base_url(spec, override=None):
    """Choose a base URL from an override or the spec metadata."""
    if override:
        return override.rstrip('/')

    servers = spec.get('servers') or []
    if servers and isinstance(servers[0], dict) and servers[0].get('url'):
        return str(servers[0]['url']).rstrip('/')

    host = spec.get('host')
    if host:
        scheme = (spec.get('schemes') or ['https'])[0]
        base_path = str(spec.get('basePath', '')).rstrip('/')
        return f'{scheme}://{host}{base_path}'

    return 'https://api.example.com'


def build_curl_example(method, path, parameters, request_body_examples, curl_headers, base_url):
    """Create a small example request block for developer docs."""
    url = f"{base_url.rstrip('/')}{path}"

    query_parameters = []
    header_parameters = []
    for parameter in parameters:
        location = parameter.get('in')
        name = parameter.get('name', 'value')
        placeholder = f'<{name}>'

        if location == 'query':
            if parameter.get('required', False) or len(query_parameters) < 2:
                query_parameters.append(f'{name}={placeholder}')
        elif location == 'header' and parameter.get('required', False):
            header_parameters.append((name, placeholder))

    if query_parameters:
        separator = '&' if '?' in url else '?'
        url = f"{url}{separator}{'&'.join(query_parameters)}"

    headers = [('Accept', 'application/json'), *curl_headers, *header_parameters]
    body_text = None
    if request_body_examples:
        media_type, example = request_body_examples[0]
        headers.append(('Content-Type', media_type))
        if media_type.endswith('json'):
            body_text = json.dumps(example, indent=2)
        else:
            body_text = str(example)

    arguments = [f'--request {method.upper()}', f'--url "{url}"']
    arguments.extend(f'--header "{name}: {value}"' for name, value in headers)
    if body_text is not None:
        arguments.append(f"--data '{body_text}'")

    lines = ['```bash']
    for index, argument in enumerate(arguments):
        prefix = 'curl ' if index == 0 else '  '
        suffix = ' ' + '\\' if index < len(arguments) - 1 else ''
        lines.append(f'{prefix}{argument}{suffix}')
    lines.append('```')
    return '\n'.join(lines)


def operation_title(method, path, operation):
    """Pick a page title with a sensible fallback."""
    return operation.get('summary') or operation.get('operationId') or f'{method.upper()} {path}'


def description_text(operation):
    """Pick a primary description for the endpoint."""
    return compact_text(operation.get('description') or operation.get('summary') or 'No description provided.')


def ensure_unique_path(candidate_path, used_paths):
    """Avoid collisions when multiple operations map to the same file slug."""
    unique_path = candidate_path
    counter = 2

    while unique_path.as_posix() in used_paths:
        unique_path = candidate_path.with_name(f'{candidate_path.stem}-{counter}{candidate_path.suffix}')
        counter += 1

    used_paths.add(unique_path.as_posix())
    return unique_path


def generate_doc_page(path, method, path_item, operation, spec, output_dir, base_url, used_paths):
    """Generate a single endpoint page and return its metadata."""
    title = operation_title(method, path, operation)
    description = description_text(operation)
    tag_name = (operation.get('tags') or ['General'])[0]
    tag_slug = slugify(tag_name)
    operation_slug = slugify(operation.get('operationId') or f'{method}-{path}')

    relative_path = ensure_unique_path(Path(tag_slug) / f'{operation_slug}.md', used_paths)
    output_path = output_dir / relative_path
    output_path.parent.mkdir(parents=True, exist_ok=True)

    parameters = merge_parameters(path_item, operation, spec)
    visible_parameters, parameter_rows = build_parameter_rows(parameters, spec)
    request_body_rows, request_body_examples = build_request_body_rows(spec, operation, parameters)
    response_rows = build_response_rows(spec, operation)
    security_rows, curl_headers = build_security_rows(spec, operation)
    curl_example = build_curl_example(method, path, visible_parameters, request_body_examples, curl_headers, base_url)

    frontmatter_description = description if len(description) <= 140 else f'{description[:137]}...'
    page_lines = [
        '---',
        f'title: {quote_frontmatter(title)}',
        f'description: {quote_frontmatter(frontmatter_description)}',
        f'slug: {quote_frontmatter("/generated-api/" + tag_slug + "/" + operation_slug)}',
        '---',
        '',
        f'# {title}',
        '',
        description,
        '',
        f'**Endpoint:** `{method.upper()} {path}`',
        '',
        f'**Operation ID:** `{operation.get("operationId", operation_slug)}`',
        '',
        f'**Tag:** {tag_name}',
        '',
        '## Authentication',
        '',
        generate_markdown_table(['Scheme', 'Details'], security_rows),
        '',
        '## Parameters',
        '',
        generate_markdown_table(['Name', 'In', 'Required', 'Type', 'Description'], parameter_rows)
        if parameter_rows
        else '_No path, query, header, or cookie parameters._',
        '',
        '## Request body',
        '',
        generate_markdown_table(['Content type', 'Schema', 'Required', 'Description'], request_body_rows)
        if request_body_rows
        else '_No request body._',
        '',
    ]

    if request_body_examples:
        example_media_type, example_payload = request_body_examples[0]
        page_lines.extend(
            [
                '### Example payload',
                '',
                f'`{example_media_type}`',
                '',
                '```json',
                json.dumps(example_payload, indent=2),
                '```',
                '',
            ]
        )

    page_lines.extend(
        [
            '## Responses',
            '',
            generate_markdown_table(['Status', 'Description', 'Schema'], response_rows)
            if response_rows
            else '_No response details provided._',
            '',
            '## Example request',
            '',
            curl_example,
            '',
        ]
    )

    output_path.write_text('\n'.join(page_lines), encoding='utf-8')
    return {
        'title': title,
        'method': method.upper(),
        'path': path,
        'tag': tag_name,
        'relative_path': relative_path,
    }


def write_overview_page(spec, output_dir, operations, overview_name, base_url):
    """Write a generated overview page that links to all endpoint docs."""
    info = spec.get('info', {})
    title = compact_text(info.get('title')) or 'Generated API Reference'
    version = compact_text(info.get('version')) or 'Unspecified'
    description = compact_text(info.get('description')) or 'Developer documentation generated from an OpenAPI or Swagger specification.'

    grouped_operations = defaultdict(list)
    for operation in operations:
        grouped_operations[operation['tag']].append(operation)

    overview_lines = [
        '---',
        f'title: {quote_frontmatter(title + " API Reference")}',
        f'description: {quote_frontmatter(description[:140])}',
        f'slug: {quote_frontmatter("/generated-api")}',
        '---',
        '',
        f'# {title} API Reference',
        '',
        description,
        '',
        f'**Version:** `{version}`',
        '',
        f'**Base URL:** `{base_url}`',
        '',
        f'**Generated endpoints:** `{len(operations)}`',
        '',
        '## Endpoints by tag',
        '',
    ]

    for tag in sorted(grouped_operations):
        rows = []
        for operation in sorted(grouped_operations[tag], key=lambda item: (item['path'], item['method'])):
            relative_link = f'./{operation["relative_path"].as_posix()}'
            rows.append(
                [
                    f"`{operation['method']}`",
                    f"`{operation['path']}`",
                    operation['title'],
                    f"[Open doc]({relative_link})",
                ]
            )

        overview_lines.extend(
            [
                f'### {tag}',
                '',
                generate_markdown_table(['Method', 'Path', 'Summary', 'Documentation'], rows),
                '',
            ]
        )

    overview_path = output_dir / overview_name
    overview_path.write_text('\n'.join(overview_lines), encoding='utf-8')
    return overview_path


def generate_docs(spec, output_dir, base_url=None, overview_name='overview.md'):
    """Generate endpoint pages plus an overview page from an OpenAPI spec."""
    if not isinstance(spec, dict):
        raise ValueError('OpenAPI spec must be a dictionary-like object.')

    paths = spec.get('paths')
    if not isinstance(paths, dict) or not paths:
        raise ValueError('OpenAPI spec does not define any paths to document.')

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    effective_base_url = build_base_url(spec, override=base_url)

    operations = []
    used_paths = set()
    for path, path_item in paths.items():
        if not isinstance(path_item, dict):
            continue

        for method, operation in path_item.items():
            if method.lower() not in HTTP_METHODS or not isinstance(operation, dict):
                continue

            metadata = generate_doc_page(
                path=path,
                method=method,
                path_item=path_item,
                operation=operation,
                spec=spec,
                output_dir=output_path,
                base_url=effective_base_url,
                used_paths=used_paths,
            )
            operations.append(metadata)

    if not operations:
        raise ValueError('No HTTP operations were found in the supplied spec.')

    overview_path = write_overview_page(
        spec=spec,
        output_dir=output_path,
        operations=operations,
        overview_name=overview_name,
        base_url=effective_base_url,
    )

    return {
        'count': len(operations),
        'generated_files': [metadata['relative_path'] for metadata in operations],
        'overview_file': overview_path.relative_to(output_path),
        'base_url': effective_base_url,
    }


def main():
    parser = argparse.ArgumentParser(description='OpenAPI -> Developer Docs Generator')
    parser.add_argument('spec', help='Path to the OpenAPI/Swagger file (.json, .yaml, .yml)')
    parser.add_argument('-o', '--output', default='docs/generated-api', help='Directory for generated markdown docs')
    parser.add_argument('--base-url', help='Override the base URL used in generated example requests')
    parser.add_argument('--overview-name', default='overview.md', help='Filename for the generated overview page')
    args = parser.parse_args()

    print(f'[INFO] Reading OpenAPI spec: {args.spec}')
    try:
        spec = load_spec(args.spec)
        result = generate_docs(
            spec=spec,
            output_dir=args.output,
            base_url=args.base_url,
            overview_name=args.overview_name,
        )
    except Exception as exc:
        print(f'[ERROR] {exc}')
        sys.exit(1)

    output_dir = Path(args.output)
    print(f'[INFO] Generated {result["count"]} endpoint page(s) in: {output_dir.resolve()}')
    print(f'[INFO] Overview: {result["overview_file"].as_posix()}')
    for relative_path in result['generated_files']:
        print(f'   + {relative_path.as_posix()}')

    print('\n[OK] OpenAPI developer documentation generation complete.')


if __name__ == '__main__':
    main()