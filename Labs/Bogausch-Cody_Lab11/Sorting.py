#!/usr/bin/env python3
# coding: utf-8

###############################################################################
# This class is a lab assignment
# *****************************************************************************************************
#  Sorting.py       
#  This class should have: selectionSort, insertionSort, bubbleSort, quickSort, 
#      and mergeSort methods which implement the corresponding sorting methods
#      DISPLAY the the comparison, swap, and pivot elements as well as the merging
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
    #   data (list) list of items (any)
    #   index1 (int) index of data to swap
    #   index2 (int) index of place to move data to
    #  
    #  Output:
    #   None
    # -----------------------------------------------------------------

    @staticmethod
    def swap(data, index1, index2):

        # Swap data at index one and data at index two
        data[index1], data[index2] = data[index2], data[index1]

    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of integers using the selection
    #   sort algorithm.
    #
    #  Input:
    #   data (list) list of items (any)
    #  
    #  Output:
    #   None
    # -----------------------------------------------------------------

    @staticmethod
    def selectionSort(data):

        # Iterate over outer each item in list (outer)
        for outer in range(len(data)):

            # Iterate over each item in list (inner) this is where the sorting will occur
            for inner in range(len(data)):

                # If data at inner index is less than data at outer index
                if data[outer] > data[inner]:

                    # Swap data of inner and outer
                    Sorting.swap(data, outer, inner)


    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of objects using an insertion
    #   sort algorithm. 
    #
    #  Input:    
    #   data (list) of values (any)
    #  
    #  Output:
    #   None
    # -----------------------------------------------------------------

    @staticmethod
    def insertionSort(data):

        # Iterate over the list
        for i in range(len(data)):

            # Temporarily store the data at outer index
            stored_data = data[i]

            # Inner index is set to outer index minus one
            j = i - 1

            # Iterate over the list again starting
            while (j >= 0) and (data[j] < data[i]):

                # Swap this inner with the one next to it
                Sorting.swap(data, j + 1, j)

                # Move the index variable back one
                j -= 1

            #
            data[j + 1] = stored_data

    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of objects using a bubble sort
    #   algorithm. 
    #
    #  Input:    
    #   data (list) of values (any)
    #  
    #  Output:
    #   None
    # -----------------------------------------------------------------

    @staticmethod
    def bubbleSort(data):

        # Iterate over the outer, going only to the length of data - two
        for outer in range(len(data) - 2):

            # Iterate over inner list, going only to the length of data - one
            for inner in range(len(data) - 1):

                # If the next value is less than the current one
                if data[inner + 1] < data[inner]:

                    # Swap the next value with the current
                    Sorting.swap(data, inner + 1, inner)



    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of objects using the quick sort
    #   algorithm. 
    #
    #  Input:    
    #   data (list) of values (any)
    #   minimum unused arg?
    #   maximum unused arg?
    #  
    #  Output:
    #   None?
    # -----------------------------------------------------------------

    @staticmethod
    def quickSort(data, minimum, maximum):

        # Call recursive helper function with the minimum as zero and the maximum as the max index
        Sorting.partition(data, minimum=0, maximum=len(data) - 1)

    # -----------------------------------------------------------------
    #  Description:
    #   Helper function. 
    #   Creates the partitions needed for quick sort. 
    #
    #  Input:    
    #   data (list) of values (any)
    #   minimum
    #   maximum
    #
    #  Output:
    #   None
    # -----------------------------------------------------------------

    @staticmethod
    def partition(data, minimum, maximum):

        # If the difference between the maximum and minimum is greater than zero
        if (maximum - minimum) > 0:

            # Store pivot
            pivot = data[minimum]

            # Save minimum and maximum
            left_location = minimum
            right_location = maximum

            # While the left location is less than or equal to the right location
            while left_location <= right_location:

                # While data in the left location is less than pivot
                while data[left_location] < pivot:

                    # Increment left location index
                    left_location += 1

                # While data in the right location is greater than the pivot
                while data[right_location] > pivot:

                    # Decrement right location index
                    right_location -= 1

                    # If the left is less than or equal to the data on the right
                if left_location <= right_location:

                    # Swap
                    Sorting.swap(data, left_location, right_location)

                    # Increment left index
                    left_location += 1

                    # Decrement right index
                    right_location -= 1

            # Recurse with the minimum and right location
            Sorting.partition(data, minimum=minimum, maximum=right_location)

            # Recurse with the left_location and the maximum
            Sorting.partition(data, minimum=left_location, maximum=maximum)

    # -----------------------------------------------------------------
    #  Description:
    #   Sorts the specified list of objects using the merge sort
    #   algorithm. 
    # -----------------------------------------------------------------

    @staticmethod
    def mergeSort(data, minimum, maximum):

        # If minimum is the same as maximum
        if minimum == maximum:

            # Return early
            return

        # Create an array of size len(data) filled with zeroes
        copy_buffer = [0 for _ in range(len(data))]

        # Call recursive helper, passing on all args and copy_buffer
        Sorting.mergeSortHelper(data, copy_buffer, minimum, maximum)\


    # -----------------------------------------------------------------
    #  Description:
    #   Helper function, breaks down merge sort into a recursive call
    #   of the first and second half of the sublist. These are
    #   separated in the 2 recursive calls arithmetically. 
    #
    #  Input:    
    #   data: (list) of values (any)
    #   copyBuffer: (list) of values to be copied
    #   low: minimum value to sort
    #   high: maximum value to sort
    #
    #  Output:
    #   None
    # -----------------------------------------------------------------

    @staticmethod
    def mergeSortHelper(data, copyBuffer, low, high):

        # If low is less than high
        if low < high:

            # Create a middle which is the low plus the high
            middle = (low + high) // 2

            # Recurse with low and middle
            Sorting.mergeSortHelper(data, copyBuffer, low, middle)

            # Recurse with middle +1 and high
            Sorting.mergeSortHelper(data, copyBuffer, middle+1, high)

            # Call the merge function with low middle and high
            Sorting.merge(data, copyBuffer, low, middle, high)

    # -----------------------------------------------------------------
    #  Description:
    #   Helper function for mergeSortHelper. Performs the main merge.
    #   Sorts the specified list of objects using the merge behavior of
    #   the merge sort algorithm. 
    #
    #  Input:    
    #   data: (list) of values (any)
    #   copyBuffer: (list) of values (any) to be copied
    #   low: minimum value to sort
    #   middle: middle value between low and high
    #   high: maximum value to sort
    #  
    #  Output:
    #   None
    # -----------------------------------------------------------------

    @staticmethod
    def merge(data, copyBuffer, low, middle, high):

        # Index one is the low
        index_one = low

        # Index two is the middle plus one
        index_two = middle + 1

        # Iterate over each index in the range low to high plus one
        for i in range(low, high+1):

            # If index one is greater than the middle
            if index_one > middle:

                # The data in copyBuffer at the index becomes data[index_two]
                copyBuffer[i] = data[index_two]

                # Increase index two
                index_two += 1

            # If index_two is greater than the high
            elif index_two > high:

                # The data in copyBuffer at the index becomes data[index_one]
                copyBuffer[i] = data[index_one]

                # Increase index_one
                index_one += 1

            # If the information at index_one in data is less than the information in data at index_two
            elif data[index_one] < data[index_two]:

                # The data in copyBuffer at the index becomes data[index_one]
                copyBuffer[i] = data[index_one]

                # Increase index_one
                index_one += 1

            # Other
            else:

                # The data in copyBuffer[index_two] becomes data[index_two]
                copyBuffer[i] = data[index_two]

                # Increment index two
                index_two += 1

        # For each index in the range low to high plus one
        for i in range(low, high+1):

            # Copy sorted items back to proper position in data
            data[i] = copyBuffer[i]

