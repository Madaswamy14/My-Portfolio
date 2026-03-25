import argparse
import concurrent.futures
import os
import re
import sys
from collections import Counter
from itertools import groupby
from pathlib import Path
from urllib.parse import unquote, urlparse

DOC_EXTENSIONS = {'.md', '.mdx'}
IGNORED_DIRS = {'node_modules', '.git', 'build', 'dist', '__pycache__'}
LINK_PATTERN = re.compile(r'(!?)\[[^\]]*?\]\(\s*([^)]+?)\s*\)')
HEADING_PATTERN = re.compile(r'^\s{0,3}(#{1,6})\s+(.*?)\s*$')
CUSTOM_ID_PATTERN = re.compile(r'\s*\{#([A-Za-z0-9_-]+)\}\s*$')
TITLE_SUFFIX_PATTERN = re.compile(r'\s+(?:"[^"]*"|\'[^\']*\')\s*$')


def get_markdown_files(scan_path):
    """Yield markdown files from a directory or a single markdown file path."""
    path = Path(scan_path)

    if path.is_file():
        if path.suffix.lower() in DOC_EXTENSIONS:
            yield path.resolve()
        return

    for root, dirs, files in os.walk(path):
        dirs[:] = [directory for directory in dirs if directory not in IGNORED_DIRS]
        for file_name in files:
            file_path = Path(root) / file_name
            if file_path.suffix.lower() in DOC_EXTENSIONS:
                yield file_path.resolve()


def normalize_target(raw_target):
    """Remove markdown title suffixes and angle-bracket wrappers."""
    target = raw_target.strip()
    target = TITLE_SUFFIX_PATTERN.sub('', target)
    if target.startswith('<') and target.endswith('>'):
        target = target[1:-1].strip()
    return target


def slugify_heading(text):
    """Create a simple markdown-compatible anchor slug from a heading."""
    text = CUSTOM_ID_PATTERN.sub('', text)
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    text = text.strip().lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')


def extract_heading_anchor(heading_text):
    """Return a custom heading id when present, otherwise derive a slug."""
    custom_id = CUSTOM_ID_PATTERN.search(heading_text)
    if custom_id:
        return custom_id.group(1).lower()
    return slugify_heading(heading_text)


def build_heading_index(markdown_files):
    """Map markdown file paths to the heading anchors they expose."""
    heading_index = {}

    for file_path in markdown_files:
        anchors = set()
        try:
            lines = file_path.read_text(encoding='utf-8').splitlines()
        except OSError:
            heading_index[file_path] = anchors
            continue

        for line in lines:
            match = HEADING_PATTERN.match(line)
            if not match:
                continue
            anchor = extract_heading_anchor(match.group(2))
            if anchor:
                anchors.add(anchor)

        heading_index[file_path.resolve()] = anchors

    return heading_index


def candidate_target_paths(base_path):
    """Return likely filesystem targets for a local markdown reference."""
    resolved_base = base_path.resolve(strict=False)
    candidates = [resolved_base]

    if resolved_base.suffix == '':
        candidates.extend(
            [
                resolved_base.with_suffix('.md'),
                resolved_base.with_suffix('.mdx'),
                resolved_base / 'index.md',
                resolved_base / 'index.mdx',
                resolved_base / 'README.md',
                resolved_base / 'README.mdx',
            ]
        )
    elif resolved_base.suffix.lower() == '.html':
        stem_path = resolved_base.with_suffix('')
        candidates.extend(
            [
                stem_path.with_suffix('.md'),
                stem_path.with_suffix('.mdx'),
                stem_path / 'index.md',
                stem_path / 'index.mdx',
            ]
        )

    unique_candidates = []
    seen = set()
    for candidate in candidates:
        key = str(candidate)
        if key not in seen:
            seen.add(key)
            unique_candidates.append(candidate)

    return unique_candidates


def resolve_local_target(file_path, link_target, root_dir):
    """Resolve a local markdown reference to a real file when possible."""
    path_part = unquote(link_target.split('#', 1)[0].split('?', 1)[0])
    if not path_part:
        return file_path.resolve()

    if path_part.startswith('/'):
        base_path = root_dir / path_part.lstrip('/')
    else:
        base_path = file_path.parent / path_part

    for candidate in candidate_target_paths(base_path):
        if candidate.exists():
            return candidate.resolve()

    return None


def validate_anchor(target_file, anchor_name, heading_index):
    """Validate a heading anchor on a markdown file target."""
    normalized_anchor = unquote(anchor_name).strip().lower()
    if not normalized_anchor:
        return True, 'OK'

    if target_file.suffix.lower() not in DOC_EXTENSIONS:
        return False, f'Anchor not supported for non-markdown target: #{normalized_anchor}'

    available_anchors = heading_index.get(target_file.resolve(), set())
    if normalized_anchor in available_anchors:
        return True, 'OK'

    return False, f'Anchor not found: #{normalized_anchor}'


def validate_local_target(file_path, link_target, root_dir, heading_index, is_image=False):
    """Validate local links, images, and markdown heading references."""
    path_part, _, anchor_name = link_target.partition('#')
    target_file = resolve_local_target(file_path, link_target, root_dir)

    if target_file is None:
        issue_type = 'missing image' if is_image else 'broken link'
        clean_target = unquote(path_part.split('?', 1)[0]) or link_target
        return False, issue_type, f'File not found: {clean_target}'

    if anchor_name:
        is_valid, message = validate_anchor(target_file, anchor_name, heading_index)
        if not is_valid:
            return False, 'invalid reference', message

    return True, 'OK', 'OK'


def check_remote_link(url, timeout=5):
    """Check whether a remote URL responds successfully."""
    try:
        import requests
    except ImportError as exc:
        raise RuntimeError(
            "Remote link checking requires the 'requests' module. "
            "Install it via 'pip install requests' or rerun with --skip-remote."
        ) from exc

    headers = {'User-Agent': 'DocumentationQualityAutomationTool/1.0'}

    try:
        response = requests.head(url, timeout=timeout, headers=headers, allow_redirects=True)
        if response.status_code in {403, 405}:
            response = requests.get(url, timeout=timeout, headers=headers, stream=True)

        if 200 <= response.status_code < 400:
            return url, True, f'Status {response.status_code}'

        return url, False, f'Status {response.status_code}'
    except requests.RequestException as exc:
        return url, False, f'Connection error: {exc.__class__.__name__}'


def scan_file(file_path, root_dir, heading_index):
    """Scan a markdown file and return local issues plus remote targets."""
    issues = []
    remote_urls = []

    try:
        lines = file_path.read_text(encoding='utf-8').splitlines()
    except OSError as exc:
        issues.append(
            {
                'file': file_path,
                'line': 0,
                'target': str(file_path),
                'type': 'file error',
                'error': str(exc),
            }
        )
        return issues, remote_urls

    for line_number, line in enumerate(lines, start=1):
        for image_prefix, raw_target in LINK_PATTERN.findall(line):
            target = normalize_target(raw_target)
            is_image = bool(image_prefix)

            if not target or target.startswith(('mailto:', 'tel:', 'javascript:', '{{')):
                continue

            if urlparse(target).scheme in {'http', 'https'}:
                remote_urls.append(
                    {
                        'file': file_path,
                        'line': line_number,
                        'target': target,
                        'type': 'missing image' if is_image else 'broken link',
                    }
                )
                continue

            is_valid, issue_type, message = validate_local_target(
                file_path=file_path,
                link_target=target,
                root_dir=root_dir,
                heading_index=heading_index,
                is_image=is_image,
            )
            if not is_valid:
                issues.append(
                    {
                        'file': file_path,
                        'line': line_number,
                        'target': target,
                        'type': issue_type,
                        'error': message,
                    }
                )

    return issues, remote_urls


def scan_docs(scan_path, check_remote=True, concurrency=10, timeout=5):
    """Scan documentation and return issues plus a lightweight summary."""
    input_path = Path(scan_path)
    root_dir = input_path if input_path.is_dir() else input_path.parent
    markdown_files = list(get_markdown_files(input_path))
    heading_index = build_heading_index(markdown_files)

    issues = []
    remote_targets = []
    for file_path in markdown_files:
        file_issues, file_remote_targets = scan_file(file_path, root_dir, heading_index)
        issues.extend(file_issues)
        remote_targets.extend(file_remote_targets)

    unique_remote_targets = sorted({item['target'] for item in remote_targets})
    remote_results = {}
    if check_remote and unique_remote_targets:
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            future_map = {
                executor.submit(check_remote_link, target, timeout): target
                for target in unique_remote_targets
            }
            for future in concurrent.futures.as_completed(future_map):
                target, is_valid, message = future.result()
                remote_results[target] = (is_valid, message)

    for remote_target in remote_targets:
        if remote_target['target'] not in remote_results:
            continue
        is_valid, message = remote_results[remote_target['target']]
        if not is_valid:
            issues.append(
                {
                    'file': remote_target['file'],
                    'line': remote_target['line'],
                    'target': remote_target['target'],
                    'type': remote_target['type'],
                    'error': message,
                }
            )

    summary = {
        'files_scanned': len(markdown_files),
        'remote_links_found': len(remote_targets),
        'unique_remote_links_checked': len(unique_remote_targets) if check_remote else 0,
        'issues_found': len(issues),
        'issue_breakdown': Counter(issue['type'] for issue in issues),
    }
    return issues, summary


def print_report(issues, summary, check_remote):
    """Print a human-friendly CLI report."""
    print(f"[INFO] Files scanned: {summary['files_scanned']}")
    print(f"[INFO] Remote links found: {summary['remote_links_found']}")
    if check_remote:
        print(f"[INFO] Unique remote links checked: {summary['unique_remote_links_checked']}")
    else:
        print('[INFO] Remote link checks skipped (--skip-remote)')

    print("\n" + "=" * 56)
    if not issues:
        print('[OK] No broken links, missing images, or invalid references found!')
        return

    print(f"[ERROR] Found {len(issues)} documentation issues\n")
    for issue_type, count in sorted(summary['issue_breakdown'].items()):
        print(f"- {issue_type}: {count}")
    print('')

    issues.sort(key=lambda issue: (str(issue['file']), issue['line'], issue['target']))
    for file_path, grouped_issues in groupby(issues, key=lambda issue: issue['file']):
        print(f"[FILE] {file_path}")
        for issue in grouped_issues:
            print(
                f"   Line {issue['line']}: [{issue['type']}] "
                f"{issue['target']} -> {issue['error']}"
            )
        print('')


def main():
    parser = argparse.ArgumentParser(description='Documentation Quality Automation Tool')
    parser.add_argument('path', help='Path to a documentation folder or markdown file to scan')
    parser.add_argument('--concurrency', type=int, default=10, help='Max concurrent remote requests')
    parser.add_argument('--timeout', type=int, default=5, help='Remote link timeout in seconds')
    parser.add_argument('--skip-remote', action='store_true', help='Skip checking external http/https links')
    args = parser.parse_args()

    scan_target = Path(args.path)
    if not scan_target.exists():
        print(f'Error: Path not found: {scan_target}')
        sys.exit(1)

    print(f'[INFO] Scanning documentation in: {scan_target}')
    try:
        issues, summary = scan_docs(
            scan_path=scan_target,
            check_remote=not args.skip_remote,
            concurrency=args.concurrency,
            timeout=args.timeout,
        )
    except RuntimeError as exc:
        print(f'Error: {exc}')
        sys.exit(1)

    print_report(issues, summary, check_remote=not args.skip_remote)
    sys.exit(1 if issues else 0)


if __name__ == '__main__':
    main()