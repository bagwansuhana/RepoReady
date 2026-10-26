# RepoReady

A lightweight Python CLI tool that checks GitHub repositories for essential files, basic documentation, and common project setup issues.

## Features

- **Essential file checks:** Checks for `README.md`, `.gitignore`, and `LICENSE`.
- **README validation:** Detects whether the README file is empty.
- **Potential secret-file detection:** Warns about common sensitive filenames, such as `.env`, `credentials.json`, and `secrets.json`.
- **Command-line interface:** Check a project directory directly from your terminal.
- **Automated tests:** Unit tests cover essential file checks, missing files, and empty README detection.

## Project Structure

```text
RepoReady/
├── repoready.py
├── test_repoready.py
├── README.md
├── .gitignore
└── LICENSE
```

## Requirements

- Python 3.10 or newer
- No third-party packages required for the core checker

## Usage

Clone the repository:

```bash
git clone https://github.com/bagwansuhana/RepoReady.git
cd RepoReady
```

Check the current directory:

```bash
python repoready.py
```

Check another project directory:

```bash
python repoready.py "path/to/your/project"
```

## Run Tests

```bash
python -m unittest -v
```

## Example Output

```text
RepoReady - Repository Check
=============================================
[PASS   ] README.md - Project documentation
[PASS   ] .gitignore - Git ignore rules
[PASS   ] LICENSE - Project license
[PASS   ] README content - Non-empty README
=============================================
Checks passed: 4/4
Warnings: 0
```

Actual output depends on the files in the directory being checked.

## Limitations

- Secret detection currently checks a predefined list of filenames in the project root.
- It does not scan file contents or Git history for exposed credentials.
- It is a basic repository checklist, not a replacement for a dedicated security scanner.

## Future Improvements

- Export check results to a report file.
- Add configurable checks.
- Support recursive directory scanning.
- Integrate additional repository quality checks.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
