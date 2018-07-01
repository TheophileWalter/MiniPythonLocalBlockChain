from PendingTransactions import PendingTransactions
from Accounts import Accounts
from Node import Node
import os

"""
Classe Client

Créer un compte
Ajoute des nouvelles transactions dans pending-transactions
Fait des requêtes
"""

class Client:

    def __init__(self, node, id):
        self.node = node
        self.account = Accounts('', node)
        self.id = id

    """
    Créer un compte
    """
    def createAccount(self, amount):
        self.id = self.account.create_account(amount)

    """
    Ajoute une nouvelle transaction dans pending-transactions
    """
    def addTrans(self, dest, amount, fees):
        trans = PendingTransactions('', self.node)
        tr = trans.writeTrans(self.id, dest, amount, fees)
        return tr

    """
    Verifie sa balance
    """
    def getBalance(self):
        if not self.id:
            return False
        else:
            return self.account.get_account_amount(self.id)

# TESTS
if __name__ == '__main__':
    # Crée un noeud
    n1 = Node('node_1', './node_1', [])
    if not n1.initialized:
        n1.create()

    # nouveau client c1
    c1 = Client('node_1', "")
    c1.createAccount(4000)
    print("Balance c1: " + str(c1.getBalance()))
    print("Accounts list: " + str(c1.account._get_accounts_list()))
        
    # nouveau client c2
    c2 = Client('node_1', "")
    print("Balance c2: " + str(c2.getBalance()))
    c2.createAccount(3000)
    print("Balance c2: " + str(c2.getBalance()))
    print("Accounts list: " + str(c2.account._get_accounts_list()))

    # nouvelle transaction de c1 à c2
    tr1 = c1.addTrans(c2.id, '500', '3')
    print("Transaction id: " + str(tr1))
    print ("Transactions pending list: " + str(os.listdir('nodes/node_1/pending-transactions')))

    # check balance client existant
    c3 = Client('node_1', c1.id)
    print("Balance c2: " + str(c3.getBalance()))
    print("Accounts list: " + str(c3.account._get_accounts_list()))


        
        