# coding=utf-8

import os
import sys
import hashlib
from random import randint
from Accounts import Accounts
from Blocks import Blocks
from PendingTransactions import PendingTransactions
from Transactions import Transactions
from Date import Date
import binascii

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
        self.POW = 16 # Difficulté
        self.name = nodeName
        self.path = 'nodes/' + nodeName + '/'
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

    # Transforme une chaîne hexadécimale en chaîne binaire
    # Source : https://walter.click/Kok9yQ
    def _binary(x):
        return " ".join(reversed( [i+j for i,j in zip( *[ ["{0:04b}".format(int(c,16)) for c in reversed("0"+x)][n::2] for n in [1,0] ] ) ] ))

    # Get new hash with md5
    def _get_new_hash(self, previous, pow, date, transactions):
        intToHash = randint(0, 2**128-1)

        block =  'previous ' + previous + '\n'
        block += 'miner ' + self.name + '\n'
        block += 'pow ' + str(pow) + '\n'
        block += 'date ' + date + '\n'
        block += 'nonce ' + str(intToHash) + '\n'
        block += 'transactions ' + transactions

        hashHexa = hashlib.md5(block.encode()).hexdigest()
        hashBin = Node._binary(hashHexa)
        return [block, hashBin.replace(' ', ''), hashHexa]

    # Get higher block
    def getHigherBlock(self):
        blocksList = self.blocks.getList()
         # if there is blocks
        if len(blocksList) != 0:
            id_max = max(map(lambda e: int(e.split('.')[0]), blocksList))
            for e in blocksList:
                if e.startswith(str(id_max) + '.'):
                    return e
            return False
        else:
            return False

    # Essaye de miner le bloc
    def miningBlock(self):
        higher = Node.getHigherBlock(self)
        if higher != False:
            stringOfZeros = "0" * int(self.POW)
            d = Date()
            transactions = self.pendingTransactions.listValidTrans(self.accounts)
            block = Node._get_new_hash(self, higher, self.POW, d.get_date(), ' '.join(transactions))
            # while stringHash not found
            if block[1].startswith(stringOfZeros):
                # On valide les transactions
                for t in transactions:
                    # Copié la transaction depuis celles en attente vers celles valides
                    current = self.pendingTransactions.readTrans(t)
                    self.pendingTransactions.transDelete(t)
                    self.transactions.writeTrans(current['from'], current['to'], current['amount'], current['fees'])
                    # Met à jour les comptes
                    self.accounts.modify_account(current['from'], self.accounts.get_account_amount(current['from']) - float(current['amount']) - float(current['fees']))
                    self.accounts.modify_account(current['to'], self.accounts.get_account_amount(current['to']) + float(current['amount']))
                # On crée le bloc
                self.blocks.writeBlockFromString(block[0], block[2])
                # On affiche un message
                print('\nNew block mined with hash ' + block[2] + '\n' + block[0] + '\n')
                return True
        return False
    
    # Vérifie si le bloc a été miné par un autre noeud
    def checkBlock(self):
        blocksList = self.blocks.getList()
        lastBlockFile = max(map(lambda e: int(e.split('.')[0]), blocksList))
        result = False
        # for each node
        for node in os.listdir('./nodes/'):
            # On s'assure qu'on essaye pas de copier nos propres blocs
            if node != self.name:
                # On cherche tous les blocs plus grands que celui actuel
                foreignBlocks = Blocks(node)
                foreignTransactions = Transactions(node)
                foreignAccounts = Accounts(node)
                blocksListF = foreignBlocks.getList()
                blocksListF.sort()
                for block in blocksListF:
                    if int(block.split('.')[0]) > lastBlockFile:
                        # On récupère le bloc et on indique qu'il ne faut plus miner
                        result = True
                        infos = foreignBlocks.getBlock(block)
                        # Vérifie que les informations ont bien été lues
                        # Sinon essaye de les relire
                        while not infos:
                            infos = foreignBlocks.getBlock(block)
                        self.blocks.writeBlock(infos['previous'], infos['miner'], infos['pow'], infos['date'], infos['nonce'], infos['transactions'])
                        # On récupère les transactions de ce bloc et met à jour les comptes
                        for t in infos['transactions']:
                            trans = foreignTransactions.readTrans(t)
                            self.transactions.writeTrans(trans['from'], trans['to'], trans['amount'], trans['fees'])
                            self.accounts.modify_account(trans['from'], foreignAccounts.get_account_amount(trans['from']))
                            self.accounts.modify_account(trans['to'], foreignAccounts.get_account_amount(trans['to']))
                        # Affiche un message
                        print('New block get from foreign node with ID ' + block)
                # Si le bloc a été miné, on quitte sans vérifier les autres noeuds
                if result:
                    return True
        return False

    # Launch threads
    def mine(self):
        while True:
            if Node.checkBlock(self):
                break
            if Node.miningBlock(self):
                break

if __name__ == '__main__':
    # On créer un noeud
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = 'node_' + str(randint(0, 2**32-1))
    node = Node(name)
    if not node.initialized:
        node.create()
    # Crée le bloc de départ
    node.blocks.createFirstBlock()
    # Tente de miner le block suivant
    while True:
        node.mine()