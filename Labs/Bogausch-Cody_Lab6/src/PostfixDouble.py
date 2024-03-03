#!/usr/bin/env python3
# coding: utf-8
import math
from sys import version
from math import sqrt

"""
    File: PostfixDouble.py
    Description: 
        Creates a postfix double object capable of calculating postfix expressions with floating point numbers
    Functions:
        add
        conversion
        divide
        infixEquationToPostfix
        multiply
        negative
        power
        powerSuper
        push
        square
        subtract
    Constants:
        None
"""

__author__ = "Cody Bogausch"
__version__ = "1.0"

# Prints the system's version of the Python to the terminal for programmer checking.
# Switch statements were put in Python 3.10 - this file is 
#   backwards compatible. It must run on earlier versions of Python.
print(version)


class PostfixDouble:
    def __init__(self, data):
        """
        Creates a postfix double object capable of calculating postfix expressions with floating point numbers
        :param data: string: expression to evaluate
        """
        self.operands = []
        self.postfix = data.replace("\n", "")

    def infixEquationToPostfix(self):
        """
        Evaluate a postfix expression and print the final answer
        """

        # User prompt
        print("The value of [" + self.postfix + "] is ", end="")

        # Create a variable to point to the postfix expression
        expression = self.postfix

        # Create an empty string to multi digit numbers
        fullNumber = str()

        # Error and early exit if the expression is not long enough to be evaluated
        if len(expression) <= 0:
            print("The postfix can not be less than 1")

        else:

            # End condition
            end_of_data = False

            # Index to iterate through
            index = 0

            # Evaluate expression
            while not end_of_data:

                # The current character in the post fix expression
                character = expression[index]

                # Control flow:
                if character == '+':

                    # Addition
                    first_operand = self.operands.pop()
                    second_operand = self.operands.pop()

                    answer = PostfixDouble.add(first_operand, second_operand)

                    # Push answer to the stack
                    self.push(answer)

                elif character == '-':

                    # Subtraction
                    first_operand = self.operands.pop()
                    second_operand = self.operands.pop()

                    answer = PostfixDouble.subtract(first_operand, second_operand)

                    # Push answer to the stack
                    self.push(answer)

                elif character == '/':

                    # Division
                    first_operand = self.operands.pop()
                    second_operand = self.operands.pop()

                    answer = PostfixDouble.divide(first_operand, second_operand)

                    # Push answer to the stack
                    self.push(answer)

                elif character == '*':

                    # Multiplication
                    first_operand = self.operands.pop()
                    second_operand = self.operands.pop()

                    answer = PostfixDouble.multiply(first_operand, second_operand)

                    # Push answer to the stack
                    self.push(answer)

                elif character == ' ':

                    # Character is a space, this is the delimiter in the expression
                    if fullNumber != '':

                        # If something is already in fullnumber convert it to a float:
                        fullNumber = self.conversion(fullNumber)

                        # Push full number to the stack
                        self.push(fullNumber)

                    # Reset container for full number
                    fullNumber = str()

                else:
                    # Group together multi digit numbers
                    fullNumber += character

                # Finally reach the end of the expression:
                if index == len(expression) - 1:
                    # Print the answer
                    print(answer)

                    # exit the loop
                    end_of_data = True

                # increment index
                index += 1

    @staticmethod
    def multiply(a, b):
        """
        Multiply two numbers.

        :param a: The first number to be multiplied.
        :param b: The second number to be multiplied.
        :return: The product of a and b.
        """
        return a * b

    @staticmethod
    def add(a, b):
        """
        Add two numbers.

        :param a: The first number to be added.
        :param b: The second number to be added.
        :return: The sum of a and b.
        """
        return a + b

    def push(self, a):
        """
        Push a value onto the stack.

        :param a: The value to be pushed onto the stack.
        """
        self.operands.append(a)

    @staticmethod
    def divide(a, b):
        """
        Divide two numbers.

        :param a: The dividend.
        :param b: The divisor.
        :return: The result of dividing b by a.
        """
        return b / a

    @staticmethod
    def subtract(a, b):
        """
        Subtract two numbers.

        :param a: The number to be subtracted.
        :param b: The number to subtract from.
        :return: The difference between b and a.
        """
        return b - a

    def conversion(self, convert):
        """
        Convert a string to a float.

        :param convert: The string to be converted.
        :return: The float value of the string.
        """
        if convert is None:
            print("The string is None.")

        return float(convert)

    @staticmethod
    def power(a, b):
        """
        Calculate the power of a to the b.

        :param a: The base.
        :param b: The exponent.
        :return: The result of raising a to the power of b.
        """
        return PostfixDouble.powerSuper(a, b)

    @staticmethod
    def powerSuper(a, b):
        """
        Calculate the power of a to the b with special cases for 0^0, 0^b, and a^0.

        :param a: The base.
        :param b: The exponent.
        :return: The result of raising a to the power of b with special cases handled.
        """
        if a == 0 and b == 0:
            raise Exception("Raise zero to zero power")
        elif a == 0:
            return 0
        elif b == 0:
            return 1
        else:
            return a ** b

    @staticmethod
    def negative(a):
        """
        Calculate the negative of a.

        :param a: The number to be negated.
        :return: The negative value of a.
        """
        return -a

    @staticmethod
    def square(a):
        """
        Calculate the square of a.

        :param a: The number to be squared.
        :return: The square of a.
        """
        return a * a

    @staticmethod
    def square_root(a):
        """
        Calculate the square root of a.

        :param a: The number to be rooted
        :return: The square root of a.
        """
        return math.sqrt(a)


