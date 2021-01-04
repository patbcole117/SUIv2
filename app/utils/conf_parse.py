import json
import os

def get_config():
    config = {'SUI_HOST': os.getenv('SUI_HOST'),'SUI_PORT': os.getenv('SUI_PORT'), 'SUI_SBO_URL': os.getenv('SUI_SBO_URL'), 'SUI_SDC_URL': os.getenv('SUI_SDC_URL')}
    return config