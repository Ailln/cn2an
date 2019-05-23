#!/usr/bin/env bash

source /anaconda3/etc/profile.d/conda.sh

echo -e "\nTest for python 3.6.3...\n"
conda activate py363

pip install -r requirements.txt --ignore-installed

python -m cn2an.cn2an_test
python -m cn2an.an2cn_test

conda deactivate

echo -e "\nTest for python 3.7.3...\n"
conda activate py373

pip install -r requirements.txt --ignore-installed

python -m cn2an.cn2an_test
python -m cn2an.an2cn_test

conda deactivate
