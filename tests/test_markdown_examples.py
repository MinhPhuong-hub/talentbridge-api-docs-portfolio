"""Regression tests: malformed copyable examples must fail verification."""
import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_markdown_examples.py'
spec = importlib.util.spec_from_file_location('example_checks', SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DocumentationExampleTests(unittest.TestCase):
    def setUp(self):
        module.ERRORS.clear()

    def test_valid_curl(self):
        module.check_curl("curl -H 'Prefer: example=normal' http://127.0.0.1:4010/jobs", 'test')
        self.assertEqual(module.ERRORS, [])

    def test_missing_endpoint_is_detected(self):
        module.check_curl('curl http://127.0.0.1:4010/unknown', 'test')
        self.assertTrue(any('no GET operation' in e for e in module.ERRORS))

    def test_invalid_json_body_is_detected(self):
        module.check_curl("curl -X POST http://127.0.0.1:4010/jobs -H 'Authorization: Bearer demo' -H 'Content-Type: application/json' -d '{broken}'", 'test')
        self.assertTrue(any('not valid JSON' in e for e in module.ERRORS))

    def test_invalid_json_body_schema_is_detected(self):
        module.check_curl("curl -X POST http://127.0.0.1:4010/jobs -H 'Authorization: Bearer demo' -H 'Content-Type: application/json' -d '{\"title\":\"A\",\"description\":\"Short\",\"location\":\"Hanoi\"}'", 'test')
        self.assertTrue(any('schema violation' in e for e in module.ERRORS))

    def test_missing_auth_header_is_detected(self):
        module.check_curl("curl -X PATCH http://127.0.0.1:4010/applications/app_456 -H 'Content-Type: application/json' -d '{\"status\":\"accepted\"}'", 'test')
        self.assertTrue(any('missing Authorization' in e for e in module.ERRORS))


if __name__ == '__main__':
    unittest.main()
