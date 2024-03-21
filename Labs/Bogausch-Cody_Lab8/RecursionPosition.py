#!/usr/bin/env python3
# coding: utf-8
##By: Professor Mikijanic

###############################################################################
# The RecursivePosition class contains functions which show different 
# common structures of recursive functions. 
#
# Note:
#   These functions all use integers to complete calculations.
#
# Functions:
#   cheersIncrement
#   cheersDecrement
#   cheersDivide
#   before
#   after
#
# ChangeLog: C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#           C. Bogausch
#   (cody.bogausch@sunycgcc.edu)
#
# Version
#   January 1, 2024
#
##############################################################################/

__author__ = "C. Mikijanic, Cody Bogausch"
__version__ = 1.0


class RecursivePosition:

    # Description: prints n+3 "idy"s before "Tally ho!"
    #     (In the case of n = 4 or higher, the function only prints "Tally ho!")
    # Parameter: n, integer.  
    # Interval: Increase by 1  
    # Base Case: n must be greater than 4 
    # Note: do not check for data type using if or try-catch - enforce this by using int()     
    @staticmethod
    def cheersIncrement(n):

        # Force n to an integer
        n = int(n)

        # Handle Base Case
        if n >= 4:

            # Celebrate, we have reached the end of the recursion
            print("Tally ho!")

        # Any other case
        else:

            # Add an idy to our eventual Tally Ho!
            print("idy")

            # Recurse
            return RecursivePosition.cheersIncrement(n+1)

    # Description: prints n+1 "idy"s before "Tally ho!"
    #     (In the case of n = 1 or lower, the function only prints "Tally ho!")
    # Parameter: n, integer.  
    # Interval: Decrease by 1  
    # Base Case: n must be less than or eq to 1
    # Note: do not check for data type using if or try-catch - enforce this by using int()     
    @staticmethod
    def cheersDecrement(n):

        # Force n to an integer
        n = int(n)

        # Handle Base Case
        if n <= 1:

            # Celebrate, we have reached the end of the recursion
            print("Tally ho!")

        # Any other case
        else:

            # Add an idy to our eventual Tally Ho!
            print("idy")

            # Recurse
            return RecursivePosition.cheersDecrement(n-1)

    # Description: prints n/2 "idy"s before "Tally ho!" (rounded up)
    #     (In the case of n = 0 or lower, the function only prints '"Tally ho!"')
    #     (In the case of n = 3 or lower, the function prints "idy" and '"Tally ho!"')
    # Parameter: n, integer. 
    # Interval: Divide by 2  
    # Base Case: n must be less than or eq to 1 
    # Note: do not check for data type using if or try-catch - enforce this by using int()         
    @staticmethod
    def cheersDivide(n):

        # Force n to an integer
        n = int(n)

        # Handle Base Case
        if n <= 1:

            # Celebrate, we have reached the end of the recursion
            print("Tally ho!")

        # Any other case
        else:

            # Add an idy to our eventual Tally Ho!
            print("idy")

            # Recurse
            return RecursivePosition.cheersDivide(n/2)

    # Parameter: n, integer.
    # Description: Print the number before a recursive if loop
    # Interval: Decrease by 1
    # Base Case: Implicit
    # Stop point: n must be greater than 1
    # Note: do not check for data type using if or try-catch - enforced by using int()
    @staticmethod
    def before(n):

        # Print, as per instructions
        print(n)

        # Handle Base Case
        if n > 1:

            # Base case is met, recurse
            RecursivePosition.before(n-1)

    # Parameter: n, integer.
    # Description: Print the number after a recursive if loop
    # Interval: Decrease by 1
    # Base Case: Implicit
    # Stop point: n must be greater than 1
    # Note: do not check for data type using if or try-catch - enforced by using int() 
    @staticmethod
    def after(n):

        # Handle Base Case
        if n > 1:

            # Base case is met, recurse
            RecursivePosition.after(n-1)

        # Print, as per instructions
        print(n)

    # Parameter: n, integer.
    # Description: Print the number before and after a recursive if loop
    # Interval: Decrease by 1
    # Base Case: Implicit
    # Stop point: n must be greater than 1
    # Note: do not check for data type using if or try-catch - enforced by using int()  
    @staticmethod
    def beforeAndAfter(n):

        # Print, as per instructions
        print(n)

        # Handle Base Case
        if n > 1:

            # Base case is met, recurse
            RecursivePosition.beforeAndAfter(n-1)

        # Print, as per instructions
        print(n)
