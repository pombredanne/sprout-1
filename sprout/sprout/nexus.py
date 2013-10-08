import urllib

def artifact_url(nexus_hostname, artifact):
    """ Get the URL to retrieve this artifact from Nexus. """
    params = { 
        'r' : artifact.repository,
        'g' : artifact.group_id,
        'a' : artifact.artifact_id,
        'v' : artifact.version
    }
    if artifact.classifier:
        params['c'] = artifact.classifier

    url = "http://%(hostname)s/service/local/artifact/maven/redirect?%(qs)s" % {
        'hostname' : nexus_hostname,
        'qs' : urllib.urlencode(params)
    }
    return url;


class Artifact(object):
    
    def __init__(self, group_id, artifact_id, version=None, classifier=None, repository=None):
        if version is None:
            version = 'LATEST'

        self.repository = repository
        self.group_id = group_id
        self.artifact_id = artifact_id
        self.version = version
        self.classifier = classifier

    def __str__(self):
        return "<Artifact %s %s %s %s>" % (
            self.repository, 
            self.group_id,
            self.artifact_id,
            self.version,
            self.classifier
        )
