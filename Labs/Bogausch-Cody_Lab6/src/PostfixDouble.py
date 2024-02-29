#!/usr/bin/env python3
# coding: utf-8

from sys import version
from math import sqrt

"""
    File: PostfixDouble.py
    Description: 
        ???
    Functions:
        ???
    Constants:
        ???
"""

__author__ = "Cody Bogausch"
__version__ = "1.0"

# Prints the system's version of the Python to the terminal for programmer checking.
# Switch statements were put in Python 3.10 - this file is 
#   backwards compatible. It must run on earlier versions of Python.
print(version)


class PostfixDouble:

    def __init__(self, data):
        self.operands = []
        self.postfix = data.replace("\n", "")

    def infixEquationToPostfix(self):
        print("The value of [" + self.postfix + "] is ", end="")
        express = self.postfix
        fullNumber = None
        if len(self.postfix) <= 0:
            print("The postfix can not be less than 1")

        else:
            end_of_data = False
            while not end_of_data:



    def push(self, a):
        self.operands.append(a)

    def divide(a, b):
        return b / a

    def subtract(a, b):
        return b - a

    def conversion(self, convert):

        if convert is None:
            print("The string is None.")

        "This function is not completed..."
        return "This function is not completed..."

    def power(a, b):
        return PostfixDouble.powerSuper(a, b)

    def powerSuper(a, b):

        if a == 0 and b == 0:

            raise Exception("Raise zero to zero power")

        elif a == 0:

            return 0

        elif b == 0:

            return 1

        else:

            return a ** b

    def negative(a):
        return -a

    def square(a):
        return a * a
