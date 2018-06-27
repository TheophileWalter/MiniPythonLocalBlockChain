# coding=utf-8

import os
import sys
import hashlib
from random import randint
from Date import Date
import binascii

# Représente un noeud
class NodeMemory:

    # Constructeur de la classe
    def __init__(self, nodeName):
        self.POW = 16 # Difficulté
        self.name = nodeName

    # Transforme une chaîne hexadécimale en chaîne binaire
    # Source : https://walter.click/Kok9yQ
    def _binary(self, x):
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
        hashBin = NodeMemory._binary(self, hashHexa)
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
    def miningBlock(self, higher):
        stringOfZeros = "0" * int(self.POW)
        d = Date()
        block = NodeMemory._get_new_hash(self, higher, self.POW, d.get_date(), '')
        # while stringHash not found
        if block[1].startswith(stringOfZeros):
            # On affiche un message
            print('New block mined with hash ' + block[2] + '\n' + block[0] + '\n')
            # Retourne l'ID du bloc miné
            return block[2]
        return False

    # Launch threads
    def mine(self, last):
        while True:
            res = NodeMemory.miningBlock(self, last)
            if res != False:
                return res

if __name__ == '__main__':
    # On créer un noeud
    if len(sys.argv) >= 2:
        name = sys.argv[1]
    else:
        name = 'node_' + str(randint(0, 2**32-1))
    node = NodeMemory(name)
    # Tente de miner le block suivant
    last = 'first'
    while True:
        last = node.mine(last)