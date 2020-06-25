import os

import yaml


def get_default_conf() -> dict:
    with open(f"{os.path.dirname(__file__)}/config.yaml", "r", encoding="utf-8") as f_config:
        config_data = yaml.load(f_config, Loader=yaml.FullLoader)
    return config_data
