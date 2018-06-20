# coding=utf-8
#!/bin/python3

class Accounts:

    # Method : init
    # Params : 
    def __int__(self, id_node, id_block):
        self.id_node = id_node
        self.id_block = id_bloc
        self.accountFolder = "nodes/"+self.id_node+"/accounts/"
    
    # Method : get next account id
    # Params : return list of file names
    def _get_new_account_id(self):
        return os.listdir(self.accountFolder)


    def _create_account(self, hashToAdd, amountToAdd):
        accountFile = open('accounts.txt', 'w+')
        accountFile.write(str(id_block)+"="+hashToAdd)
        accountFile.write(str(id_block)+"="+amountToAdd)
    
    
    def _main(self):
        _create_account("1.", 5000)

    _main()