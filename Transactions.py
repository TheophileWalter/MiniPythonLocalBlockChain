""" 
Classe Transaction hérite de la classe TransactionParent

Classe fille correspondant à une transaction
"""

class Transaction(TransactionParent):

    def __init__(self, node):
        TransactionParent.__init__(self, True, node)

        
