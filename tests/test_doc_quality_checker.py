import tempfile
import unittest
from pathlib import Path

from doc_quality_checker import scan_docs


class DocumentationQualityCheckerTests(unittest.TestCase):
    def write_file(self, root_dir, relative_path, content):
        target_path = Path(root_dir) / relative_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(content, encoding='utf-8')
        return target_path

    def test_extensionless_markdown_link_resolves(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            self.write_file(temp_dir, 'guide/intro.md', '# Intro\n\nSee [Setup](./setup).\n')
            self.write_file(temp_dir, 'guide/setup.md', '# Setup\n')

            issues, summary = scan_docs(temp_dir, check_remote=False)

            self.assertEqual([], issues)
            self.assertEqual(2, summary['files_scanned'])

    def test_missing_image_is_reported(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            self.write_file(temp_dir, 'guide/intro.md', '# Intro\n\n![Diagram](./images/missing.png)\n')

            issues, _ = scan_docs(temp_dir, check_remote=False)

            self.assertEqual(1, len(issues))
            self.assertEqual('missing image', issues[0]['type'])

    def test_invalid_anchor_is_reported(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            self.write_file(temp_dir, 'guide/intro.md', '# Intro\n\nSee [API](./api.md#does-not-exist).\n')
            self.write_file(temp_dir, 'guide/api.md', '# API Reference\n')

            issues, _ = scan_docs(temp_dir, check_remote=False)

            self.assertEqual(1, len(issues))
            self.assertEqual('invalid reference', issues[0]['type'])

    def test_valid_anchor_reference_passes(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            self.write_file(temp_dir, 'guide/intro.md', '# Intro\n\nSee [API](./api.md#api-reference).\n')
            self.write_file(temp_dir, 'guide/api.md', '# API Reference\n')

            issues, _ = scan_docs(temp_dir, check_remote=False)

            self.assertEqual([], issues)


if __name__ == '__main__':
    unittest.main()