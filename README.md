
# RepoReady

A lightweight Python CLI tool that checks repositories for essential files and basic documentation issues.

## Features

- Checks for a README, `.gitignore`, and license.
- Detects an empty README.
- Reports passed and missing checks.
- Accepts a project folder path as input.
- Uses Python's standard library.

## Requirements 

- Python 3.10 or later

No external packages are required.

## Usage

Run the checker from your terminal:

```bash
python repoready.py .
```

To check a different project folder:

```bash
python repoready.py "path/to/your/project"
```

## Example Output

```text
RepoReady - Repository Check
====================================
[PASS   ] README.md - Project documentation
[MISSING] .gitignore - Git ignore rules
[PASS   ] LICENSE - Project license
[PASS   ] README content - Non-empty README
====================================
Result: 3/4 checks passed
```

The output depends on which files are present in the folder being checked.

## Project Structure

```text
repoready/
├── repoready.py
├── test_repoready.py
├── README.md
├── .gitignore
└── LICENSE
```

## Current Limitations

- Checks a small set of common repository files.
- Does not validate license text or inspect code quality.
- Does not guarantee that a repository is secure or production-ready.

## Future Improvements

- Export reports to a file.
- Add automated tests for different folder structures.
- Check for common project configuration files.

## License

Distributed under the MIT License.
