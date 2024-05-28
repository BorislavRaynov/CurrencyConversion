import json


CONFIG_FILE = 'config.json'


def load_api_key():
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
        return config['api_key']
