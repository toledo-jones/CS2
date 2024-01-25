# !/usr/bin/env python3
# coding: utf-8
"""
Name: Cody Bogausch
Description:  A function object is a value you can assign to a variable or pass as an argument.
For example, do_twice is a function that takes a function object as an argument and calls it twice:
  def do_twice(f):
  f()
  f()
 Here’s an example that uses do_twice to call a function named print_spam twice.
  def print_spam():
  print('spam')
  do_twice(print_spam)
Type this example into a script and test it.

Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice,
passing the value as an argument. 

Create a function called print_twice, which takes a string as an argument, and prints out a value twice.

Use the modified version of do_twice to call print_twice twice, passing the word 'data' as an argument.

Define a new function called do_four that takes a function object and a value and calls the function four times,
passing the value as a parameter.
There should be only two statements in the body of this function, not four.
"""


def main():
    # Entry point
    print("Spam Spammer v 1.00")
    execute_function_n_times(print_twice, 'data', n=2)


def execute_function_n_times(function, *args, n: int):  # do_twice()
    """ Calls a function n number of times.
    n must be an integer. """
    for _ in range(n):
        function(*args)


def print_twice(args: str):
    """ Prints string argument twice"""
    for times in range(2):
        print(args)


def do_four(function, args):
    """ Calls a function 4 times passing the args variable as it's arguments"""
    for _ in range(4):
        function(args)


# If this script is executed run as main
if __name__ == '__main__':
    main()
