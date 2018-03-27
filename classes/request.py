  # biblioteca para usar o HTTP
from http.client import HTTPConnection

# helper para gerar log de erro
from src.helpers import log

import json

class Request(object):
    host = ''
    port = ''
    method = ''
    route = ''
    response = None

    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
        self.method = config['method']
        self.route = config['route']
        self.headers = config['headers']
        self.body = config['body']

    def request(self):
        try:
            http = HTTPConnection(self.host, self.port)
            http.request(self.method, self.route, self.body, self.headers)
            response = http.getresponse()
            return self.handler(response)
        except Exception as ex:
            log.generate(str(ex))
            print('-------------------------------------------------')
            print('Ocorreram erros durante a execução - Verifique os logs')
        finally:
            http.close()

    def handler(self, response):
        self.response = json.loads(response.read())
        if response.status == 200:
            return self.response

        elif response.status == 404:
            return {
                "status": 404,
                "message": 'A operação solicitada não foi encontrada.'
            }

        elif response.status == 500:
            log.generate(str(self.response['message']))
            return {
                "status": 500,
                "content": self.response['message']
            }