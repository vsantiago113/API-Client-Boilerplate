# API-Client-Boilerplate

This project help you create standardize RESTful API wrappers so you can create a collection of all the API's you use everyday and using them all the same or very similar way.

### How to install
NOTE: this is just an example this module is not published in PyPi
```ignorelang
$ pip install ExampleAPIClient
```

---

## Usage

#### Import and instantiate the class
```python
from ExampleAPIClient import Client

client = Client(verify=False, warnings=False, api_version='v1')
```

#### Connect and Disconnect
```python
from ExampleAPIClient import Client

client = Client(verify=False, warnings=False, api_version='v1')

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

client.disconnect()
```

#### HTTP GET all records
```python
from ExampleAPIClient import Client
import json

client = Client(verify=False, warnings=False, api_version='v1')

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

response = client.get(method='routers', PageSize=10, Offset=0)
if response.status_code in [200, 202, 204]:
    print(json.dumps(response.json(), indent=4))
else:
    print(response.status_code, response.reason)

client.disconnect()
```

#### HTTP GET a single record
```python
from ExampleAPIClient import Client
import json

client = Client(verify=False, warnings=False, api_version='v1')

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

response = client.get(method='routers/123456')
if response.status_code in [200, 202, 204]:
    print(json.dumps(response.json(), indent=4))
else:
    print(response.status_code, response.reason)

client.disconnect()
```

#### HTTP POST
```python
from ExampleAPIClient import Client
import json

client = Client(verify=False, warnings=False, api_version='v1')

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

response = client.post(method='routers', data={'name': 'RT99', 'ip': '192.168.1.199'})
if response.status_code in [200, 202, 204]:
    print(json.dumps(response.json(), indent=4))
else:
    print(response.status_code, response.reason)

client.disconnect()
```

#### HTTP PUT
```python
from ExampleAPIClient import Client
import json

client = Client(verify=False, warnings=False, api_version='v1')

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

response = client.put(method='routers/123456', data={'name': 'RT300', 'ip': '192.168.1.230'})
if response.status_code in [200, 202, 204]:
    print(json.dumps(response.json(), indent=4))
else:
    print(response.status_code, response.reason)

client.disconnect()
```

#### HTTP DELETE
```python
from ExampleAPIClient import Client
import json

client = Client(verify=False, warnings=False, api_version='v1')

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

response = client.delete(method=f'routers/123456')
if response.status_code in [200, 202, 204]:
    print(json.dumps(response.json(), indent=4))
else:
    print(response.status_code, response.reason)

client.disconnect()
```

### How to use Dynamic Methods

#### HTTP GET all records
```python
from ExampleAPIClient import Client
import json

client = Client(verify=False, warnings=False, api_version='v1')

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

response = client.get_routers(PageSize=10, Offset=0)
if response.status_code in [200, 202, 204]:
    print(json.dumps(response.json(), indent=4))
else:
    print(response.status_code, response.reason)

client.disconnect()
```

#### HTTP GET a single record
```python
from ExampleAPIClient import Client
import json

client = Client(verify=False, warnings=False, api_version='v1')

client.connect(url='http://127.0.0.1:5000', username='admin', password='Admin123')

response = client.get_routers_x('123456', placeholder='x', split_method='_')
if response.status_code in [200, 202, 204]:
    print(json.dumps(response.json(), indent=4))
else:
    print(response.status_code, response.reason)

client.disconnect()
```
