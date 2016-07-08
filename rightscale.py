from libcloud.compute.providers import get_driver
import yaml

import logging
logging.basicConfig(filename='libcloud.log', level=logging.DEBUG)


def get_configuration():
    config = {}
    with open('config.yaml', 'r') as file:
        config_text = file.read()
        config = yaml.load(config_text)
    return config


def get_connection(config=None):
    if config is None:
        config = get_configuration()
    cls = get_driver(config['provider'])
    driver = cls(**config['connection'])
    return driver


def map(config, map_name, dictionary, extra_dictionary):
    if 'maps' not in config.keys():
        return
    if map_name not in config['maps'].keys():
        return
    for key, value in config['maps'][map_name].items():
        mapped_value = extra_dictionary.get(value, None)
        dictionary[key] = mapped_value
    return dictionary
