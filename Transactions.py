from TransactionsParent import TransactionsParent

""" 
Classe Transaction hérite de la classe TransactionParent

Classe fille correspondant à une transaction
"""

class Transactions(TransactionsParent):

    def __init__(self, node):
        super().__init__(True, node)

        
if __name__ == '__main__':
    trans = Transactions('node_1')
    print("Trans list = "+str(trans.listTrans()))
    tr1 = trans.writeTrans('3.6764f46975c7de06', '3.5541f46975c7de06', '100', '1')
    print("tr1 = "+str(tr1)+" : OK")
    l = trans.listTrans()
    print("Trans list = "+str(l))
    print('Trans ' + str(l[0]) + ' = ' + str(trans.readTrans(l[0])))