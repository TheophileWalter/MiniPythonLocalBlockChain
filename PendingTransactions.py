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

    
    """
    Retourne la liste des transactions valides
    Peut prendre un objet Account en paramètres, si il n'est pas donné alors un objet sera créé dans le noeud actuel
    """
    def listValidTrans(self, accounts = False):
        if not accounts:
            accounts = Accounts(self.name)
        trans = PendingTransactions.listTrans(self)
        valid = []
        for t in trans:
            infos = PendingTransactions.readTrans(self, t)
            amountFrom = accounts.get_account_amount(infos['from'])
            amountTo = accounts.get_account_amount(infos['to'])
            # Vérifie la transaction
            if amountFrom >= (float(infos['amount']) + float(infos['fees'])) and amountTo != -1:
                valid.append(t)
        return valid


if __name__ == '__main__':
    trans = PendingTransactions('node_1')
    print("Trans list = "+str(trans.listTrans()))
    tr1 = trans.writeTrans('3.6764f46975c7de06', '3.5541f46975c7de06', '100', '1')
    print("tr1 = "+str(tr1)+" : OK")
    print("Trans list = "+str(trans.listTrans()))
    trans.transDelete(tr1)
    print("Trans list = "+str(trans.listTrans()))


        
