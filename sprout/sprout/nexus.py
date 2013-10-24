import urllib
import os
from subprocess import Popen, PIPE

def artifact_dict_to_list(artifact_list, default_version=None, default_classifier='installer', default_repository='public'):
    """ Given a list of artifact dictionaries, return a list of actual Artifact objects. """
    return [Artifact(
                a['group_id'], 
                a['artifact_id'], 
                a.get('version', default_version), 
                a.get('filename', None),
                a.get('classifier', default_classifier), 
                a.get('repository', default_repository)
           ) for a in artifact_list]


def local2(command, print_command=False):
    """Run a command, returning the exit code, output, and stderr."""
    p = Popen(command, stdout=PIPE, stderr=PIPE)
    if print_command: print " ".join(command)
    output, errput = p.communicate()
    return p.returncode, output, errput

class Artifact(object):
    
    def __init__(self, group_id, artifact_id, version, filename, classifier, repository):
        if version is None:
            version = 'LATEST'

        self.repository = repository
        self.group_id = group_id
        self.artifact_id = artifact_id
        self.version = version
        self.classifier = classifier
        if filename:
            self.filename = filename
        else:
            self.filename = artifact_id

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

    def download(self, nexus_hostname, target_dir):
        """ Attempt to download this artifact from nexus."""
        url = self.get_url(nexus_hostname)
        target_file = os.path.join(target_dir, self.filename)
        print("Will try to download from: %s and save as %s" % (url, target_file))
        curl_args = ['curl', '-sSLA', 'fabric-deploy', url, '-o', target_file]

        status, stdout, stderr = local2(curl_args)
        return status, stdout, stderr

    def __str__(self):
        return "<Artifact %s %s %s %s %s>" % (
            self.repository, 
            self.group_id,
            self.artifact_id,
            self.version,
            self.classifier
        )
