#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      An account where monies are deposited based on time.
   Functions:
      ???
   Constants:
      ???        
"""

__author__ = "???"
__version__ = "1.0"

class TimeDepositAccount("???"):

    PENALTY_FEE = 20

    # Description:
    #    ???
    # INPUT:
    #    ???
    # OUTPUT
    #    ???
    def __init__(self, rate, initialBalance, monthNumber):
        "This function is not completed..."

    # Description:
    #    ???
    # INPUT:
    #    ???
    # OUTPUT
    #    ???
    def addInterest(self):
        "This function is not completed..."

    # Description:
    #    ???
    # INPUT:
    #    ???
    # OUTPUT
    #    ???
    def withdraw(self, amount):
        if ("???????????"):
                self.timeBalance = self.timeBalance - TimeDepositAccount.PENALTY_FEE
                print("Penalty of " + str(TimeDepositAccount.PENALTY_FEE) + " withdrawn.")   
        "This function is not completed..."

def main():   
    bob = TimeDepositAccount(.5, 1000.00, 12)
    for i in range(10):
        print(i)
        bob.addInterest()
        print("Your balance is " + str(bob.getBalance()))
    bob.withdraw(100)
    print("Your balance is " + str(bob.getBalance()))
    bob.addInterest()
    print("Your balance is " + str(bob.getBalance()))
    bob.addInterest()
    print("Your balance is " + str(bob.getBalance()))
    bob.addInterest()
    print("Your balance is " + str(bob.getBalance()) + " dollars.")
    bob.withdraw(100)
    print("Your balance is " + str(bob.getBalance()))

if __name__ == "__main__":
    main()