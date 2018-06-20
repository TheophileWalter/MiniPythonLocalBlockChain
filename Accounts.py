# coding=utf-8
#!/bin/python3

import os
import re
import filecmp
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

    # Method : append a new account in account.txt
    # Params : self
    def _create_account(self, uniqueId, amount):
        accountFilePath = self.nodePath+_get_new_hash(self)
        accountFile = open(accountFilePath, 'w+')
        accountFile.write(str(uniqueID)+":"+str(amount))
        accountFile.close()
    
    # Method : get list of account nodes
    # Params : self
    def _get_accounts_list(self):
        self.accountsFilesList = os.listdir("somedirectory")
        #for p in self.accountsFilesList: print(p)
        return filePath

    # Method : modify account
    # Params : self, accountId
    def _modify_account(self, accountId, amount):
        accountFileToModify = open(accountId, 'w')
        accountFileToModify.write(str(amount))
        accountFileToModify.close()

    # Method : check if account already exists
    # Params : self, accountId
    def _modify_account(self, accountId):
        fileName = self.nodePath+"/"+accountId
        return os.path.isfile(fileName)


# TESTS
newAccount1 = Accounts('1.e970dc85732370a2', '500')
newAccount1._get_accounts_list()
newAccount1._create_account()

newAccount2 = Accounts("2.66824d0f1ad014f5", "4564")
newAccount2._get_accounts_list()
newAccount2._create_account()
    