# coding=utf-8

import os
from random import randint
from Accounts import Accounts
from Blocks import Blocks
from PendingTransactions import PendingTransactions
from Transactions import Transactions
import threading

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
    def _get_new_hash(self):
        intToHash = random.randint(0, 2**128-1)
        hashHexa = hashlib.md5(str(intToHash).encode()).hexdigest()
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
        # if thread not already launched
        if not self.thread_miningBlock:
            if not Node.getHigherBlock(self):
                return False
            else:
                nbOfZeros = 20
                stringOfZeros = "0" * int(nbOfZeros)
                stringHash = Node._get_new_hash()
                # while stringHash not found
                while not stringHash.startswith(stringOfZeros):
                    stringHash = Node._get_new_hash()
                
                # TODO CREATE NEW BLOCK
                
                print(True)
                self.thread_checkBlock._stop()
                self.thread_miningBlock._stop()
        else:
            print(False)
    
        # Thread check blocks
    def checkBlock(self):
        # if thread not already launched
        if not self.thread_checkBlock:
            blocksList = [files for roots, dirs, files in os.walk(self.path+"/blocks/")]
            # if there is blocks
            if len(blocksList) != 0:
                lastBlockFile = max(blocksList)
                # while no new block file
                whileCdt = True
                while whileCdt:
                    nodesList = os.listdir("./nodes/")
                    # for each node
                    for i in nodesList:
                        blocksList = [files for roots, dirs, files in os.walk("./nodes/"+i+"/blocks/")]
                        whileCdt = lastBlockFile > max(blocksList)
                
                # TODO GET NEW BLOCK ON RIGHT NODE
                
                print(True)
                self.thread_miningBlock._stop()
                self.thread_checkBlock._stop()
            else:
                print(False)
        else:
            print(False)

    # Launch threads
    def launchThreads(self):
        self.thread_miningBlock = threading.Thread(target=miningBlock, args=(self,))
        self.thread_checkBlock = threading.Thread(target=checkBlock, args=(self,))
        
        self.thread_miningBlock.start()
        self.thread_checkBlock.start()

        whileCft = True
        while whileCdt:
            if 




if __name__ == '__main__':
    node = Node('node_1')
    assert node.initialized
    node2 = Node('node_' + str(randint(0, 2**32-1)))
    assert not node2.initialized
    node2.create()
    assert node2.initialized
    node2.cropyFrom('node_1')