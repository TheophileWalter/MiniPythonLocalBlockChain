# MiniPythonLocalBlockChain
Projet du cours Blockchain

### Main informations
Node = Miner

### TODO list
- [ ] Class : **Main.py**

- [ ] Class : **Blocks.py** _Théophile_
  - [x] _init_(self, nodeName)
  - [x] getBlock(self, id)
  - [x] getList(self)
  - [x] writeBlock(self, previous, miner, pow, date, nonce, transactions)
  - [x] tests

- [ ] Class : **TransactionsParent.py** (classe mère de Transactions et PendingTransactions, définit le dossier où chercher) _Alice_
  - [x] _init_(self, b, node)
  - [x] listTrans(self)
  - [x] readTrans(self, trans)
  - [x] writeTrans(self, src, dest, amount, fees)
  - [x] tests

- [ ] Class : **Transactions.py** (hérite de TransactionsParent) _Alice_
  - [x] _init_(self, node)

- [ ] Class : **PendingTransactions.py** (hérite de TransactionsParent) _Alice_
  - [x] _init_(self, node)
  - [x] transDelete(self,trans)

- [ ] Class : **Accounts.py** _Alexis_
  - [x] _init_(self, nodeName)
  - [x] _get_new_hash(self)
  - [x] _get_accounts_list(self)
  - [x] modify_account(self, accountId, amount)
  - [x] _check_if_account_already_exists(self, accountId)
  - [x] create_account(self, amount)
  - [x] get_account_amount(self, accountId)
  - [x] tests

- [x] Class : **Date.py** _Alexis_
  - [x] _init_(self)
  - [x] get_date(self)
  - [x] tests
  
- [ ] Class : **Node.py**
