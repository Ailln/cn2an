#!/usr/bin/env bash

rm dist/*
python setup.py sdist
twine upload dist/*