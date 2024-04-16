#!/usr/bin/env python3
# coding: utf-8

###############################################################################
# This class is a lab assignment
# *****************************************************************************************************
#  Sorting.py       
#  This class should have: selectionSort, insertionSort, bubbleSort, quickSort, 
#      and mergeSort methods which implement the coresponding sorting methods 
#      DISPLAY the the comparision, swap, and pivot elements as well as the merging 
# *****************************************************************************************************
#
# Functions:
#   ???
#   (FILL IN THE DETAILS)
#
#
#
# ChangeLog: C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#           Cody Bogausch
#   (cody.bogausch@sunycgcc.edu)
#
# Version
#   April 11, 2024
#
###############################################################################

__author__ = "C. Mikijanic, Cody Bogausch"
__version__ = 1.0000000001


class Sorting:

    # -----------------------------------------------------------------
    #  Description:
    #   Helper function.
    #   Used in ALL sorting algorithms in this module.
    #   Swaps two elements in the specified list. 
    #
    #  Input:    
    #   ???
    #  
    #  Output:
    #   ???
    # -----------------------------------------------------------------
    @staticmethod
    def swap(data, index1, index2):
        data[index1], data[index2] = data[index2], data[index1]

    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of integers using the selection
    #   sort algorithm.
    #
    #  Input:    
    #   ???
    #  
    #  Output:
    #   ???
    # -----------------------------------------------------------------
    @staticmethod
    def selectionSort(data):

        print(data)

        for i in range(len(data)):

            for j in range(len(data)):

                if data[i] > data[j]:

                    Sorting.swap(data, i, j)

        print(data)

    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of objects using an insertion
    #   sort algorithm. 
    #
    #  Input:    
    #   ???
    #  
    #  Output:
    #   ???
    # -----------------------------------------------------------------
    @staticmethod
    def insertionSort(data):

        print(data)

        for i in range(len(data)):

            j = i - 1

            temp = data[i]

            while data[i] < data[j] and j > 0:

                Sorting.swap(data, j, j+1)

                j -= 1

            data[j+1] = temp

        print(data)

        # -----------------------------------------------------------------

    #  Description:
    #   Sorts the specified list of objects using a bubble sort
    #   algorithm. 
    #
    #  Input:    
    #   ???
    #  
    #  Output:
    #   ???
    # -----------------------------------------------------------------
    @staticmethod
    def bubbleSort(data):

        print(data)

        for i in range(len(data) - 2):

            for j in range(len(data) - 1):

                if data[j + 1] < data[j]:

                    Sorting.swap(data, j + 1, j)

        print(data)
    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of objects using the quick sort
    #   algorithm. 
    #
    #  Input:    
    #   ???
    #  
    #  Output:
    #   ???
    # -----------------------------------------------------------------

    def quickSort(data, minimum, maximum):
        "Complete this function, add inline comments, and finish the function description..."

    # -----------------------------------------------------------------
    #  Description:
    #   Helper function. 
    #   Creates the partitions needed for quick sort. 
    #
    #  Input:    
    #   ???
    #  
    #  Output:
    #   ???
    # -----------------------------------------------------------------
    def partition(data, minimum, maximum):
        "Complete this function, add inline comments, and finish the function description..."

    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of objects using the merge sort
    #   algorithm. 
    # -----------------------------------------------------------------

    def mergeSort(data, minimum, maximum):
        "Complete this function, add inline comments, and finish the function description..."

    # -----------------------------------------------------------------
    #  Description:
    #   Helper function, breaks down merge sort into a recursive call
    #   of the first and second half of the sublist. These are
    #   separated in the 2 recursive calls arithmetically. 
    #
    #  Input:    
    #   ???
    #  
    #  Output:
    #   ???
    # -----------------------------------------------------------------
    def mergeSortHelper(data, copyBuffer, low, high):
        "Complete this function, add inline comments, and finish the function description..."

    # -----------------------------------------------------------------
    #  Description:
    #   Helper function for mergeSortHelper. Performs the main merge.
    #   Sorts the specified list of objects using the merge behavior of
    #   the merge sort algorithm. 
    #
    #  Input:    
    #   ???
    #  
    #  Output:
    #   ???
    # -----------------------------------------------------------------
    def merge(data, copyBuffer, low, middle, high):
        "Complete this function, add inline comments, and finish the function description..."
