#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh

## conda env create
env_list=$(conda env list)
for env in "py369" "py374" "py383"
do
  if [[ $env_list =~ $env ]]
  then
    echo "$env env has been created."
  else
    echo "$env env is being created..."
    conda create -n $env python=${env:2:1}.${env:3:1}.${env:4:1} -y
  fi
done

## py369
echo -e "\nTest for python 3.6.9...\n"

conda activate py369

echo "Install dependencies"
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Lint with flake8"
pip install flake8
# stop the build if there are Python syntax errors or undefined names
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

echo "Test with pytest"
pip install pytest
pytest

conda deactivate

## py374
echo -e "\nTest for python 3.7.4...\n"
conda activate py374

echo "Install dependencies"
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Lint with flake8"
pip install flake8
# stop the build if there are Python syntax errors or undefined names
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

echo "Test with pytest"
pip install pytest
pytest

conda deactivate

## py383
echo -e "\nTest for python 3.8.3...\n"
conda activate py383

echo "Install dependencies"
python -m pip install --upgrade pip
pip install -r requirements.txt

echo "Lint with flake8"
pip install flake8
# stop the build if there are Python syntax errors or undefined names
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

echo "Test with pytest"
pip install pytest
pytest

conda deactivate
