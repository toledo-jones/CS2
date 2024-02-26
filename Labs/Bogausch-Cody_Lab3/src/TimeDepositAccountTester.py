#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      Tester file to check the TimeDepositAccount class
"""

__author__ = "Prof. Mikijanic"
__version__ = "1.0"

from TimeDepositAccount import *

class TimeDepositAccountTester:

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