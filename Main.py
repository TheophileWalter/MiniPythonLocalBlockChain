# coding=utf-8
# Projet de Mini Blockchain

import sys
import os
from Node import Node
from NodeMemory import NodeMemory
from random import randint
import shutil

if __name__ == '__main__':
    # Récupération des paramètres
    working_dir = ''
    genesis = ''
    mono_memory = False
    mono_disk = False
    peers = []
    miner = ''
    params = sys.argv[1:]
    for i in range(len(params)):
        if params[i] == '-working-dir' and len(params) > i+1:
            i += 1
            working_dir = params[i]
        elif params[i] == '-genesis' and len(params) > i+1:
            i += 1
            genesis = params[i]
        elif params[i] == '-mono-memory':
            mono_memory = True
        elif params[i] == '-mono-disk':
            mono_disk = True
        elif params[i] == '-peer' and len(params) > i+1:
            i += 1
            peers.append(params[i])
        elif params[i] == '-miner' and len(params) > i+1:
            i += 1
            miner = params[i]
    
    # Vérification
    if mono_memory and mono_disk:
        print('Error: Can\'t use both "-mono-memory" and "-mono-disk"!')
        exit(1)
    if mono_disk and miner != '':
        print('Error: Can\'t use both "-mono-disk" and "-miner"!')
        exit(1)
    if mono_memory and miner != '':
        print('Error: Can\'t use both "-mono-memory" and "-miner"!')
        exit(1)

    if mono_memory:
        # Lance un noeud en mémoire
        node = NodeMemory('mono-memory')
        # Tente de miner le block suivant
        last = 'first'
        while True:
            last = node.mine(last)
    elif mono_disk:
        # Prépare un dossier pour le dique seul
        os.chdir('./mono/')
        shutil.rmtree('./nodes/', ignore_errors=True)
        os.makedirs('./nodes/')
        # Lance un noeud seul sur le disque
        node = Node('mono-disk', './mono', [])
        if not node.initialized:
            node.create()
        # Crée le bloc de départ
        node.blocks.createFirstBlock()
        # Tente de miner le block suivant
        while True:
            node.mine()
    elif miner != '':
        # Vérifie qu'un dossier a été donnée pour le noeud
        if working_dir == '':
            print('Error: No working directory provided!\nUse "-working-dir" option.')
            exit(1)
        # Lance un noeud qui va rejoindre le réseau
        node = Node(miner, working_dir, peers)
        if not node.initialized:
            node.create()
        # Crée le bloc de départ
        node.blocks.createFirstBlock()
        # Tente de miner le block suivant
        while True:
            node.mine()