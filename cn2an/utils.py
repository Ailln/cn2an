import os
import yaml


def get_default_conf():
    with open(f"{os.path.dirname(__file__)}/config.yaml", "r", encoding="utf-8") as f_config:
        config_data = yaml.load(f_config, Loader=yaml.FullLoader)
    return config_data


if __name__ == "__main__":

    get_default_conf()
