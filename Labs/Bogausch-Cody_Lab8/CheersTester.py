#!/usr/bin/env python3
# coding: utf-8
##By: Professor Mikijanic

###############################################################################
# Tester class for the RecursionPosition class. This program is used to 
# demonstrate principles of recursion, specifically recursive call loops and 
# the effect of location on executible code. 
#
# Note:
#   RecursionPosition functions all use integers to complete calculations.
#
# Functions:
#   main - Mainline for the CheersTester class
#
# ChangeLog: C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#
# Version
#   January 1, 2024
#
##############################################################################/

__author__ = "C. Mikijanic"
__version__ = 1.0 

from RecursionPosition import *

class CheersTester:
    def main():
        print("___________________________________________")
        print("Test of cheersIncrement function:")
        print("___________________________________________")
        print("----------------------------------------")
        print("Parameter = 1")
        RecursivePosition.cheersIncrement(1)
        print("----------------------------------------")
        print("Parameter = 2")
        RecursivePosition.cheersIncrement(2)
        print("----------------------------------------")
        print("Parameter = 3")
        RecursivePosition.cheersIncrement(3)
        print("----------------------------------------")
        print("Parameter = 4")
        RecursivePosition.cheersIncrement(4)
        print("----------------------------------------") 
        print("Parameter = 5")
        RecursivePosition.cheersIncrement(5)
        print("----------------------------------------")                
        print("Parameter = 0")
        RecursivePosition.cheersIncrement(0)
        print("----------------------------------------")
        print("Parameter = -1")
        RecursivePosition.cheersIncrement(0)
        print("----------------------------------------") 

        print("___________________________________________")
        print("Test of cheersDecrement function:")
        print("___________________________________________")
        print("----------------------------------------")
        print("Parameter = 1")
        RecursivePosition.cheersDecrement(1)
        print("----------------------------------------")
        print("Parameter = 2")
        RecursivePosition.cheersDecrement(2)
        print("----------------------------------------")
        print("Parameter = 3")
        RecursivePosition.cheersDecrement(3)
        print("----------------------------------------")
        print("Parameter = 0")
        RecursivePosition.cheersDecrement(0)
        print("----------------------------------------")
        print("Parameter = -1")
        RecursivePosition.cheersDecrement(0)
        print("----------------------------------------")

        print("___________________________________________")
        print("Test of cheersDivide function:")
        print("___________________________________________")
        print("----------------------------------------")
        print("Parameter = 1")
        RecursivePosition.cheersDivide(1)
        print("----------------------------------------")
        print("Parameter = 2")
        RecursivePosition.cheersDivide(2)
        print("----------------------------------------")
        print("Parameter = 3")
        RecursivePosition.cheersDivide(3)
        print("----------------------------------------")
        print("Parameter = 4")
        RecursivePosition.cheersDivide(4)
        print("----------------------------------------")
        print("Parameter = 0")
        RecursivePosition.cheersDivide(0)
        print("----------------------------------------")
        print("Parameter = -1")
        RecursivePosition.cheersDivide(-1)
        print("----------------------------------------")

        print("___________________________________________")
        print("Test of before function:")
        print("___________________________________________")
        print("----------------------------------------")
        print("Parameter = 1")
        RecursivePosition.before(1)
        print("----------------------------------------")
        print("Parameter = 2")
        RecursivePosition.before(2)
        print("----------------------------------------")
        print("Parameter = 3")
        RecursivePosition.before(3)
        print("----------------------------------------")
        print("Parameter = 0")
        RecursivePosition.before(0)
        print("----------------------------------------")
        print("Parameter = -1")
        RecursivePosition.before(-1)
        print("----------------------------------------")

        print("___________________________________________")
        print("Test of after function:")
        print("___________________________________________")
        print("----------------------------------------")
        print("Parameter = 1")
        RecursivePosition.after(1)
        print("----------------------------------------")
        print("Parameter = 2")
        RecursivePosition.after(2)
        print("----------------------------------------")
        print("Parameter = 3")
        RecursivePosition.after(3)
        print("----------------------------------------")
        print("Parameter = 0")
        RecursivePosition.after(0)
        print("----------------------------------------")
        print("Parameter = -1")
        RecursivePosition.after(-1)
        print("----------------------------------------")

        print("___________________________________________")
        print("Test of beforeAndAfter function:")
        print("___________________________________________")
        print("----------------------------------------")
        print("Parameter = 1")
        RecursivePosition.beforeAndAfter(1)
        print("----------------------------------------")
        print("Parameter = 2")
        RecursivePosition.beforeAndAfter(2)
        print("----------------------------------------")
        print("Parameter = 3")
        RecursivePosition.beforeAndAfter(3)
        print("----------------------------------------")
        print("Parameter = 0")
        RecursivePosition.beforeAndAfter(0)
        print("----------------------------------------")
        print("Parameter = -1")
        RecursivePosition.beforeAndAfter(-1)
        print("----------------------------------------")


    if __name__ == "__main__":
        main()