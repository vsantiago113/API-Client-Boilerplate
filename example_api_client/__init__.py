"""
This is where you want to create the connection and disconnect methods.
"""

import requests
from requests.auth import HTTPBasicAuth
from example_api_client.api_interface import APIPlugin


class Client(APIPlugin):
    """
    This is where you want to create the connection and disconnect methods.
    """
    headers = None
    base_url = None
    token = None
    refresh_token = None

    def connect(self, url: [str, None] = None,
                username: [str, bytes] = '',
                password: [str, bytes] = '') -> requests.Response:
        """
        The connect method contains everything needed to create a connection to the
        API endpoint and authenticate.

        :param url: The URL for the API endpoint.
        :param username: The login username for the API endpoint.
        :param password: The login password for the API endpoint.
        :return: requests.Response
        """
        self.base_url = f'{url.strip("/")}/api/{self.api_version}'
        response = requests.post(f'{self.base_url}/generatetoken',
                                 auth=HTTPBasicAuth(username, password),
                                 verify=False)
        self.token = response.headers.get('X-Example-access-token')
        self.refresh_token = response.headers.get('X-Example-refresh-token')
        self.headers = {'Content-Type': 'application/json',
                        'X-Example-access-token': self.token}
        return response

    def disconnect(self) -> requests.Response:
        """
        Logout and disconnect.

        :return: requests.Response
        """
        return requests.post(f'{self.base_url}/revoketoken')

    def get_lets_get_all_routers(self, *args, url: [str, None] = None, data: dict = None,
                                 auth: HTTPBasicAuth = None, placeholder='x',
                                 split_method: [str, None] = None,
                                 **kwargs) -> requests.Response:
        """
        This is just an example of how to use dynamic methods.

        :param args: Arguments to pass to the method
        :param url: The URL of the resource you are trying to access. Defaults to base_url + method
        :param data: The data to change or update as a Python dictionary. Defaults to None
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None
        :param placeholder: The placeholder in the class method, default to x. Example get_method1_x
        :param split_method: Split the method name to build the URL. Defaults to '_' underscore
        :param kwargs: keyword arguments to pass to the method
        :return: The requests.Response
        """
        return self.dynamic_method_boilerplate(*args, url, data, auth,
                                               placeholder, split_method, **kwargs)

    def get_routers(self, *args, url: [str, None] = None, data: dict = None,
                    auth: HTTPBasicAuth = None, placeholder='x',  split_method: [str, None] = '_',
                    **kwargs) -> requests.Response:
        """
        This is just an example of how to use dynamic methods.

        :param args: Arguments to pass to the method
        :param url: The URL of the resource you are trying to access. Defaults to base_url + method
        :param data: The data to change or update as a Python dictionary. Defaults to None
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None
        :param placeholder: The placeholder in the class method, default to x. Example get_method1_x
        :param split_method: Split the method name to build the URL. Defaults to '_' underscore
        :param kwargs: keyword arguments to pass to the method
        :return: The requests.Response
        """
        return self.dynamic_method_boilerplate(*args, url, data, auth,
                                               placeholder, split_method, **kwargs)

    def get_routers_x(self, *args, url: [str, None] = None, data: dict = None,
                      auth: HTTPBasicAuth = None, placeholder='x',
                      split_method: [str, None] = '_',
                      **kwargs) -> requests.Response:
        """
        This is just an example of how to use dynamic methods.

        :param args: Arguments to pass to the method
        :param url: The URL of the resource you are trying to access. Defaults to base_url + method
        :param data: The data to change or update as a Python dictionary. Defaults to None
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None
        :param placeholder: The placeholder in the class method, default to x. Example get_method1_x
        :param split_method: Split the method name to build the URL. Defaults to '_' underscore
        :param kwargs: keyword arguments to pass to the method
        :return: The requests.Response
        """
        return self.dynamic_method_boilerplate(*args, url, data, auth,
                                               placeholder, split_method, **kwargs)

    def post_routers(self, *args, url: [str, None] = None, data: dict = None,
                     auth: HTTPBasicAuth = None, placeholder='x',
                     split_method: [str, None] = '_',
                     **kwargs) -> requests.Response:
        """
        This is just an example of how to use dynamic methods.

        :param args: Arguments to pass to the method
        :param url: The URL of the resource you are trying to access. Defaults to base_url + method
        :param data: The data to change or update as a Python dictionary. Defaults to None
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None
        :param placeholder: The placeholder in the class method, default to x. Example get_method1_x
        :param split_method: Split the method name to build the URL. Defaults to '_' underscore
        :param kwargs: keyword arguments to pass to the method
        :return: The requests.Response
        """
        return self.dynamic_method_boilerplate(*args, url, data, auth,
                                               placeholder, split_method, **kwargs)

    def put_routers_x(self, *args, url: [str, None] = None, data: dict = None,
                      auth: HTTPBasicAuth = None, placeholder='x',
                      split_method: [str, None] = '_',
                      **kwargs) -> requests.Response:
        """
        This is just an example of how to use dynamic methods.

        :param args: Arguments to pass to the method
        :param url: The URL of the resource you are trying to access. Defaults to base_url + method
        :param data: The data to change or update as a Python dictionary. Defaults to None
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None
        :param placeholder: The placeholder in the class method, default to x. Example get_method1_x
        :param split_method: Split the method name to build the URL. Defaults to '_' underscore
        :param kwargs: keyword arguments to pass to the method
        :return: The requests.Response
        """
        return self.dynamic_method_boilerplate(*args, url, data, auth,
                                               placeholder, split_method, **kwargs)

    def delete_routers_x(self, *args, url: [str, None] = None, data: dict = None,
                         auth: HTTPBasicAuth = None, placeholder='x',
                         split_method: [str, None] = '_',
                         **kwargs) -> requests.Response:
        """
        This is just an example of how to use dynamic methods.

        :param args: Arguments to pass to the method
        :param url: The URL of the resource you are trying to access. Defaults to base_url + method
        :param data: The data to change or update as a Python dictionary. Defaults to None
        :param auth: A Requests HTTPBasicAuth with the username and password. Defaults to None
        :param placeholder: The placeholder in the class method, default to x. Example get_method1_x
        :param split_method: Split the method name to build the URL. Defaults to '_' underscore
        :param kwargs: keyword arguments to pass to the method
        :return: The requests.Response
        """
        return self.dynamic_method_boilerplate(*args, url, data, auth,
                                               placeholder, split_method, **kwargs)
