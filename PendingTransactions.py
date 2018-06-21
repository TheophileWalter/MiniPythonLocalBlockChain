""" 
Classe PendingTransactions hérite de la classe TransactionParent

Classe fille correspondant à une transaction en attente d'entrée dans un bloc
"""

class PendingTransactions(TransactionsParent):

    def __init__(self, node):
        TransactionsParent.__init__(self, False, node)

"""
Supprime une transaction (une fois qu'elle entre dans un bloc)
"""

        
