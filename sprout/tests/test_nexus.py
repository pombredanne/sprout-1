from sprout import * 
import urlparse 
import unittest

class NexusTest(unittest.TestCase):

    def test_artifact_url(self):
        """ build artifact url. """
        artifact = nexus.Artifact('group_id', 'artifact_id', 'version', 'filename', 'classifier', 'repo')
        result = artifact.get_url('nexus')
        params = urlparse.parse_qs(result.split('?')[1])

        self.assertEquals('group_id', "".join(params['g']))
        self.assertEquals('artifact_id', "".join(params['a']))
        self.assertEquals('version', "".join(params['v']))
        self.assertEquals('classifier', "".join(params['c']))
        self.assertEquals('repo', "".join(params['r']))

    def test_artifact_url_no_classifier(self):
        """ build artifact url without a classifier """
        artifact = nexus.Artifact('group_id', 'artifact_id', 'version', 'filename', classifier=None, repository='repo')
        result = artifact.get_url('nexus')
        params = urlparse.parse_qs(result.split('?')[1])

        self.assertEquals('group_id', "".join(params['g']))
        self.assertEquals('artifact_id', "".join(params['a']))
        self.assertEquals('version', "".join(params['v']))
        self.assertNotIn('c', params)
        self.assertEquals('repo', "".join(params['r']))

    def test_artifact_without_required_properties(self):
        artifact = nexus.Artifact('group_id', 'artifact_id', None, None, None, None)

        self.assertEquals('LATEST', artifact.version)
        self.assertEquals('artifact_id', artifact.filename)
        self.assertIsNone(artifact.repository)
        self.assertIsNone(artifact.classifier)
