import xml.etree.ElementTree as ElementTree
import json
from datetime import *
import re


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

    def get_account_id(self):
        """
        The account ID associated with the OFX file.
        :return: An account ID (free text)
        """
        return self.root.findall("./BANKMSGSRSV1/STMTTRNRS/STMTRS/BANKACCTFROM/ACCTID")[0].text

    def get_file_timestamp(self):
        """
        Checks when the OFX file was generated and returns it in a Python datetime format
        :return: A date with yyyy/mm/dd hh/mm/ss information
        """
        time_string = self.root.findall("./SIGNONMSGSRSV1/SONRS/DTSERVER")[0].text
        result = re.match(r"^(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})(\d{2})", time_string)
        return datetime(int(result.group(1)),
                        int(result.group(2)),
                        int(result.group(3)),
                        int(result.group(4)),
                        int(result.group(5)),
                        int(result.group(6))
                        )
