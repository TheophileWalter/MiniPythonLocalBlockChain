import os
import hashlib as hl

"""
Classe TransactionParent

Ecrire et lire les transactions dans les fichiers Transactions et PendingTransactions
"""

class TransactionParent:
    
    """ 
    Initialise le chemin jusqu'au dossier correspondant au type de transaction

    b: booleen correspondant au type de transaction
            True = Transactions
            False = PendingTransactions
    node: le noeud dans lequel est/sera placée la transaction 
    """
    def __init__(self, b, node):

        if b == True:
            self.path = "/nodes/"+node+"/transactions"
        else:
            self.path = "/nodes/"+node+"/pendingTransactions"

    """
    Retourne la liste des transactions
    """
    def listTrans(path):
        return os.listdir(path)

    """
    Retourne une transaction sous forme de dictionnaire
    """
    def readTrans(trans):
        d = {}
        with open(trans, 'r') as t:
            content = t.readlines()

            # remove whitespaces and \n
            content = [x.strip() for x in content]

            for line in content:
                word = line.split(" ")

                if word in ["from", "to", "amount", "fees"]:
                    d[word[0]] = word[1]
                else:
                    return False

        return d
