import os

import yaml


def get_default_conf():
    with open("{current_path}/config.yaml".format(current_path=os.path.dirname(__file__)), "r", encoding="utf-8") as f_config:
        config_data = yaml.load(f_config, Loader=yaml.FullLoader)
    return config_data
