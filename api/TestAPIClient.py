from api import APIPlugin
import requests
from requests.auth import HTTPBasicAuth
import inspect


class Client(APIPlugin):
    headers = None
    base_url = None
    token = None
    refresh_token = None

    def connect(self, url: [str, None] = None, username: [str, bytes] = '', password: [str, bytes] = ''):
        self.base_url = f'{url.strip("/")}/api/{self.api_version}'
        response = requests.post(f'{self.base_url}/generatetoken', auth=HTTPBasicAuth(username, password), verify=False)
        self.token = response.headers.get('X-Example-access-token')
        self.refresh_token = response.headers.get('X-Example-refresh-token')
        self.headers = {'Content-Type': 'application/json', 'X-Example-access-token': self.token}
        return response

    def disconnect(self):
        return requests.post(f'{self.base_url}/revoketoken')

    def get_lets_get_all_routers(self, *args, url: [str, None] = None, data: dict = None,
                                 auth: HTTPBasicAuth = None, placeholder='x',  split_method: [str, None] = None,
                                 **kwargs) -> requests.Response:
        http_method = inspect.stack()[0][3].split('_')[0].upper()
        method = '_'.join(inspect.stack()[0][3].split('_')[1:])
        method = '/'.join(method.split(split_method)) if split_method is not None else method
        if args:
            method = method.replace(placeholder, '{}').format(*args)
        return requests.request(http_method, f'{self.base_url.strip("/")}/{method}' if url is None else url,
                                headers=self.headers, verify=self.verify, json=data, auth=auth, params=kwargs)

    def get_routers(self, *args, url: [str, None] = None, data: dict = None,
                    auth: HTTPBasicAuth = None, placeholder='x',  split_method: [str, None] = '_',
                    **kwargs) -> requests.Response:
        http_method = inspect.stack()[0][3].split('_')[0].upper()
        method = '_'.join(inspect.stack()[0][3].split('_')[1:])
        method = '/'.join(method.split(split_method)) if split_method is not None else method
        if args:
            method = method.replace(placeholder, '{}').format(*args)
        return requests.request(http_method, f'{self.base_url.strip("/")}/{method}' if url is None else url,
                                headers=self.headers, verify=self.verify, json=data, auth=auth, params=kwargs)

    def get_routers_x(self, *args, url: [str, None] = None, data: dict = None,
                      auth: HTTPBasicAuth = None, placeholder='x',  split_method: [str, None] = '_',
                      **kwargs) -> requests.Response:
        http_method = inspect.stack()[0][3].split('_')[0].upper()
        method = '_'.join(inspect.stack()[0][3].split('_')[1:])
        method = '/'.join(method.split(split_method)) if split_method is not None else method
        if args:
            method = method.replace(placeholder, '{}').format(*args)
        return requests.request(http_method, f'{self.base_url.strip("/")}/{method}' if url is None else url,
                                headers=self.headers, verify=self.verify, json=data, auth=auth, params=kwargs)

    def post_routers(self, *args, url: [str, None] = None, data: dict = None,
                     auth: HTTPBasicAuth = None, placeholder='x',  split_method: [str, None] = '_',
                     **kwargs) -> requests.Response:
        http_method = inspect.stack()[0][3].split('_')[0].upper()
        method = '_'.join(inspect.stack()[0][3].split('_')[1:])
        method = '/'.join(method.split(split_method)) if split_method is not None else method
        if args:
            method = method.replace(placeholder, '{}').format(*args)
        return requests.request(http_method, f'{self.base_url.strip("/")}/{method}' if url is None else url,
                                headers=self.headers, verify=self.verify, json=data, auth=auth, params=kwargs)

    def put_routers_x(self, *args, url: [str, None] = None, data: dict = None,
                      auth: HTTPBasicAuth = None, placeholder='x',  split_method: [str, None] = '_',
                      **kwargs) -> requests.Response:
        http_method = inspect.stack()[0][3].split('_')[0].upper()
        method = '_'.join(inspect.stack()[0][3].split('_')[1:])
        method = '/'.join(method.split(split_method)) if split_method is not None else method
        if args:
            method = method.replace(placeholder, '{}').format(*args)
        return requests.request(http_method, f'{self.base_url.strip("/")}/{method}' if url is None else url,
                                headers=self.headers, verify=self.verify, json=data, auth=auth, params=kwargs)

    def delete_routers_x(self, *args, url: [str, None] = None, data: dict = None,
                         auth: HTTPBasicAuth = None, placeholder='x',  split_method: [str, None] = '_',
                         **kwargs) -> requests.Response:
        http_method = inspect.stack()[0][3].split('_')[0].upper()
        method = '_'.join(inspect.stack()[0][3].split('_')[1:])
        method = '/'.join(method.split(split_method)) if split_method is not None else method
        if args:
            method = method.replace(placeholder, '{}').format(*args)
        return requests.request(http_method, f'{self.base_url.strip("/")}/{method}' if url is None else url,
                                headers=self.headers, verify=self.verify, json=data, auth=auth, params=kwargs)
