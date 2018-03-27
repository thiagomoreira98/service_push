import json

config = {
    "sql": { },
    "api": {
        "host": 'localhost',
        "port": 1234
    }
}

def readJSON():
    f = open('banco.json', 'r')
    config['sql'] = json.loads(f.read())
    f.close()