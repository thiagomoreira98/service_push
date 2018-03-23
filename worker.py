from http.client import HTTPConnection
from urllib.parse import urlencode
from sqlalchemy import create_engine
import json

host = 'localhost'
port = 7002

# h1 = HTTPConnection('localhost', 7002)
# h1.request('GET', '/ping')
# response = h1.getresponse()
# data = response.read()
# print(response.status, ' ', response.reason)
# print(data)
# print(data[0]["message"], ' ', data["data"])

create_engine("mssql+pymssql://user:pass@host/db", deprecate_large_types=True)

obj = {
    "nome": "thiago",
    "idade": 20,
    "peso": 60
}

objs = [
    obj,
    obj,
    obj
]

body = json.dumps(objs)
# print(objs)
print(f'body', body)
headers = {"Content-type": "application/json"}
h2 = HTTPConnection('localhost', 7002)
h2.request('POST', '/ping', body, headers)
response2 = h2.getresponse()
data = response2.read()