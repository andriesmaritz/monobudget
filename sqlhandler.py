import sqlite3


class SqlHandler:

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.database = self.connection.cursor()

    def create_transactions_table(self):
        query = "CREATE TABLE transactions (\n" \
                "    transaction_id varchar(255), \n" \
                "    transaction_type varchar(255), \n"\
                "    date_posted varchar(255), \n"\
                "    transaction_amount float, \n"\
                "    name varchar(255), \n"\
                "    memo varchar(255), \n"\
                "PRIMARY KEY transaction_id);"
        print(query)
        self.database.execute(query)
        self.connection.commit()
