import os
import hashlib as hl
from os.path import isfile

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

    """hashCreated = _get_new_hash(self)
        fileName = self.nodePath+"/"+hashCreated
        accountFileToModify = open(fileName, 'w')
        accountFileToModify.write(str(amount))
        accountFileToModify.close()
        return hashCreated"""
    """
    Ecrit une nouvelle transaction dans un fichier
    """
    def writeTrans(self, src, dest, amount, fees):
        chaine = "from " + src + "\nto " + dest + "\namount " + amount + " units\nfees " + fees + " units"
        nameFile = hl.md5(chaine.encode()).hexdigest()
        filePath = self.path + "/" + nameFile

        ## test si le fichier existe deja
        if isfile(filePath):
            file = open(filePath, 'w')
            file.write(chaine)
            file.close()
        else:
            return False

        return


if __name__ == '__main__':
    # transaction
    trans = TransactionParent(True, "node_1")
    trans.writeTrans('3.1234f46975c7de06', '3.8749f46975c7de06', '40000', '10')
    trans.writeTrans('3.1234f46975c7de06', '3.8749f46975c7de06', '44000', '40')
    print(trans.listTrans())
    print(trans.readTrans('f16d7429acd70873e9377290333f3334'))

    # pending transaction
    trans = TransactionParent(False, "node_3")
    trans.writeTrans('3.6764f46975c7de06', '3.5541f46975c7de06', '100', '1')
    print(trans.listTrans())
    print(trans.readTrans('c997d20e015a6d378c7266d5cc504fa8'))

