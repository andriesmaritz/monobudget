import sqlite3


class SqlHandler:

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.database = self.connection.cursor()

    def create_transactions_table(self):
        query = '''CREATE TABLE transactions (
          transaction_id varchar(255),
          transaction_type varchar(255),
          date_posted varchar(255),
          transaction_amount float,
          name varchar(255),
          memo varchar(255),
          PRIMARY KEY transaction_id
        )'''
        print(query)
        self.database.execute(query)
        self.connection.commit()
