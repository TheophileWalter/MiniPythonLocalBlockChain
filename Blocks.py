# coding=utf-8
"""
    Projet Mini Blockchain
    Gestion des blocs
"""

class Blocks:

    # Constructeur de la classe
    # 
    # @params
    #   - nodeName : Le nom du noeud
    def __init__(self, nodeName):
        # Enregiste l'emplacement des blocs
        self.path = 'nodes/' + nodeName + '/blocks/'

    # Récupère un bloc donné (en fonction de son ID)
    # Retourne False en cas d'erreur
    def getBlock(self, id):
        # Lecture du bloc ligne par ligne
        block = {}
        with open(self.path + id, 'r') as f:
            content = f.readlines()
            for line in content:
                # Découpe en fonction des espaces
                identifier = line.split(' ')
                # Vérifie si la ligne est correcte
                if len(identifier) == 0:
                    return False
                # Vérifie l'identificateur
                if identifier[0] in ['previous', 'miner', 'pow', 'date', 'nonce']:
                    block[identifier[0]] = line[(len(identifier[0])+1):]
                elif identifier[0] == 'transactions':
                    block[identifier[0]] = identifier[1:]
                else:
                    return False
            f.close()
        return block

    # Récupère la liste des blocs de la chaîne
    def getList(self):
        return

# Test
if __name__ == '__main__':
    blocks = Blocks('nodes_1')
    b = blocks.getBlock('1.b9d946ccdd74dcae')
    print(b)

