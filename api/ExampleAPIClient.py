from api import APIPlugin


class Client(APIPlugin):
    headers = None
    base_url = None

    def connect(self):
        pass

    def disconnect(self):
        pass
