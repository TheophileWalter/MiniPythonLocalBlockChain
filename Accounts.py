# coding=utf-8
#!/bin/python3

import os
import re
import hashlib
import random


class Accounts:

    # Method : init
    # Params : self, nodePath
    def __init__(self, nodeName, nodePath):
        self.nodePath = nodePath + 'accounts' if nodePath[-1] == '/' else nodePath + '/accounts'
        self.nodeName = nodeName

    # Method : generate new hash
    # Params : self
    def _get_new_hash(self):
        intToHash = random.randint(0, 2**32-1)
        return hashlib.md5(str(intToHash).encode()).hexdigest()
    
    # Method : get list of account nodes
    # Params : self
    def _get_accounts_list(self):
        return os.listdir(self.nodePath)

    # Method : modify account
    # Params : self, accountId, amount
    def modify_account(self, accountId, amount):
        fileName = self.nodePath + '/' + accountId
        accountFileToModify = open(fileName, 'w')
        accountFileToModify.write(str(amount))
        accountFileToModify.close()

    # Method : check if account already exists
    # Params : self, accountId
    def _check_if_account_already_exists(self, accountId):
        fileName = self.nodePath + '/' + accountId
        return os.path.isfile(fileName)

    # Method : create account
    # Params : self, amount
    def create_account(self, amount):
        hashCreated = Accounts._get_new_hash(self)
        while Accounts._check_if_account_already_exists(self, hashCreated):
            Accounts.create_account(self, amount)
        
        fileName = str(self.nodePath + '/' + hashCreated)
        accountFileToModify = open(fileName, 'w')
        accountFileToModify.write(str(amount))
        accountFileToModify.close()
        return hashCreated
    
    # Method : read account
    # Params : self, accountId
    def get_account_amount(self, accountId):
        fileName = self.nodePath + '/' + accountId
        if Accounts._check_if_account_already_exists(self, accountId):
            with open(fileName, 'r') as f:
                try:
                    return float(f.read())
                except:
                    return -1
        else:
            return -1

# TESTS
if __name__ == '__main__':
    newAccount1 = Accounts('node_1', './node_1')
    # test create
    account11 = newAccount1.create_account(500)
    print(account11 + ' : ' + open('./node_1/accounts/'+account11).read() + ' [=? 500]')
    # test modify
    newAccount1.modify_account(account11, 400)
    print(account11+' : ' + open('./node_1/accounts/'+account11).read() + ' [=? 400]')
    # test _check_if_account_already_exists
    print('File already exists : ' + str(newAccount1._check_if_account_already_exists(account11)) + ' [=? True]')
    print('File already exists : ' + str(newAccount1._check_if_account_already_exists('20374ca3ee149e19d5e0a024f7062836')) + ' [=? False]')
    # test _get_new_hash
    print(newAccount1._get_new_hash() + ' != '+newAccount1._get_new_hash())
    # test accounts list
    print('Accounts list : ' + str(newAccount1._get_accounts_list()))
    # test get account amount
    print('Amount of ' + account11 + ' = ' + str(newAccount1.get_account_amount(account11)) + ' [=? 400]')