import ofxhandler
import sqlhandler
import unittest
from datetime import *


class TestOfxHandler(unittest.TestCase):

    def setUp(self):
        self.ofx = ofxhandler.OfxHandler("../bin/config.json")

    def test_file_parsed(self):
        self.assertIsNotNone(self.ofx.xml)

    def test_get_transactions(self):
        transactions = self.ofx.get_transactions()
        for transaction in transactions:
            if transaction["transaction_id"] == "4561239876201808021":
                self.assertEqual(transaction["transaction_type"], "DEBIT")
                self.assertEqual(transaction["transaction_amount"], -1599.00)
                self.assertEqual(transaction["name"], "POS PURCHASE (EFFEC 30072018) WO")
                self.assertEqual(transaction["memo"], "POS PURCHASE (EFFEC 30072018) WORLD FOCUS CAPE CARD NO. 4321")

    def test_get_account_id(self):
        account_id = self.ofx.get_account_id()
        self.assertEqual(account_id, "4561239876")

    def test_file_timestamp(self):
        timestamp = self.ofx.get_file_timestamp()
        reference = datetime(2018, 8, 25, 13, 28, 39)
        self.assertEqual(timestamp, reference)


class TestSqlHandler(unittest.TestCase):

    def setUp(self):
        self.sql = sqlhandler.SqlHandler("../bin/config.json")

    def test_create_transactions_table(self):
        self.sql.create_transactions_table()


if __name__ == '__main__':
    unittest.main()
