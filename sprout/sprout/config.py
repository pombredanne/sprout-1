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
    return Config(data.get('artifacts'), data.get('settings'), data.get('installers'))

class Config(object):

    def __init__(self, artifacts=[], settings={}, installer_list={}):
        if artifacts is None:
            artifacts = []
        if settings is None:
            settings = {}
        if installer_list is None:
            installer_list = {}

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

    def get_environment_dir(self):
        return self.get_setting('environment_dir')

    def get_local_temp_dir(self):
        return self.get_setting('local_temp_dir')

    def get_deploy_temp_dir(self):
        return self.get_setting('deploy_temp_dir')

    def get_remote_user(self):
        return self.get_setting('remote_user')
