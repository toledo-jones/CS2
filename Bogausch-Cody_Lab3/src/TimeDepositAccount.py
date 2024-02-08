#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      An account where monies are deposited based on time.
   Functions:
      __init__: construct a new time deposit account, takes rate(float), intialBalance(float) and monthNumber(int)
      setTimeBalance: set a new # of months left until a penalty free withdraw
      getTimeBalance: returns current number of months left until a penalty free withdraw
      addInterest: adds interest based on the rate and current account balance
   Constants:
      PENALTY_FEE: cost to be added onto a withdraw when it is made before the time balance is 0
                    (penalize the user for early withdrawl)
"""

__author__ = "Cody Bogausch"
__version__ = "1.0"

from SavingsAccount import SavingsAccount

class TimeDepositAccount(SavingsAccount):

    PENALTY_FEE = 20

    # Description:
    #    Constructs a Time Deposit Account
    # INPUT:
    #    rate: (float) rate of interest bearing account
    #    initialBalance: (float) starting balance of the account
    #    monthNumber: (int) number of months left until the deposit can be withdrawn without penalty
    # OUTPUT
    #    ???
    def __init__(self, rate, initialBalance, monthNumber):
        super().__init__(rate, initialBalance)
        self.setTimeBalance(monthNumber)

    # Description:
    #    Set Time Balance
    # INPUT:
    #    monthNumber: (int) number of months left until the deposit can be withdrawn without penalty
    # OUTPUT
    #    None
    def setTimeBalance(self, monthNumber):
        self.timeBalance = monthNumber

    # Description:
    #    Get Time Balance
    # INPUT:
    #    None
    # OUTPUT
    #    timeBalance: (int) number of months remaining until the deposit can be withdrawn without penalty
    def getTimeBalance(self):
        return self.timeBalance

    # Description:
    #    Adds interest and ticks down the time balance by one month.
    #    This function is intended to be called once, monthly. Use with caution.
    # INPUT:
    #    None
    # OUTPUT
    #    None
    def addInterest(self):
        # Call parent addInterest
        super().addInterest()

        # Tick down the time balance by one month
        self.setTimeBalance(self.getTimeBalance() - 1)

    # Description:
    #    Overrides parent withdraw method to impose restrictions on the user for how long they must wait before
    #    making a withdraw
    # INPUT:
    #    amount(float): amount to withdraw from account
    # OUTPUT
    #    result(bool or float): True if the withdraw was successful,
    #                           False if the balance is too low
    #                           float if the withdraw was made early. Returns penalty amount in this case
    def withdraw(self, amount):
        # Check to see if the withdraw will incur a penalty
        if self.timeBalance > 0:
            print(f"Fee of ${self.PENALTY_FEE} is added withdraw amount of {amount}")
            # The withdraw is penalized by adding the penalty fee to the withdraw amount
            amount += self.PENALTY_FEE
        # Check to see if the withdraw goes through. The account may not have enough funds.
        if not super().withdraw(amount):
            return False
        # Send back to the penalty fee in a return value to so that is
        # removed from the account but not given to the customer.
        # This will require some additional code in the ATM. Or the bank teller. Or whoever is using this code.
        return self.PENALTY_FEE

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