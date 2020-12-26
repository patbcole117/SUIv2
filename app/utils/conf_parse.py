import json
import re

def get_config():
    with open('app/mnt/config.txt', 'r') as config:
        config = json.load(config)
        return config