# !/usr/bin/env python3
# coding: utf-8
"""
Name: Cody Bogausch
Description:  The Fibonacci sequence is a famous mathematical sequence used in
graphics program algorithms in order to create computer generated images of
natural phenomenon, such as plant leaves, shells, and lava splatters. 
"""


def main():
    # Entry point
    print(f"The first fibonacci number above 50,000 is: {get_fibonacci_above_value(50000)}")


def get_fibonacci_above_value(value):
    # Initialize the sequence
    sequence = [0, 1]

    sum = 0
    while sum < value:
        # Debug
        print(sequence)

        # Sum is the last two variables in the list
        sum = sequence[-1] + sequence[-2]

        # Add that sum to our sequence and then repeat 
        sequence.append(sum)
    return sum


# If this script is executed run as main
if __name__ == '__main__':
    main()
