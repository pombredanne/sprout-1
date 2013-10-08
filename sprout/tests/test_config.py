import sprout.config
import unittest

class ConfigTest(unittest.TestCase):

    def test_variable_subst(self):
        """ one variable substitution """
        cfg = sprout.config.load_data( 
            {
                "variables" :  { "$FOO" : "realvalue" },
                "artifacts" : ["http://$FOO/bar", "http://$FOO/baz"],
                "settings" : { }
            })
        self.assertEquals("http://realvalue/bar", cfg.artifacts[0])
        self.assertEquals("http://realvalue/baz", cfg.artifacts[1])


    def test_multi_variable_subst(self):
        """ multi-variable substitution """
        cfg = sprout.config.load_data(
            {
                "variables" : { "$FOO" : "f", "$BAR" : "b" },
                "artifacts" : ["http://$FOO/$BAR", "https://$FOO/$BAR"],
                "settings" : {}
            })
        self.assertEquals("http://f/b", cfg.artifacts[0])
        self.assertEquals("https://f/b", cfg.artifacts[1])


    def test_no_variables(self):
        cfg = sprout.config.load_data(
            {
                "artifacts" : ["x", "y"],
                "settings" : {}
            })
        self.assertEquals("x", cfg.artifacts[0])
        self.assertEquals("y", cfg.artifacts[1])
        self.assertEquals({}, cfg.variables)
        self.assertEquals({}, cfg.settings)


    def test_no_artifacts(self):
        cfg = sprout.config.load_data(
            {
                "settings" : {'x':'y'},
                "variables" : { '$X' : 'xx'}
            })
        self.assertEquals([], cfg.artifacts)
        self.assertEquals('xx', cfg.variables.get('$X'))
        self.assertEquals('y', cfg.settings.get('x'))
    

    def test_no_settings(self):
        cfg = sprout.config.load_data(
            {
                "artifacts" : ["x", "y"],
                "variables" : { '$X' : 'xx'}
            })
        self.assertEquals("x", cfg.artifacts[0])
        self.assertEquals("y", cfg.artifacts[1])
        self.assertEquals('xx', cfg.variables.get('$X'))
        self.assertEquals({}, cfg.settings)


