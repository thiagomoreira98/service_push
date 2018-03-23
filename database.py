# biblioteca para conexão com o banco
import pyodbc

class Database(object):
    driver = ''
    server = ''
    user = ''
    password = ''
    database = ''

    def __init__(self, config):
        self.driver = config['driver']
        self.server = config['server']
        self.user = config['user']
        self.password = config['password']
        self.database = config['database']

    # montando a string de conexão
    def getConnectionString(self):
        return 'DRIVER='+self.driver+';SERVER='+self.server+';DATABASE='+self.database+';UID='+self.user+';PWD='+self.password

    # executando uma consulta no banco
    def execute(self, query):
        try:
            connection = pyodbc.connect(self.getConnectionString())
            cursor = connection.cursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                print(row.nome)
                print(row.sobrenome)
        except pyodbc.DatabaseError as err:
            print(err.args)
            # cursor.execute("ROLLBACK")
        finally:
            cursor.close()
            del cursor
            connection.close()