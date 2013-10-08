import urllib

def artifact_url(cfg):
    """ Get the URL to retrieve this artifact from Nexus. """
    params = { 'todo' : 'todo'}

    url = "http://%(hostname)s/service/local/artifact/maven/redirect?%(qs)s" % {
        'hostname' : cfg.settings.get('nexus_hostname'),
        'qs' : urllib.urlencode(params)
    }
    return url;
