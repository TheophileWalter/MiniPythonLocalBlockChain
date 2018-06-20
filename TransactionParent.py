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
            self.path = "nodes/"+node+"/transactions"
        else:
            self.path = "nodes/"+node+"/pendingTransactions"

    """
    Retourne la liste des transactions
    """
    def listTrans(self, path):
        return os.listdir(path)

    """
    Retourne une transaction sous forme de dictionnaire
    """
    def readTrans(self, trans):
        d = {}
        path = self.path + "/" + trans
        with open(path, 'r') as t:
            content = t.readlines()

            # remove whitespaces and \n
            content = [x.strip() for x in content]

            for line in content:
                word = line.split(" ")

                if word[0] in ['from', 'to', 'amount', 'fees']:
                    d[word[0]] = word[1]
                else:
                    return False

        return d

    """
    Ecrit une nouvelle transaction dans un fichier
    """
    def writeTrans(self, path):
        return


if __name__ == '__main__':
    trans = TransactionParent(False, "nodes_1")
    print(trans.listTrans(trans.path))
    print(trans.readTrans('1.edb53223550477e2'))
