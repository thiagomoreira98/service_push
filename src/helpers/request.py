# arquivo com as configurações do worker
from config.settings import *

# classe para configurar o request
from classes.request import Request

import json

def request(options):
    req = Request({
        "host": config['api']['host'],
        "port": config['api']['port'],
        "method": options['method'],
        "route": options['route'],
        "headers": options['headers'],
        "body": options['body']
    })

    return req.request()