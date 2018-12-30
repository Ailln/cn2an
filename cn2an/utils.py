# encoding: utf-8
import codecs

import yaml

def get_default_conf():
    with codecs.open("./cn2an/config.yaml", "r", encoding="utf-8") as f_config:
        config_data = yaml.load(f_config)
    return config_data
 