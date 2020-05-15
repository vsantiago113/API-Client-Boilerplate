from api import APIPlugin
import requests
from requests.auth import HTTPBasicAuth


class Client(APIPlugin):
    headers = {'Content-Type': 'application/json'}
    base_url = None

    def connect(self, url: str = '', username: str = '', password: str = ''):
        self.base_url = f'{url.strip("/")}/api/{self.api_version}'
        response = requests.post(f'{self.base_url}', auth=HTTPBasicAuth(username, password),
                                 headers=self.headers, verify=self.verify)

        return response

    def disconnect(self):
        pass
