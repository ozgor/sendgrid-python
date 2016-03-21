import python_http_client
import json
import os
import base64
from .version import __version__

class SendGridAPIClient(object):
    """SendGrid API."""
    def __init__(self, **opts):
        """
        Construct SendGrid v3 API object.

        :params host: Base URL for the API call
        :type host: string

        """
        self.path = opts.get('path', os.path.abspath(os.path.dirname(__file__)))
        python_http_client.Config(self.path)
        self.useragent = 'sendgrid/{0};python_v3'.format(__version__)
        self.host = opts.get('host', 'https://api.sendgrid.com')
        self.version = __version__

        if (opts.get('apikey') != None):
            self._apikey = opts.get('apikey', os.environ.get('SENDGRID_API_KEY'))
            authorization = 'Bearer {0}'.format(self._apikey)
        else:
            login = opts.get('login')
            password = opts.get('password')
            self._auth_token = base64.b64encode(login + ':' + password)
            authorization = 'Basic {0}'.format(self._auth_token)

        headers = {
                    "Authorization": authorization,
                    "Content-Type": "application/json",
                    "User-agent": self.useragent
                  }

        self.client = python_http_client.Client(host=self.host,
                                                request_headers=headers,
                                                version=3)

    @property
    def apikey(self):
        return self._apikey

    @apikey.setter
    def apikey(self, value):
        self._apikey = value

    @property
    def auth_token(self):
        return self._auth_token

    @auth_token.setter
    def auth_token(self, value):
        self._auth_token = value
