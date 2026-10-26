

from pathlib import Path
import argparse

ESSENTIAL_FILES = {
    "README.md": "Project documentation",
    ".gitignore": "Git ignore rules",
    "LICENSE": "Project license",
}

def check_repository(folder):
    root = Path(folder).expanduser().resolve()

    if not root.is_dir():
        raise NotADirectoryError(f"Not a valid folder: {root}")

    results = []

    for filename, description in ESSENTIAL_FILES.items():
        exists = (root / filename).is_file()
        results.append((filename, description, exists))

    readme = root / "README.md"
    if readme.is_file():
        content = readme.read_text(encoding="utf-8", errors="replace")
        has_content = bool(content.strip())
        results.append(
            ("README content", "Non-empty README", has_content)
        )

    return results

def display_report(results):
    print("\nRepoReady - Repository Check")
    print("=" * 36)

    for filename, description, passed in results:
        status = "PASS" if passed else "MISSING"
        print(f"[{status:7}] {filename} - {description}")

    total = len(results)
    passed = sum(1 for _, _, ok in results if ok)

    print("=" * 36)
    print(f"Result: {passed}/{total} checks passed")

def main():
    parser = argparse.ArgumentParser(
        description="Check a project folder for essential repository files."
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Path to the project folder (default: current directory)",
    )
    args = parser.parse_args()

    try:
        results = check_repository(args.folder)
        display_report(results)
    except (NotADirectoryError, OSError) as error:
        parser.error(str(error))

if __name__ == "__main__":
    main()
