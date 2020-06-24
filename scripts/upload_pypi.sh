#!/usr/bin/env bash

rm dist/*
python setup.py clean
python setup.py sdist bdist_wheel

pip install -r requirements_dev.txt
twine upload dist/*