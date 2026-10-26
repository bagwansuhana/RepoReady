
import tempfile
import unittest
from pathlib import Path

from repoready import check_repository


class TestRepoReady(unittest.TestCase):

    def test_all_essential_files_present(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)

            for filename in ("README.md", ".gitignore", "LICENSE"):
                (root / filename).write_text(
                    "Sample content", encoding="utf-8"
                )

            results = check_repository(root)
            self.assertTrue(all(passed for _, _, passed in results))

    def test_missing_files_are_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            results = check_repository(temp)

            missing = [
                filename
                for filename, _, passed in results
                if not passed
            ]

            self.assertIn("README.md", missing)
            self.assertIn(".gitignore", missing)
            self.assertIn("LICENSE", missing)

    def test_empty_readme_is_detected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("", encoding="utf-8")

            results = check_repository(root)
            readme_check = [
                passed
                for filename, _, passed in results
                if filename == "README content"
            ]

            self.assertEqual(readme_check, [False])


if __name__ == "__main__":
    unittest.main()
