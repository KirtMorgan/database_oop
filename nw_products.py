import pyodbc
class Nwproducts:
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password  = 'Passw0rd2018'
        self.docker_db_instance = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL SERVER};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+self.password)
        self.cursor = self.docker_db_instance.cursor()

    def sql_query_no_transaction(self, sql_query):
        return self.cursor.execute(sql_query)

    def print_all_product_records(self):
        query_records = self.sql_query_no_transaction("SELECT * FROM Products")
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)
