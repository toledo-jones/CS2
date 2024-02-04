#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
        A bank account has a balance that can be changed by 
        deposits and withdrawals.
   Functions:
      __init__: takes optional initialBalance parameter, set to 0.0 by default
      deposit: deposit money into this account
      withdraw: withdraw money from this account
      getBalance: returns current balance
      setBalance: sets the current balance (overrides balance) (use with caution!)
      transfer: uses the deposit and withdraw methods to move money from one account to another

   Constants:
      None
"""

__author__ = "Cody Bogausch"
__version__ = "1.0"


class BankAccount:

    # Constructs a bank account with a zero balance or an initial balance
    # INPUT:
    #    initialBalance: set to 0.0 by default
    # OUTPUT
    #    None
    def __init__(self, initialBalance=0.0):
        self.setBalance(initialBalance)

    # Deposits money into the bank account.
    # INPUT:
    #    amount: money to deposit into account
    # OUTPUT
    #    None
    def deposit(self, amount):
        # Get current balance
        current_balance = self.getBalance()

        # Calculate new balance based on amount
        new_balance = amount + current_balance

        # use setBalance to change balance of account to calculated value.
        self.setBalance(new_balance)

    # Withdraws money from the bank account.
    # INPUT:
    #    amount: money to withdraw from account
    # OUTPUT
    #    None
    def withdraw(self, amount):
        # Get current balance
        current_balance = self.getBalance()

        # Calculate new balance based on amount
        new_balance = current_balance - amount

        # use setBalance to change balance of account to calculated value.
        self.setBalance(new_balance)

    # Gets the current balance of the bank account.
    # INPUT:
    #    None
    # OUTPUT
    #    balance: current balance of account
    def getBalance(self):
        return self.balance

    # Sets the current balance of the bank account.
    # INPUT:
    #    new_balance: amount to set the balance to. (Completely overrides current balance)
    # OUTPUT
    #    None
    def setBalance(self, new_balance):
        self.balance = new_balance

    # Transfers money from the bank account to another account
    # INPUT:
    #    amount: money to transfer
    #    account: BankAccount object to transfer money into
    # OUTPUT
    #    None
    def transfer(self, amount, account):
        # Withdraw amount from this account
        self.withdraw(amount)

        # Deposit into other account
        account.deposit(amount)


