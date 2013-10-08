from sprout import * 
import unittest

class NexusTest(unittest.TestCase):

    def test_artifact_url(self):
        """ build artifact url from configuration. """
        cfg = config.Config() 
        cfg.settings['nexus_hostname'] = 'nexus'
        result = nexus.artifact_url(cfg)
        self.assertEquals(
            "http://nexus/service/local/artifact/maven/redirect?todo=todo",
            result)
