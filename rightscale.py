from libcloud.compute.providers import get_driver
import yaml


def get_connection():
    config = {}
    with open('config.yaml', 'r') as file:
        config_text = file.read()
        config = yaml.load(config_text)

    cls = get_driver(config['provider'])
    driver = cls(**config['connection'])
    return driver