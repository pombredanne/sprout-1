import httplib


class WebServer(object):
    def __init__(self, host):
        self.host = host

    def _make_request(self, method, url, data, headers):
        conn = httplib.HTTPConnection(self.host)
        params = None
        if headers is None:
            headers = {}

        if data is not None and not isinstance(data, basestring):
            params = urllib.urlencode(data)
        else:
            params = data

        conn.request(method.upper(), url, params, headers)
        response = conn.getresponse()
        data = response.read()
        response.body = data
        response.status_line = "%03d %s" % (response.status, response.reason)
        conn.close
        return response

    def get(self, url, data=None, headers=None):
        return self._make_request("GET", url, data, headers)

    def post(self, url, data=None, headers=None):
        return self._make_request("POST", url, data, headers)
