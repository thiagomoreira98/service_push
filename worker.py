# classe para configurar o banco
from database import Database

# classe para configurar o request
from request import Request

# config do banco
sql = {
    "driver": '{ODBC Driver 13 for SQL Server}',
    "server": 'localhos',
    "database": 'VethosPen',
    "user": 'sa',
    "password": 'vethos@1tecnologia'
}

# conectando com o banco
db = Database(sql)
results = db.execute('SELECT * FROM seguranca.usuario;')
# print(results)

req = Request({
    "host": "localhost",
    "port": 1234,
    "method": 'GET',
    "route": '/ping'
})

response = req.request()
print(response)

# h1 = HTTPConnection('localhost', 7002)
# h1.request('GET', '/ping')
# response = h1.getresponse()
# data = response.read()
# print(response.status, ' ', response.reason)
# print(data)
# print(data[0]["message"], ' ', data["data"])

# body = json.dumps(obj)
# print(obj)
# print(f'body', body)
# headers = {"Content-type": "application/json"}
# h2 = HTTPConnection('localhost', 7002)
# h2.request('POST', '/ping', body, headers)
# response2 = h2.getresponse()
# data = response2.read()
