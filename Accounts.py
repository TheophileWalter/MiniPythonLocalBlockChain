# coding=utf-8
#!/bin/python3

class Accounts(object):

    # Method : init
    # Params : self, uniqueID, amount
    def __init__(self, uniqueID, amount):
        self.uniqueID = uniqueID
        self.amount = amount


    # Method : append a new account in account.txt
    # Params : self
    def _create_account(self):
        accountFile = open('accounts.txt', 'w+')
        accountFile.write(str(self.uniqueID)+":"+str(self.amount))


newAccount1 = Accounts('1.e970dc85732370a2', '500')
newAccount1._create_account()

newAccount2 = Accounts("2.66824d0f1ad014f5", "4564")
newAccount2._create_account()
    