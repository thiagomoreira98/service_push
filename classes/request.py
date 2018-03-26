# biblioteca para usar o HTTP
from http.client import HTTPConnection


class Request(object):
    host = ''
    port = ''
    method = ''
    route = ''

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
            return {
                "status": response.status,
                "content": response.read()
            }
        except Exception as ex:
            print(f'ex-request:', ex)
        finally:
            http.close()