# coding=utf-8

import os
from random import randint
from Accounts import Accounts
from Blocks import Blocks
from PendingTransactions import PendingTransactions
from Transactions import Transactions

# Représente un noeud
class Node:

    # Instancie les attributs du noeud
    def __get_attributes__(self):
        self.accounts = Accounts(self.name)
        self.blocks = Blocks(self.name)
        self.pendingTransactions = PendingTransactions(self.name)
        self.transactions = Transactions(self.name)

    # Constructeur de la classe
    #
    # Prend le nom du noeud en paramètres, si il n'existe pas, l'attribut 'initialized' est mis à False
    # Il faut dans ce cas appeller la méthode 'create'
    def __init__(self, nodeName):
        self.name = nodeName
        self.path = 'nodes/' + nodeName + '/'
        self.name = nodeName
        self.thread_miningBlock = False
        self.thread_checkBlock = False
        # Vérifie si le répertoire n'existe pas
        if not os.path.isdir(self.path):
            self.initialized = False
        else:
            # On instancie toutes les classes
            Node.__get_attributes__(self)
            self.initialized = True

    # Crée le noeud courant
    def create(self):
        # Création des dossiers
        os.mkdir(self.path)
        os.mkdir(self.path + 'accounts')
        os.mkdir(self.path + 'blocks')
        os.mkdir(self.path + 'pending-transactions')
        os.mkdir(self.path + 'transactions')
        # Chargement des classes
        Node.__get_attributes__(self)
        self.initialized = True

    # Copie les données d'un noeud vers celui actuel
    def cropyFrom(self, nodeName):
        # Chargement du noeud distant
        distant = Node(nodeName)
        # Vérifie si le noeud distant existe
        if not distant.initialized or not self.initialized:
            return False
        # Copie les informations
        for id in distant.accounts._get_accounts_list():
            self.accounts.modify_account(id, distant.accounts.get_account_amount(id))
        for id in distant.blocks.getList():
            infos = distant.blocks.getBlock(id)
            self.blocks.writeBlock(infos['previous'], infos['miner'], infos['pow'], infos['date'], infos['nonce'], ' '.join(infos['transactions']))
        for id in distant.pendingTransactions.listTrans():
            infos = distant.pendingTransactions.readTrans(id)
            self.pendingTransactions.writeTrans(infos['from'], infos['to'], infos['amount'], infos['fees'])
        for id in distant.transactions.listTrans():
            infos = distant.transactions.readTrans(id)
            self.transactions.writeTrans(infos['from'], infos['to'], infos['amount'], infos['fees'])

    # Get new hash with md5
    def _get_new_hash(self, previous, pow, date, transactions):
        intToHash = random.randint(0, 2**128-1)

        block =  'previous ' + previous + '\n'
        block += 'miner ' + self.name + '\n'
        block += 'pow' + pow + '\n'
        block += 'date ' + date + '\n'
        block += 'nonce ' + str(intToHash) + '\n'
        block += 'transactions ' + transactions + '\n'

        hashHexa = hashlib.md5(block.encode()).hexdigest()
        hashInt = int(hashHexa, 16)
        hashBin = bin(hashInt)
        return hashBin[3:]

    # Get higher block
    def getHigherBlock(self):
        blocksList = self.blocks.getList()
         # if there is blocks
        if len(blocksList) != 0:
            return = max(blocksList)
        else:
            return False

    # Thread mining blocks
    def miningBlock(self):
        if Node.getHigherBlock(self):
            nbOfZeros = 20
            stringOfZeros = "0" * int(nbOfZeros)
            stringHash = Node._get_new_hash()
            # while stringHash not found
            while not stringHash.startswith(stringOfZeros):
                stringHash = Node._get_new_hash()
            
            # TODO CREATE NEW BLOCK
            
            return True
        else:
            return False
    
        # Thread check blocks
    def checkBlock(self):
        blocksList = self.blocks.getList()
        lastBlockFile = max(blocksList)
        result = False
        # for each node
        for node in os.listdir('./nodes/'):
            # On cherche tous les blocs plus grands que celui actuel
            foreignNode = Blocks(node)
            for block in foreignNode.getList():
                if block > lastBlockFile:
                # On récupère le bloc et on indique qu'il ne faut plus miner
                result = True
                infos = foreignNode.getBlock(block)
                self.blocks.writeBlock(infos['previous'], infos['miner'], infos['pow'], infos['date'], infos['nonce'], infos['transactions'])
        return result



    # Launch threads
    def launchThreads(self):
        while True:
            if Node.checkBlock(self):
                break
            if Node.miningBlock(self):
                break
            




if __name__ == '__main__':
    node = Node('node_1')
    assert node.initialized
    node2 = Node('node_' + str(randint(0, 2**32-1)))
    assert not node2.initialized
    node2.create()
    assert node2.initialized
    node2.cropyFrom('node_1')