#!/usr/bin/env python3
# coding: utf-8


###############################################################################
# This class is a lab assignment tester
# *****************************************************************************************************
#  SortTest.py
#   This models some development jobs out in the field,
#       where the developer is in charge of not only going through the code line-by-line with a debugger,
#       but also creating test scripts which verify that the functionality works.
#
# (These scripts are usually employed as part of national and industry certification processes.)
# *****************************************************************************************************
#
# Functions:
#   ???
#   (FILL IN THE DETAILS)
#
#
#
# ChangeLog:    Cody Bogausch
#           (cody.bogausch@sunycgcc.edu)
#
#
# Version
#   April 11, 2024
#
###############################################################################

import random
import time
import copy

from Sorting import Sorting


def timed_test(algorithm: Sorting, *args) -> None:
    """
    Execute an arbitrary sorting algorithm then calculate and display the time elapsed during the sort
    @param algorithm: Type of sorting algorithm from the Sorting class
    @return: None
    """

    start_time = time.time()

    print(f"Time is: {start_time}")

    algorithm(*args)

    print(f"Time elapsed: {time.time() - start_time}")


def create_random_list(size: int) -> list[int]:
    # Empty container
    lyst = list()

    # Iterate over arbitrary size value
    for _ in range(size):
        # Append a random value for each index in container
        lyst.append(random.randint(0, 100))

    # return random list
    return lyst


def main() -> None:
    """
    Tester for Sorting.py
    @return: None
    """
    # 1) Print headers for each algorithm,
    # which inform the person who runs the test when each algorithm is running,
    # and what type of data is being used (given lists, or random input)—
    # these print statements will be output to the terminal.

    # 2) For input, you will need these 7 python lists:
    # (The final sorted lists will be printed to the terminal.)

    testList1 = [54, 38, 10, 44, 85]
    testList2 = [94, 16, 33, 29, 100]
    testList3 = [11, 12, 13, 14, 15, 16, 17]
    testList4 = [7, 7, 7, 7, 7]
    testList5 = [12, 84, 73, 11, 88]
    testList6 = [19, 89, 17, 31, 56, 18, 34, 68, 77, 9, 21, 66, 48, 78, 73, 87, 2, 11, 34]
    testList7 = [17, 100, 15, 32, 54, 19, 89, 78, 87, 7, 31, 56, 41, 100, 83, 95, 7, 21, 100]

    # b) Use the random package to make a random list of 100 integers,
    # a random list of 500 integers, and a random list of 1000 integers.
    # That means that the list indexes are 0-99, 0-499, and 0-999.

    testList8 = create_random_list(100)
    testList9 = create_random_list(500)
    testList10 = create_random_list(1000)

    # 3) Sort your 10 arrays,
    # and use the time package to calculate the time taken to complete the sorting for the 7 given arrays,
    # and your 3 random arrays.
    # Print the time after each sorting operation is completed.

    print("")
    timed_test(Sorting.bubbleSort, copy.copy(testList1))

    print("Selection Sort:")
    timed_test()


if __name__ == '__main__':
    main()
