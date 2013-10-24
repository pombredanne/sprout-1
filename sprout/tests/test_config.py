import sprout.config
import unittest

class ConfigTest(unittest.TestCase):

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
                "artifacts" : [
                    { "group_id" : "group", "artifact_id" : "x" },
                    { "group_id" : "group", "artifact_id" : "y" }
                ],
                "variables" : { '$X' : 'xx'}
            })
        self.assertEquals("x", cfg.artifacts[0].artifact_id)
        self.assertEquals("y", cfg.artifacts[1].artifact_id)
        self.assertEquals('xx', cfg.variables.get('$X'))
        self.assertEquals({}, cfg.settings)

    def test_convert_installers(self):
        cfg = sprout.config.load_data(
            {
                "artifacts" : [
                    { "group_id" : "group", "artifact_id" : "x" },
                    { "group_id" : "group", "artifact_id" : "y" }
                ],
                "installers" : [ 
                    {
                        "hostname" : "myhost",
                        "installer_type" : "izpack",
                        "installer_artifacts" : ["foo.jar", "bar.jar"],
                        "user_input_file" : "myhost.xml"
                    }]
            })
        self.assertEquals("myhost", cfg.installer_list[0].hostname)
        self.assertEquals("myhost.xml", cfg.installer_list[0].user_input_file)
        self.assertEquals("foo.jar", cfg.installer_list[0].installer_artifacts[0])
        self.assertEquals("bar.jar", cfg.installer_list[0].installer_artifacts[1])

 
