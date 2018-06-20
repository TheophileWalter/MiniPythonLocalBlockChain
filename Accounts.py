# coding=utf-8
#!/bin/python3

import os
import re
import hashlib
import random


class Accounts(object):

    # Method : init
    # Params : self, nodeName
    def __init__(self, nodeName):
        self.nodePath = "./nodes/"+nodeName+"/"
        self.accountsFilesList = []

    # Method : generate new hash
    # Params : self
    def _get_new_hash(self):
        intToHash = random.randint(0, 2**32-1)
        return hashlib.md5(intToHash).hexdigest()
    
    # Method : get list of account nodes
    # Params : self
    def _get_accounts_list(self):
        self.accountsFilesList = os.listdir("somedirectory")
        #for p in self.accountsFilesList: print(p)
        return filePath

    # Method : modify account
    # Params : self, accountId, amount
    def modify_account(self, accountId, amount):
        fileName = self.nodePath+"/"+accountId
        accountFileToModify = open(fileName, 'w')
        accountFileToModify.write(str(amount))
        accountFileToModify.close()

    # Method : check if account already exists
    # Params : self, accountId
    def _check_if_account_already_exists(self, accountId):
        fileName = self.nodePath+"/"+accountId
        return os.path.isfile(file_name)

    # Method : create account
    # Params : self, amount
    def create_account(self, accountId, amount):
        hashCreated = _get_new_hash(self)
        fileName = self.nodePath+"/"+hashCreated
        accountFileToModify = open(fileName, 'w')
        accountFileToModify.write(str(amount))
        accountFileToModify.close()
        return hashCreated
    

# TESTS
if __name__ == '__main__':
    newAccount1 = Accounts('node_1')
    account11 = newAccount1.create_account(500)
    print(account11)
    newAccount1.modify_account(account11, 400)

    newAccount2 = Accounts('node_2')
    print(newAccount2._get_accounts_list())
    newAccount2._check_if_account_already_exists
    