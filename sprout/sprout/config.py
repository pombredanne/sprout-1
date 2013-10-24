import json
from collections import namedtuple 
from pprint import pprint
from sprout import nexus, installers

def load_config(config_file):
    """ Load config data from a file. """
    with open(config_file) as f:
        rawdata = json.load(f)
        # returns a new instance of Config with data from config_file
        return load_data(rawdata)

def load_data(data):
    """ Load config data from a dictionary. """
    return Config(data.get('artifacts'), data.get('variables'), data.get('settings'), data.get('installers'))

class Config(object):

    def __init__(self, artifacts=[], variables={}, settings={}, installer_list={}):
        if artifacts is None:
            artifacts = []
        if variables is None:
            variables = {}
        if settings is None:
            settings = {}
        if installer_list is None:
            installer_list = {}

        self.variables = variables
        self.settings = settings

        # convert artifact dictionary to a list of nexus.Artifact objects
        self.artifacts = nexus.artifact_dict_to_list(artifacts,
            self.get_setting('default_version'),
            self.get_setting('default_classifier'),
            self.get_setting('default_repository'))

        # convert installers dict to list of installers
        self.installer_list = installers.dict_to_list(installer_list)

    def get_setting(self, setting_name):
        return self.settings.get(setting_name, None)
