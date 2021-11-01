#!/usr/bin/env bash

source ~/opt/anaconda3/etc/profile.d/conda.sh

## conda env create
env_list=$(conda env list)
for env in py3613 py3711 py3811
do
  if [[ $env_list =~ $env ]]
  then
    echo "${env} has been created."
  else
    echo "${env} is being created..."
    conda create -n $env python=${env:2:1}.${env:3:1}.${env:4:1} -y
  fi

  echo -e "\nTest for ${env}...\n"

  conda activate ${env}

  echo "Install dependencies"
  python -m pip install --upgrade pip
  pip install -r requirements.txt

  echo "Lint with flake8"
  pip install flake8
  # stop the build if there are Python syntax errors or undefined names
  flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
  # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
  flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

  echo -e "Test with pytest\n"
  pip install pytest
  pytest

  conda deactivate
done
