#!/usr/bin/env bash

pip uninstall cn2an -y

python setup.py clean
python setup.py install
