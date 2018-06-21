import os
from TransactionsParent import TransactionsParent

""" 
Classe PendingTransactions hérite de la classe TransactionParent

Classe fille correspondant à une transaction en attente d'entrée dans un bloc
"""

class PendingTransactions(TransactionsParent):

    """
    Initialise une transaction en attente
    """
    def __init__(self, node):
        super().__init__(False, node)

    """
    Supprime une transaction (une fois qu'elle entre dans un bloc)
    """
    def transDelete(self,trans):
        os.remove(self.path + '/' + trans)


if __name__ == '__main__':
    trans = PendingTransactions('node_1')
    print("Trans list = "+str(trans.listTrans()))
    tr1 = trans.writeTrans('3.6764f46975c7de06', '3.5541f46975c7de06', '100', '1')
    print("tr1 = "+str(tr1)+" : OK")
    print("Trans list = "+str(trans.listTrans()))
    trans.transDelete(tr1)
    print("Trans list = "+str(trans.listTrans()))


        
