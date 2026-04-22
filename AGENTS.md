# AGENTS.md

Guidance for coding agents working in this repository.

## Project Overview

- `cn2an` is a Python package for converting between Chinese numerals and Arabic numerals, plus sentence-level transformations.
- Public package entry points are exported from `cn2an/__init__.py`: `cn2an`, `an2cn`, and `transform`.
- Core implementation files are:
  - `cn2an/cn2an.py` for Chinese numeral to Arabic numeral conversion.
  - `cn2an/an2cn.py` for Arabic numeral to Chinese numeral conversion.
  - `cn2an/transform.py` for converting numerals inside text.
  - `cn2an/conf.py` for conversion dictionaries and constants.
- Examples live in `example/`.

## Environment

- The package supports Python `>=3.6`; avoid syntax or stdlib features that would break Python 3.6 unless support is intentionally changed.
- Runtime dependencies are listed in `requirements.txt`.
- Test and release helper dependencies are listed in `requirements_test.txt` and `requirements_dev.txt`.
- The comprehensive local test script uses `uv` to create temporary environments for multiple Python versions.

## Common Commands

- Install runtime dependency:
  ```bash
  pip install -r requirements.txt
  ```
- Run the default test suite in the current environment:
  ```bash
  python -m pytest
  ```
- Run the full local validation matrix:
  ```bash
  bash scripts/local_test.sh
  ```
- Run the same lint checks used by `scripts/local_test.sh`:
  ```bash
  python -m flake8 cn2an example setup.py --count --select=E9,F63,F7,F82 --show-source --statistics
  python -m flake8 cn2an example setup.py --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
  ```
- Run the performance benchmark:
  ```bash
  python -m cn2an.performance
  ```

## Coding Conventions

- Keep edits small and focused on the requested behavior.
- Preserve Python 3.6 compatibility, including type annotation syntax.
- Follow the existing class-based converter style and keep public behavior reachable through `cn2an/__init__.py`.
- Keep user-facing exceptions and warnings consistent with the current Chinese messages.
- Prefer `Decimal` or existing conversion helpers for numeric edge cases where float representation can lose precision.
- Keep comments useful and brief; do not add comments that simply restate the code.
- Do not commit generated artifacts such as `build/`, `dist/`, `*.egg-info/`, `.pytest_cache/`, or temporary `.cn2an-test.*` directories.

## Testing Guidance

- Add or update tests beside the relevant module using the existing `unittest` style:
  - `cn2an/cn2an_test.py`
  - `cn2an/an2cn_test.py`
  - `cn2an/transform_test.py`
- For converter changes, cover all affected modes:
  - `cn2an`: `strict`, `normal`, and `smart` where relevant.
  - `an2cn`: `low`, `up`, `rmb`, and `direct` where relevant.
- Include regression cases for invalid inputs when changing validation logic.
- Run at least `python -m pytest` before finishing code changes. Use `bash scripts/local_test.sh` when compatibility or packaging risk is meaningful.

## Release Notes

- The package version is defined in `cn2an/__init__.py`.
- Packaging metadata is in `setup.py`.
- Release helper scripts are in `scripts/`; inspect them before changing packaging or publishing behavior.
