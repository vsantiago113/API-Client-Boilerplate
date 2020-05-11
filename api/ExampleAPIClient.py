from api import APIPlugin


class Client(APIPlugin):
    headers = None
    base_url = None

    def connect(self, url: str = '', username: str = '', password: str = ''):
        pass

    def disconnect(self):
        pass
