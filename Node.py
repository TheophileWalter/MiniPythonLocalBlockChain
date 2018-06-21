# coding=utf-8

import os
import Accounts
import Blocks
import PendingTransactions
import Transactions

# Représente un noeud
class Node:

    # Constructeur de la classe
    #
    # Prend le nom du noeud en paramètres, le charge si il existe,
    # le crée si il n'existe pas
    def __init__(self, nodeName):
        self.name = nodeName
        self.path = 'nodes/' + nodeName + '/'
        self.name = nodeName
        # Vérifie si le répertoire existe
        if os.path.isdir(self.path):
            # Dans ce cas, on charge toutes les classes
            self.accounts = Accounts(nodeName)
            self.blocks = Blocks(nodeName)
            self.pendingTransactions = PendingTransactions(nodeName)
            self.transactions = Transactions(nodeName)
        else:
            # Sinon on crée les dossiers
            