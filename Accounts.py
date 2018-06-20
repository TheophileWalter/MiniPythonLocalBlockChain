# coding=utf-8
#!/bin/python3

import os
import re
import filecmp
import hashlib
import random

class Accounts(object):

    # Method : init
    # Params : self, uniqueID, amount
    def __init__(self, uniqueID, amount):
        self.uniqueID = uniqueID
        self.amount = amount
        self.accountsFilesList = []

    # Method : generate new hash
    # Params : self
    def _get_new_hash(self):
        intToHash = random.randint(0, 2**32-1)
        return hashlib.md5(intToHash).hexdigest()

    # Method : append a new account in account.txt
    # Params : self
    def _create_account(self):
        for accountFilePath in self.accountsList:
            accountFile = open(accountFilePath, 'w+')
            accountFile.write(str(self.uniqueID)+":"+str(self.amount))
    
    # Method : get list of account nodes
    # Params : self
    def _get_accounts_list(self):
        for root, dirs, files in os.walk("."):
            for fileName in files:
                filePath = os.path.join(root, fileName)
                
                if re.search("(\.\/nodes\/nodes_[0-9]+\/accounts\/.*)", filePath):
                    self.accountsFilesList.append(filePath)

        #for p in self.accountsFilesList: print(p)
        return filePath

    # Method : check if all accounts.txt are identicals
    # Params : self
    def _check_all_accounts(self):

        visitedAccountsFiles=[]

        for file1 in self.accountsFilesList:
            
            visitedAccountsFiles.append(file1)

            for file2 in self.accountsFilesList:
                if file2 in visitedAccountsFiles:
                    if not filecmp.cmp('file1.txt', 'file1.txt'):
                        return False
        
        return True


# TESTS
newAccount1 = Accounts('1.e970dc85732370a2', '500')
newAccount1._get_accounts_list()
newAccount1._create_account()

newAccount2 = Accounts("2.66824d0f1ad014f5", "4564")
newAccount2._get_accounts_list()
newAccount2._create_account()
    