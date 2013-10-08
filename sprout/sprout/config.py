import json
from collections import namedtuple 
from pprint import pprint


def load_config(config_file):
    """ Load config data from a file. """
    with open(config_file) as f:
        rawdata = json.load(f)
        # returns a new instance of Config with data from config_file
        return load_data(rawdata)

def load_data(data):
    """ Load config data from a dictionary. """
    return Config(data.get('artifacts'), data.get('variables'), data.get('settings'))

class Config(object):

    def __init__(self, artifacts=[], variables={}, settings={}):
        if artifacts is None:
            artifacts = []
        if variables is None:
            variables = {}
        if settings is None:
            settings = {}

        self.artifacts = artifacts
        self.variables = variables
        self.settings = settings
        self.substitute_variables()
    
    def substitute_variables(self):
        """
        Go through all the configuration data and apply all 
        variable substitutions.
        """
        # ok, admittedly this is a lame way to do this.
        # TODO replace quick n dirty with an elegant fix later.
        # because this is just sad... :(

        # TODO the second: this whole concept might go away, if
        # the newer data format works out.
        for i in range(len(self.artifacts)):
            for var, value in self.variables.items():
               self.artifacts[i] = self.artifacts[i].replace(var, value)
