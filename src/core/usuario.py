# arquivo com as configurações do worker (config)
from config.settings import *

# classe para configurar o request
from classes.request import Request

# classe para configurar o banco
from classes.database import Database

import datetime

import json

def selecionar():
    db = Database(config['sql'])
    rows = db.execute('SELECT * FROM seguranca.usuario;')
    
    lista = []
    for row in rows:
        obj = {}
        obj['id'] = row.id
        obj['nome'] = row.nome
        lista.append(obj)
        # row.dataCadastro = None

    return lista

def push():
    usuarios = selecionar()

    options = {
        "host": config['api']['host'],
        "port": config['api']['port'],
        "method": 'POST',
        "route": '/ping',
        "headers": { "token": 'xxx', "Content-Type": 'application/json' },
        "body": json.dumps(usuarios)
    }

    req = Request(options)
    response = req.request()
    print(response['status'])
    print(response['content'])