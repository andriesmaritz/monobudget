import xml.etree.ElementTree as ElementTree
import json


class OfxHandler:

    def __init__(self, filename):
        with open(filename) as f:
            config = json.load(f)
        self.xml = ElementTree.parse(config["filename"])
        self.root = self.xml.getroot()

    def get_transactions(self):
        transactions = []
        for entry in self.root.iter('STMTTRN'):
            transaction_amount = float(entry.find("TRNAMT").text)
            transaction = {
                "transaction_type": entry.find("TRNTYPE").text,
                "date_posted": entry.find("DTPOSTED").text,
                "transaction_amount": transaction_amount,
                "transaction_id": entry.find("FITID").text,
                "name": entry.find("NAME").text,
                "memo": entry.find("MEMO").text
            }
            transactions.append(transaction)
        return transactions
