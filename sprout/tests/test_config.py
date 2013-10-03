from sprout.config import Config
import unittest

class ConfigTest(unittest.TestCase):

    def test_variable_subst(self):
        """ one variable substitution """
        config = Config()
        config.load_data(
            ["http://$FOO/bar", "http://$FOO/baz"],
            { "$FOO" : "realvalue" })

        self.assertEquals("http://realvalue/bar", config.artifacts[0])
        self.assertEquals("http://realvalue/baz", config.artifacts[1])


    def test_multi_variable_subst(self):
        """ multi-variable substitution """
        config = Config()
        config.load_data(
            ["http://$FOO/$BAR", "https://$FOO/$BAR"],
            { "$FOO" : "f", "$BAR" : "b" })

        self.assertEquals("http://f/b", config.artifacts[0])
        self.assertEquals("https://f/b", config.artifacts[1])


