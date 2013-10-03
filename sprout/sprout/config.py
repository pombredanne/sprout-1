import json
from pprint import pprint

class Config(object):
    
    def load(self, config_file):
        """ Load config data from a file. """
        with open(config_file) as f:
            self.data = json.load(f)
        self.__substitute_variables()

    def load_data(self, artifacts_list, variables_dict):
        """ Load config data from a list and dictionary. """
        self.data = { 
            "artifacts" : artifacts_list,
            "variables" : variables_dict
        }
        self.__substitute_variables()

    def __substitute_variables(self):
        """
        Go through all the configuration data and apply all 
        variable substitutions.
        """
        # ok, admittedly this is a lame way to do this.
        # TODO replace quick n dirty with an elegant fix later.
        # because this is just sad... :(
        for i in range(len(self.artifacts)):
            for var, value in self.variables.items():
                self.artifacts[i] = self.artifacts[i].replace(var, value)

    @property
    def artifacts(self):
        return self.data["artifacts"]

    @property
    def variables(self):
        return self.data["variables"]

