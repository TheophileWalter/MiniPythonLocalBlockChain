# coding=utf-8
# Projet de Mini Blockchain

import sys

if __name__ == '__main__':
    # Récupération des paramètres
    working_dir = ''
    genesis = ''
    mono_memory = False
    mono_disk = False
    peer = ''
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
            peer = params[i]
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
        # Todo: Lancer un noeud en mémoire
    elif mono_disk:
        # Todo: Lancer un noeud sur disque
    elif miner != '':
        # Todo: Lancer un noeud qui a rejoindre le réseau