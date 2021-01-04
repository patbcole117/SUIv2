import json
import os

def get_config(f=False):
    if f:
        with open('app/mnt/config.txt', 'r') as config:
            config = json.load(config)
    else:
        config = {'SUI_HOST': os.getenv('SUI_HOST'),'SUI_PORT': os.getenv('SUI_PORT'), 'SUI_SBO_URL': os.getenv('SUI_SBO_URL'), 'SUI_SDC_URL': os.getenv('SUI_SDC_URL')}
    return config