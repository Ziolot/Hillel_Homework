import uuid
from datetime import date


class Bank:
    bank_fee = 0.01

    def __init__(self, name_bank):
        self.name_bank = name_bank
        self._balance = 0
        self._transactions = []
        self.bank_account = uuid.uuid4()

    @property
    def current_balance(self):
        deposit = 0
        withdraw = 0
        for transaction in self._transactions:
            if transaction[1] == 'Deposit funds ':
                deposit += transaction[0]
            else:
                withdraw += transaction[0]
        return deposit - withdraw

    def deposit(self, amount):
        self._balance += amount * 0.99
        self._transactions.append((amount, 'Deposit funds ', str(date.today())))

    def withdrawal_of_funds(self, amount):
        if amount < self._balance:
            self._balance -= amount * 1.01
        else:
            print('Not enough funds on the Deposit ', str(self._balance))
        self._transactions.append((amount, 'Withdraw funds ', str(date.today())))


operation = Bank('The Arztotska Bank')
print('Bank - ', operation.name_bank)
print('Bank account - ', operation.bank_account)
operation.deposit(5000)
print('deposit of funds - ', operation._balance)
operation.withdrawal_of_funds(3000)
print('deposit of funds - ', operation._balance)
operation.withdrawal_of_funds(800)
print('Withdraw of funds - ', operation._balance)
print('archive of transactions - ', operation._transactions)
print('current balance - ', operation._balance)
