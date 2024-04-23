#!/usr/bin/env python
# coding: utf-8

# !/usr/bin/env python3

""""
   Description:
      A bank account can be of type Savings Account.
   Functions:
      __init__: constructs a new savings account
      addInterest: add interest to account based on balance and amount
   Constants:
      None
"""

__author__ = "???"
__version__ = "1.0"

from BankAccount import BankAccount


class SavingsAccount(BankAccount):

    # Description:
    #    Constructs a savings account with an interest rate and initial balance
    # INPUT:
    #    rate (float): interest rate for this savings account
    #    initialBalance (float): starting balance of this account. Default to 0.0
    # OUTPUT
    #    None
    def __init__(self, rate, initialBalance=0.0):
        super().__init__(initialBalance)
        self.setRate(rate)
        self.minimumBalance = 0.0

    # Description:
    #    Adds interest to the savings account. Calculated based on the rate and account balance.
    # INPUT:
    #    None
    # OUTPUT
    #    None
    def addInterest(self):
        # Calculate interest using the principle * rate / 100
        interest = self.getBalance() * self.interestRate / 100

        # Deposit interest into back into account
        self.deposit(interest)

    # Description:
    #    Withdraw money from account
    #    This will override the parent method for withdraw and impose a restriction to the account
    #    A savings account cannot have a minimum balance
    # INPUT:
    #    amount: amount to withdraw
    # OUTPUT
    #    None
    def withdraw(self, amount):
        # Only permit a legal withdraw
        if self.getBalance() - amount <= self.minimumBalance:
            # Withdraw will bring account below minimum.
            print("Insufficient Funds. Cannot perform withdraw.")
            return False

        # We can allow the withdraw
        super().withdraw(amount)

    # Description:
    #    Sets the interest rate for this account
    # INPUT:
    #    rate: new interest rate
    # OUTPUT
    #    None
    def setRate(self, rate):
        self.interestRate = rate

    # Description:
    #    Gets the interest rate for this account
    # INPUT:
    #    None
    # OUTPUT
    #    interestRate: current interest rate for this account
    def getRate(self):
        return self.interestRate
