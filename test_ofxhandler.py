import ofxhandler
import unittest
import datetime


class TestOfxHandler(unittest.TestCase):

    def setUp(self):
        self.ofx = ofxhandler.OfxHandler("config.json")

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


if __name__ == '__main__':
    unittest.main()
