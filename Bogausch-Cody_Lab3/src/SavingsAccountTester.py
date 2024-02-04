
#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      Tester file to check the BankAccount and SavingsAccount classes
"""

__author__ = "Prof. Mikijanic"
__version__ = "1.0"

from BankAccount import BankAccount
from SavingsAccount import SavingsAccount

class SavingsAccountTester:

    # Description:
    #    ???
    # INPUT:
    #    ???
    # OUTPUT
    #    ???    
    def main():
        # Test for the BankAccount Class
        bob = BankAccount(1000)
        print(bob.getBalance())
        bob.deposit(5000)
        print(bob.getBalance())
        bob.withdraw(1000)
        print(bob.getBalance())
        bob.deposit(2000)
        print(bob.getBalance())
        bob.deposit(1000)
        print(bob.getBalance())
        bob.withdraw(2000)
        print(bob.getBalance())
        
   
        print("____________________________")


        anne = SavingsAccount(.5, 1000)
        print(anne.getBalance())
        anne.addInterest()
        print(anne.getBalance())
        anne.withdraw(1000)
        print(anne.getBalance())
        anne.deposit(2000)
        print(anne.getBalance())
        anne.deposit(1000)
        print(anne.getBalance())
        anne.withdraw(2000)
        print(anne.getBalance())
        anne.addInterest()
        print(anne.getBalance())

    if __name__ == "__main__":
        main()