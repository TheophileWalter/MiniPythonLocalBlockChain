# MiniPythonLocalBlockChain
Projet du cours Blockchain

### Main informations
Node = Miner

### TODO list
- [ ] Class : **Main.py**
- [ ] Class : **Blocks.py** _Théophile_
- [ ] Class : **TransactionsParent.py** (classe mère de Transactions et PendingTransactions, définit le dossier où chercher) _Alice_
- [ ] Class : **Transactions.py** (hérite de TransactionsParent) _Alice_
- [ ] Class : **PendingTransactions.py** (hérite de TransactionsParent, rajoute une méthode qui supprime une transaction) _Alice_
- [ ] Class : **Accounts.py** _Alexis_
  - [x] _init__(self, nodeName)
  - [x] _get_new_hash(self)
  - [x] _get_accounts_list(self)
  - [x] modify_account(self, accountId, amount)
  - [x] _check_if_account_already_exists(self, accountId)
  - [x] create_account(self, amount)
  - [x] get_account_amount(self, accountId)
  - [x] tests
