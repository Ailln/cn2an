import os

import yaml


def get_default_conf():
    with open(f"{os.path.dirname(__file__)}/config.yaml", "r") as f_config:
        config_data = yaml.load(f_config, Loader=yaml.FullLoader)
    return config_data
