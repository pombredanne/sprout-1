from fabric.api import local
import json
from pprint import pprint
from sprout import config

__all__ = ['get_artifacts', 'deploy']

def get_artifacts(config_file):
    pass
    

def deploy(config_file):
    c = config.load_config(config_file)


