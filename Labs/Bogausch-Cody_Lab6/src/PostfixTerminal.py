#!/usr/bin/env python3
# coding: utf-8

"""
    File: PostfixTerminal.py
    Description: 
        Terminal program for the PostfixDouble class. Takes a 
        text file with lines of text in reverse Polish notation
        and sends the lines to PostfixDouble for processing.
    Input:
        in.txt
    Functions:
        N/A
    Constants:
        N/A

    Note: in.text can only have postfix expressions.
       One expression = one line.
       More expressions can be added to in.txt.
"""

__author__ = "Prof. Mikijanic"
__version__ = "1.0"

from PostfixDouble import *


class PostfixTerminal:
    inputFile = open("in.txt")
    line = None
    line = inputFile.readline()
    while line != '':
        a = PostfixDouble(line)
        a.infixEquationToPostfix()
        line = inputFile.readline()
    inputFile.close()
