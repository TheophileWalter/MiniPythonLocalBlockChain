# MiniPythonLocalBlockChain
Projet du cours Blockchain

### Main informations
Node = Miner

### TODO list
- [ ] Class : **Main.py**
- [ ] Class : **Blocks.py** _Théophile_
- [ ] Class : **TransactionParent.py** (classe mère de Transactions et PendingTransactions) _Alice_
- [ ] Class : **Transactions.py** (hérite de TransactionParent, définit uniquement le dossier où chercher)
- [ ] Class : **PendingTransactions.py** (hérite de TransactionParent, définit uniquement le dossier où chercher)
- [ ] Class : **Accounts.py** _Alexis_
  - [x] _init__(self, nodeName)
  - [x] _get_new_hash(self)
  - [x] _get_accounts_list(self)
  - [x] modify_account(self, accountId, amount)
  - [x] _check_if_account_already_exists(self, accountId)
  - [x] create_account(self, amount)
  - [x] get_account_amount(self, accountId)
  - [x] tests
