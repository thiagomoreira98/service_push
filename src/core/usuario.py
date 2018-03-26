# arquivo com as configurações do worker (config)
from config.settings import *

# classe para configurar o request
from classes.request import Request

# classe para configurar o banco
from classes.database import Database

import datetime

def selecionar():
    db = Database(config['sql'])
    rows = db.execute('SELECT * FROM seguranca.usuario;')
    print(rows)
    
    for row in rows:
        row.dataCadastro = None
        print(row.dataCadastro)

    return rows

def push():
    usuarios = selecionar()
    print(usuarios)

    options = {
        "host": config['api']['host'],
        "port": config['api']['port'],
        "method": 'POST',
        "route": '/ping',
        "headers": { "token": 'xxx', "Content-Type": 'application/json' },
        "body": {}# usuarios
    }

    req = Request(options)
    req.request()