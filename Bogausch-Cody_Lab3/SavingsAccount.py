#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      A savings account is a type of bank account with a mininimum balance 
      and an interest rate
   Functions:
      addInterest
      withdraw
   Constants:
      ???      
"""

__author__ =  "Cody Bogausch"
__version__ = "1.0" 

from BankAccount import BankAccount

class SavingsAccount(BankAccount):
   def __init__(self, rate: float, initialBalance: float):
      """
      
      """
      self.setInterestRate(rate)
      super().setBalance(initialBalance)
      self.setMinimumBalance()

   def addInterest(self) -> None: 
      
      interest = self.minimumBalance * self.interestRate / 100
      "This function is not completed..."


   def withdraw(self, amount: float) -> None: 
      """
      Remove some amount of money from the account balance. 
         
      This will remove money from this account

      :param amount: amount of money to remove from the balance
      """
      
      if (self.minimumBalance <= self.getBalance()):
            
            
   def setMinimumBalance(self, newMinimum=1.00):
      self.minimumBalance = newMinimum

   def setInterestRate(self, newRate):
      self.interestRate = newRate

   def getMinimumBalance(self) -> float:
      return self.minimumBalance