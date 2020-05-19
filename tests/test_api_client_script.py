from ExampleAPIClient import Client
import unittest

device_id = None


class TestExampleAPIClient(unittest.TestCase):

    def test_authentication(self):
        client = Client()
        response = client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        self.assertTrue(response.status_code, 200)
        self.assertIsInstance(client.token, str)
        self.assertIsInstance(client.refresh_token, str)

    def test_on_get_static_and_dynamic_methods(self):
        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req1 = client.get(method='lets_get_all_routers', PageSize=2, Offset=0)
        req2 = client.get_lets_get_all_routers(PageSize=2, Offset=0)

        self.assertDictEqual(req1.json(), req2.json())

    def test_on_get_dynamic_methods(self):
        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req1 = client.get(method='routers', PageSize=2, Offset=0)
        req2 = client.get_routers(PageSize=2, Offset=0)

        self.assertDictEqual(req1.json(), req2.json())

    def test_getting_object(self):
        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req = client.get(method='routers/12345')

        self.assertEqual(req.status_code, 200)

    def test_creating_object(self):
        global device_id

        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req = client.post(method='routers', data={'name': 'RT99', 'ip': '192.168.1.199'})

        device_id = req.json().get('id')

        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json().get('name'), 'RT99')
        self.assertEqual(req.json().get('ip'), '192.168.1.199')

    def test_updating_object(self):
        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req = client.put(method='routers/123456', data={'name': 'RT300', 'ip': '192.168.1.225'})

        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json().get('id'), '123456')
        self.assertEqual(req.json().get('name'), 'RT300')
        self.assertEqual(req.json().get('ip'), '192.168.1.225')

    def test_deleting_object(self):
        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req = client.delete(method=f'routers/{device_id}')

        self.assertEqual(req.status_code, 200)

        req = client.get(method=f'routers/{device_id}')

        self.assertEqual(req.status_code, 404)

    def test_getting_object_dynamic_method(self):
        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req = client.get_routers_x('12345')

        self.assertEqual(req.status_code, 200)

    def test_creating_object_dynamic_method(self):
        global device_id

        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req = client.post_routers(data={'name': 'RT99', 'ip': '192.168.1.199'})

        device_id = req.json().get('id')

        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json().get('name'), 'RT99')
        self.assertEqual(req.json().get('ip'), '192.168.1.199')

    def test_updating_object_dynamic_method(self):
        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req = client.put_routers_x('123456', data={'name': 'RT400', 'ip': '192.168.1.240'})

        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json().get('id'), '123456')
        self.assertEqual(req.json().get('name'), 'RT400')
        self.assertEqual(req.json().get('ip'), '192.168.1.240')

    def test_deleting_object_dynamic_method(self):
        client = Client()
        client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

        req = client.delete_routers_x(device_id)

        self.assertEqual(req.status_code, 200)

        req = client.get_routers_x(device_id)

        self.assertEqual(req.status_code, 404)


if __name__ == '__main__':
    unittest.main()
