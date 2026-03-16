import json
import tempfile
import unittest
from pathlib import Path

from openapi_docs_generator import generate_docs, load_spec


class OpenApiDocsGeneratorTests(unittest.TestCase):
    def write_json(self, root_dir, relative_path, content):
        target_path = Path(root_dir) / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(json.dumps(content, indent=2), encoding='utf-8')
        return target_path

    def test_load_spec_from_json_file(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            spec_path = self.write_json(temp_dir, 'spec.json', {'openapi': '3.0.0', 'paths': {}})

            spec = load_spec(spec_path)

            self.assertEqual('3.0.0', spec['openapi'])

    def test_generate_docs_creates_overview_and_endpoint_pages(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            spec = {
                'openapi': '3.0.0',
                'info': {
                    'title': 'Payments API',
                    'version': '2026-03-13',
                    'description': 'API for payment operations.',
                },
                'servers': [{'url': 'https://api.example.com'}],
                'components': {
                    'securitySchemes': {
                        'BearerAuth': {'type': 'http', 'scheme': 'bearer'}
                    },
                    'schemas': {
                        'ChargeRequest': {
                            'type': 'object',
                            'properties': {
                                'amount': {'type': 'integer', 'example': 5000},
                                'currency': {'type': 'string', 'example': 'USD'},
                            },
                        },
                        'ChargeResponse': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string', 'example': 'ch_123'},
                                'status': {'type': 'string', 'example': 'succeeded'},
                            },
                        },
                    },
                },
                'paths': {
                    '/charges': {
                        'post': {
                            'tags': ['Payments'],
                            'summary': 'Create charge',
                            'description': 'Create a payment charge for an order.',
                            'operationId': 'createCharge',
                            'security': [{'BearerAuth': []}],
                            'parameters': [
                                {
                                    'name': 'expand',
                                    'in': 'query',
                                    'required': False,
                                    'schema': {'type': 'string'},
                                    'description': 'Expand related resources.',
                                }
                            ],
                            'requestBody': {
                                'required': True,
                                'content': {
                                    'application/json': {
                                        'schema': {'$ref': '#/components/schemas/ChargeRequest'}
                                    }
                                },
                            },
                            'responses': {
                                '201': {
                                    'description': 'Charge created.',
                                    'content': {
                                        'application/json': {
                                            'schema': {'$ref': '#/components/schemas/ChargeResponse'}
                                        }
                                    },
                                }
                            },
                        }
                    }
                },
            }

            output_dir = Path(temp_dir) / 'generated'
            result = generate_docs(spec, output_dir)

            endpoint_path = output_dir / 'payments' / 'createcharge.md'
            overview_path = output_dir / 'overview.md'

            self.assertEqual(1, result['count'])
            self.assertTrue(endpoint_path.exists())
            self.assertTrue(overview_path.exists())

            endpoint_text = endpoint_path.read_text(encoding='utf-8')
            self.assertIn('# Create charge', endpoint_text)
            self.assertIn('## Authentication', endpoint_text)
            self.assertIn('Bearer token in `Authorization` header.', endpoint_text)
            self.assertIn('## Request body', endpoint_text)
            self.assertIn('application/json', endpoint_text)
            self.assertIn('## Example request', endpoint_text)
            self.assertIn('Authorization: Bearer <token>', endpoint_text)

            overview_text = overview_path.read_text(encoding='utf-8')
            self.assertIn('# Payments API API Reference', overview_text)
            self.assertIn('[Open doc](./payments/createcharge.md)', overview_text)

    def test_generate_docs_supports_swagger_two_body_parameters(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            spec = {
                'swagger': '2.0',
                'info': {'title': 'Orders API', 'version': '1.0.0'},
                'host': 'api.example.com',
                'basePath': '/v1',
                'schemes': ['https'],
                'paths': {
                    '/orders': {
                        'post': {
                            'summary': 'Create order',
                            'description': 'Create a new order.',
                            'consumes': ['application/json'],
                            'parameters': [
                                {
                                    'name': 'body',
                                    'in': 'body',
                                    'required': True,
                                    'schema': {
                                        'type': 'object',
                                        'properties': {
                                            'amount': {'type': 'integer'},
                                            'currency': {'type': 'string'},
                                        },
                                    },
                                }
                            ],
                            'responses': {
                                '201': {
                                    'description': 'Created',
                                    'schema': {'type': 'object'},
                                }
                            },
                        }
                    }
                },
            }

            output_dir = Path(temp_dir) / 'generated'
            generate_docs(spec, output_dir)

            endpoint_path = output_dir / 'general' / 'post-orders.md'
            endpoint_text = endpoint_path.read_text(encoding='utf-8')

            self.assertIn('https://api.example.com/v1/orders', endpoint_text)
            self.assertIn('## Request body', endpoint_text)
            self.assertIn('application/json', endpoint_text)
            self.assertIn('## Responses', endpoint_text)


if __name__ == '__main__':
    unittest.main()