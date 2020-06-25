#!/usr/bin/env bash

pip uninstall en2an -y

python setup.py clean
python setup.py install
