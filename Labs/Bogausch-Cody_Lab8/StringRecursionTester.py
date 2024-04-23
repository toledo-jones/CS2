#!/usr/bin/env python3
# coding: utf-8
##By: Professor Mikijanic

###############################################################################
# The StringRecursion class tests different 
# common structures of recursive functions, demonstrating how different
# setups of recursion functions can perform the same computation.
#
# Note:
#   The functions tested all take a string as a parameter.
#
# Functions:
#   main - Mainline for the module
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

from RecursionMethod import *

class StringRecursion:

        def main():    

                print("")
                print("This a base check of all functions in Recursion Method: ")                    
                a1 = RecursionMethod()
                print(a1.number(""))
                a2 = RecursionMethod()
                print(a2.number("A"))
                a3 = RecursionMethod()
                print(a3.number("B"))
                a4 = RecursionMethod()
                print(a4.number("ABC"))
                a5 = RecursionMethod()
                print(a5.number("BCA"))
                a6 = RecursionMethod()
                print(a6.number("ABCACB"))
                
                print("")
                print("This is with the clearCount method: ")
        
                a7 = RecursionMethod()
                print(a7.number2(""))
                a7.clearCount()
                print(a7.number2("A"))
                a7.clearCount()
                print(a7.number2("B"))
                a7.clearCount()
                print(a7.number2("ABC"))
                a7.clearCount()
                print(a7.number2("BCA"))
                a7.clearCount()
                print(a7.number2("ABCACB"))

                #------------------------------------------------------------------------ Optimization begins 
                
                print("")
                print("This is with the counter being manipulated with a static recursive method: ")
                print("The reduction is split into three different parts.")
                print("One for each half of the string, and one for the new combined string.: ")
                
                print(RecursionMethod.number3(""))
                print(RecursionMethod.number3("A"))
                print(RecursionMethod.number3("B"))
                print(RecursionMethod.number3("ABC"))
                print(RecursionMethod.number3("BCA"))
                print(RecursionMethod.number3("ABCACB"))
                
                print("")
                print("This is with the counter being manipulated in the recursive method.")
                print("The reduction is put on one line.")        
                print(RecursionMethod.number4(""))
                print(RecursionMethod.number4("A"))
                print(RecursionMethod.number4("B"))
                print(RecursionMethod.number4("ABC"))
                print(RecursionMethod.number4("BCA"))
                print(RecursionMethod.number4("ABCACB"))
                
                print("")
                print("This is with the counter being manipulated in the recursive method: ")
                print("The reduction is included in the recursion.")
        
                print(RecursionMethod.number5(""))
                print(RecursionMethod.number5("A"))
                print(RecursionMethod.number5("B"))
                print(RecursionMethod.number5("ABC"))
                print(RecursionMethod.number5("BCA"))
                print(RecursionMethod.number5("ABCACB"))
                
                print("")
                print("This is with the counter else ommited in the recursive method: ")
                print("The reduction is included in the recursion.")
        
                print(RecursionMethod.number6(""))
                print(RecursionMethod.number6("A"))
                print(RecursionMethod.number6("B"))
                print(RecursionMethod.number6("ABC"))
                print(RecursionMethod.number6("BCA"))
                print(RecursionMethod.number6("ABCACB"))
              

        if __name__ == "__main__":
                main()
