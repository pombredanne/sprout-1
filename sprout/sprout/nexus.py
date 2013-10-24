import urllib

def artifact_dict_to_list(artifact_list, default_version=None, default_classifier='installer', default_repository='public'):
    """ Given a list of artifact dictionaries, return a list of actual Artifact objects. """
    return [Artifact(
                a['group_id'], 
                a['artifact_id'], 
                a.get('version', default_version), 
                a.get('classifier', default_classifier), 
                a.get('repository', default_repository)
           ) for a in artifact_list]


class Artifact(object):
    
    def __init__(self, group_id, artifact_id, version=None, classifier=None, repository=None):
        if version is None:
            version = 'LATEST'

        self.repository = repository
        self.group_id = group_id
        self.artifact_id = artifact_id
        self.version = version
        self.classifier = classifier

    def get_url(self, nexus_hostname):
        """ Get the URL to retrieve this artifact from Nexus. """
        params = { 
            'r' : self.repository,
            'g' : self.group_id,
            'a' : self.artifact_id,
            'v' : self.version
        }
        if self.classifier:
            params['c'] = self.classifier

        url = "http://%(hostname)s/service/local/artifact/maven/redirect?%(qs)s" % {
            'hostname' : nexus_hostname,
            'qs' : urllib.urlencode(params)
        }
        return url;

    def __str__(self):
        return "<Artifact %s %s %s %s %s>" % (
            self.repository, 
            self.group_id,
            self.artifact_id,
            self.version,
            self.classifier
        )
