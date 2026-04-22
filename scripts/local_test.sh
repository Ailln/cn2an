#!/usr/bin/env bash

set -euo pipefail

PROJECT_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
LINT_TARGETS=(cn2an example setup.py)

if [[ -z "${PYTHON_VERSIONS:-}" ]]
then
  if [[ "$(uname -s)" == "Darwin" && "$(uname -m)" == "arm64" ]] && arch -x86_64 /usr/bin/true >/dev/null 2>&1
  then
    # uv has no native macOS arm64 CPython 3.7 builds; use Rosetta for 3.7 on Apple Silicon.
    PYTHON_VERSIONS="cpython-3.7.9-macos-x86_64-none 3.8.20 3.9.22 3.10.17 3.11.12 3.12.10 3.13.3"
  else
    PYTHON_VERSIONS="3.7.9 3.8.20 3.9.22 3.10.17 3.11.12 3.12.10 3.13.3"
  fi
fi
TMP_ROOT=$(mktemp -d "${PROJECT_ROOT}/.cn2an-test.XXXXXX")
export UV_CACHE_DIR="${TMP_ROOT}/uv-cache"
export UV_PYTHON_INSTALL_DIR="${TMP_ROOT}/python"

cleanup() {
  rm -rf "${TMP_ROOT}"
}
trap cleanup EXIT

cd "${PROJECT_ROOT}"

for python_version in ${PYTHON_VERSIONS}
do
  env_dir="${TMP_ROOT}/py${python_version//./}"
  python_bin="${env_dir}/bin/python"

  echo -e "\nTest for Python ${python_version}...\n"

  echo "Install uv-managed Python ${python_version}"
  uv python install "${python_version}"

  echo "Create temporary uv environment"
  uv venv --managed-python --python "${python_version}" "${env_dir}"

  echo "Install dependencies"
  uv pip install --python "${python_bin}" -r requirements.txt flake8 pytest

  echo "Lint with flake8"
  # stop the build if there are Python syntax errors or undefined names
  "${python_bin}" -m flake8 "${LINT_TARGETS[@]}" --count --select=E9,F63,F7,F82 --show-source --statistics
  # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
  "${python_bin}" -m flake8 "${LINT_TARGETS[@]}" --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

  echo -e "Test with pytest\n"
  "${python_bin}" -m pytest

  echo "Remove temporary uv environment"
  rm -rf "${env_dir}"
done
