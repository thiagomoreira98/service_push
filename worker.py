# arquivo com as configurações do worker
from config.settings import *

# classe para configurar o banco
from classes.database import Database

# classe para configurar o request
from classes.request import Request

# conectando com o banco
db = Database(config['sql'])
results = db.execute('SELECT * FROM seguranca.usuario;')
print(results)

req = Request({
    "host": config['api']['host'],
    "port": config['api']['port'],
    "method": 'GET',
    "route": '/pin',
    "headers": { "token": 'xxx', "Content-Type": 'application/json' },
    "body": {}
})

response = req.request()
print(response)

# body = json.dumps(obj)
# print(obj)
# print(f'body', body)
# headers = {"Content-type": "application/json"}
# h2 = HTTPConnection('localhost', 7002)
# h2.request('POST', '/ping', body, headers)
# response2 = h2.getresponse()
# data = response2.read()