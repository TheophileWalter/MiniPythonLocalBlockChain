import os
import hashlib as hl
from os.path import isfile

"""
Classe TransactionssParent

Ecrire et lire les transactions dans les fichiers Transactions et PendingTransactions
"""

class TransactionsParent:
    
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
            self.path = "nodes/"+node+"/pending-transactions"

    """
    Retourne la liste des transactions
    """
    def listTrans(self):
        return os.listdir(self.path)

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
    def writeTrans(self, src, dest, amount, fees):
        chaine = "from " + src + "\nto " + dest + "\namount " + amount + " units\nfees " + fees + " units"
        nameFile = hl.md5(chaine.encode()).hexdigest()
        filePath = self.path + "/" + nameFile

        ## test si le fichier existe deja
        if not isfile(filePath):
            file = open(filePath, 'w')
            file.write(chaine)
            file.close()
            return nameFile
        else:
            return False


if __name__ == '__main__':
    # transaction
    trans = TransactionsParent(True, "node_1")
    tr1 = trans.writeTrans('3.1234f46975c7de06', '3.8749f46975c7de06', '40000', '10')
    tr2 = trans.writeTrans('3.1234f46975c7de06', '3.8749f46975c7de06', '44000', '40')
    tr3 = trans.writeTrans('3.1234f46975c7de06', '3.8749f46975c7de06', '44000', '40')
    print("tr1 = "+str(tr1)+" : OK")
    print("tr2 = "+str(tr2)+" : OK")
    print("tr2 = "+str(tr3)+" : False")
    print("Trans list = "+str(trans.listTrans()))
    print("Read "+str(tr1)+str(trans.readTrans(tr1)))
    print("Read "+str(tr2)+str(trans.readTrans(tr2)))

    # pending transaction
    trans = TransactionsParent(False, "node_3")
    tr4 = trans.writeTrans('3.6764f46975c7de06', '3.5541f46975c7de06', '100', '1')
    print("tr4 = "+str(tr4)+" : OK")
    print("Trans list = "+str(trans.listTrans()))
    print("Read "+str(tr4)+str(trans.readTrans(tr4)))

