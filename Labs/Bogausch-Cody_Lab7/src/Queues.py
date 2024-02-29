#!/usr/bin/env python3
# coding: utf-8
##By: Professor Mikijanic

###############################################################################
# The Queue class creates a queue structure that can be used to perform
# basic queueing tasks. It uses Linked List nodes as the base. 
#
# Note:
#   Lists of nodes can be made of any length, limited only by the amount of
#   free memory in the heap. 
#
#
# ChangeLog: C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#            Cody Bogausch
#   (cody.bogausch@sunycgcce.edu)
#
# Version
#   January 1, 2024
#
##############################################################################/

__author__ = "C. Mikijanic, Cody Bogausch"
__version__ = 1.0

from Node import Node


class Queue:

    ###
    # Initialize an empty queue.
    # Argument: 
    #   None
    # Postcondition:
    #   Queue created, this queue is empty.
    # Exception: MemoryError
    #   Indicates insufficient memory for the new queue.    
    ### 

    def __init__(self):

        # Attempt to create a new Queue
        try:

            # Empty queue condition:
            self.head = None
            self.tail = None

        # Handle empty memory condition
        except MemoryError:
            print("Insufficient memory for a new Queue.")

    ###
    # Add a new element to the queue.
    # Argument: 
    #    data - the element data to be added
    # Postcondition:
    #   Queue has been increased by one item.
    # Exception: MemoryError
    #   Indicates insufficient memory for the new sequence.    
    ### 
    def enqueue(self, data):

        # Add a node at the end of the queue
        try:

            # Head is none
            if self.head is None:

                # Create a new head
                self.head = Node(data)

                # End of line is also the beginning
                self.tail = self.head

            else:

                # Line already has a beginning
                self.tail.addNodeAfter(data)

                # Make our new node the end
                self.tail = self.tail.getLink()

        # Need more memory
        except MemoryError:
            print("Insufficient memory for a new sequence")

    ###
    # Remove an element from the queue.
    # Argument: 
    #    None
    # Postcondition:
    #   Queue has been decreased by one item.
    # Exception: TypeError
    #   Indicates that there is no elements, so 
    #   dequeue may not be called.    
    ### 
    def dequeue(self):
        try:

            # Create a cursor starting at the first in line, the head
            cursor = self.head

            # Link must contain something to be shifted up in list
            if self.head.getLink() is not None:

                # Move head down to next
                self.head = self.head.getLink()

                # Exit
                return cursor

            # Link does not exist, return head and set the head to None
            else:

                # Set head to none
                self.head = None

                # Exit
                return cursor



        #
        except TypeError:
            print("There are no elements in the Queue")

    ###
    # Check to see if the queue is empty.
    # Argument: 
    #    None
    # Returns:
    #   True/False - if the queue is empty or not.
    ### 
    def isEmpty(self):

        # Head is None
        if self.head is None:

            # Yes
            return True

        # Head is not None
        else:

            # No
            return False

    ###
    # Print out a string representation of the queue
    # Argument: 
    #    None
    # Returns:
    #   A string containing all of the elements in the queue
    ### 
    def __str__(self):

        # Initialize an empty string
        string_representation = ''

        # Handle empty sequence condition
        if self.head is None:
            return string_representation

        # Cursor points to head
        cursor = self.head

        # Iterate through queue
        while cursor.link is not None:

            # Append current cursor data to string representation
            string_representation += " " + str(cursor.data)

            # Move the cursor
            cursor = cursor.link

        # Add final Node
        string_representation += " " + str(cursor.data)

        # Return string with leading spaces removed
        return string_representation.strip()
