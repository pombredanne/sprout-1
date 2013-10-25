import sprout.config
import unittest

class ConfigTest(unittest.TestCase):

    def test_no_artifacts(self):
        cfg = sprout.config.load_data(
            {
                "settings" : {'x':'y'},
            })
        self.assertEquals([], cfg.artifacts)
        self.assertEquals('y', cfg.settings.get('x'))
    

    def test_no_settings(self):
        cfg = sprout.config.load_data(
            {
                "artifacts" : [
                    { "group_id" : "group", "artifact_id" : "x" },
                    { "group_id" : "group", "artifact_id" : "y" }
                ]
            })
        self.assertEquals("x", cfg.artifacts[0].artifact_id)
        self.assertEquals("y", cfg.artifacts[1].artifact_id)
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
                        "artifact_files" : ["foo.jar", "bar.jar"],
                        "env_files" : ["myhost.xml"],
                        "install_script" : "make_it_so.sh"
                    }]
            })
        self.assertEquals("myhost", cfg.installer_list[0].hostname)
        self.assertEquals("myhost.xml", cfg.installer_list[0].env_files[0])
        self.assertEquals("foo.jar", cfg.installer_list[0].artifact_files[0])
        self.assertEquals("bar.jar", cfg.installer_list[0].artifact_files[1])
        self.assertEquals("make_it_so.sh", cfg.installer_list[0].install_script)

 
