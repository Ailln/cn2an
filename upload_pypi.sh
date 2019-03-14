#!/usr/bin/env bash

python setup.py sdist
twine upload dist/*