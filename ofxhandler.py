import xml.etree.ElementTree as ElementTree
import json


class OfxHandler:

    def __init__(self, filename):
        with open(filename) as f:
            config = json.load(f)
        self.xml = ElementTree.parse(config["filename"])
        self.root = self.xml.getroot()

    def get_transactions(self):
        """
        Provide a list of all transactions in the OFX file. Minimal processing of the data
        is performed at this level; the data is just structured into a dictionary.
        :return: A dictionary containing a list of transactions with their properties
        """
        transactions = []
        for entry in self.root.iter('STMTTRN'):
            transaction = {
                "transaction_type": entry.find("TRNTYPE").text,
                "date_posted": entry.find("DTPOSTED").text,
                "transaction_amount": float(entry.find("TRNAMT").text),
                "transaction_id": entry.find("FITID").text,
                "name": entry.find("NAME").text,
                "memo": entry.find("MEMO").text
            }
            transactions.append(transaction)
        return transactions
