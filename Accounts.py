# coding=utf-8

class Accounts:

    def __int__(self, id_node, id_block):
        self.id_node = id_node
        self.id_block = id_block
    
    accountFilePath = "nodes/"+id_node+"/"+id_block


    def _get_file_content():
        with open(accountFilePath, "r") as f:
            linesBlock = f.readlines()
    

    def _create_account(hashToAdd, amountToAdd):
        accountFile = open('accounts.txt', 'w+')
        accountFile.write(str(id_block)+"="+hashToAdd)
        accountFile.write(str(id_block)+"="+amountToAdd)
    

    def _main():
        _create_account("1.hashCode", 5000)

    _main()