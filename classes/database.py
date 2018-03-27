# biblioteca para conexão com o banco
import pyodbc

# helper para gerar log de erro
from src.helpers import log

class Database(object):
    driver = ''
    server = ''
    user = ''
    password = ''
    database = ''
    rows = []

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
            queryResult = cursor.fetchall()
            self.setRows(queryResult)
            return self.getRows()
        except pyodbc.DatabaseError as ex:
            log.generateLog(str(ex))
            raise ex
        else:
            cursor.close()
            del cursor
            connection.close()

    def setRows(self, queryResult):
        self.rows = list(queryResult)

    def getRows(self):
        return self.rows