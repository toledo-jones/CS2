#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
        A bank account has a balance that can be changed by 
        deposits and withdrawals.
        This class will serve as the parent for all other types of bank accounts. 
   
   Functions:
      getBalance
      setBalance
      deposit
      withdraw
      transfer
   
   Constants:
      None  
"""

__author__ =  "Cody Bogausch"
__version__ =  "1.0"

class BankAccount:
    def __init__(self, initialBalance=0.0) -> None:
        """
        Creates a bank account with zero balance or some other starting balance
        
        This will serve as the parent for all other types of accounts

        :param initialBalance: The starting balance of this account. Default to 0. 
        """
        self.setBalance(initialBalance)
    
    def getBalance(self) -> float:
        """
        Get Balance

        returns: Exact current account standing
        """
        return self._balance

    def setBalance(self, newBalance) -> None:
        """
        Set Balance
        
        Typically only called during init 
        :param newBalance: New balance to replace old balance
        """
        self._balance = newBalance

    def deposit(self, amount: float) -> None:    
        """
        Add some amount of money to the account balance. 
         
        This will add money to this account

        :param amount: amount of money to add to the balance
        """
        # TODO: Do some enforcement of deposits. Check if they're negative... etc

        # Retrieve our current balance and then add our deposit
        new_balance = self.getBalance() + amount
        
        # Update balance
        self.setBalance(new_balance) 

    def withdraw(self, amount): 
        """
        Remove some amount of money from the account balance. 
            
        This will remove money from this account

        :param amount: amount of money to remove from the balance
        """
        # TODO: Do some enforcement of withdraws. Check if they're negative... etc

        # Retrieve our current balance and then subtact our withdraw
        new_balance = self.getBalance() - amount
        
        # Update balance
        self.setBalance(new_balance) 
    
    def transfer(self, amount, other):
        "This function is not completed..."
    