#!/usr/bin/env python3
# coding: utf-8

##By: Christine Mikijanic
## File: LinkedSeq.py, based on DoubleLinkedSeq from edu.colorado.collections
## This is an assignment for students to complete


###############################################################################
# This class is a homework assignment
# A LinkedSeq is a collection of elements.
# The sequence can have a special "current element," which is specified and 
# accessed through four methods that are not available in the sequence class 
# (start, getCurrent, advance and isCurrent).
#
# Limitations:
#   Beyond the Integer.MAX_VALUE value of integers elements, the size method
#   does not work.
#
# ChangeLog: Michael Main 
#   (main@colorado.edu)
#            C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#            Cody Bogausch
#   (cody.bogausch@sunycgcc.edu)
# Note:
#   This file contains only blank implementations ("stubs")
#   because this is a Programming Project for student.
#
# Version
#   January 1, 2024
###############################################################################
import copy
from Node import Node

__author__ = "Cody Bogausch"
__version__ = "0.999999989"


class LinkedSeq:
    """

    Ran out of time, unfortunately.

    """

    ###
    # Initialize an empty sequence.
    # Argument: - none
    # Postcondition:
    #   This sequence is empty.
    ###   
    def __init__(self):
        self.head: (Node or None) = None
        self.currentElement: (Node or None) = None
        self.manyNodes: int = 0

    ###
    # Add a new element to this sequence, after the current element. 
    # Argument: element
    #   the new element that is being added
    # Postcondition:
    #   A new copy of the element has been added to this sequence.
    #
    #   If there was a current element, then the new element is placed after the current element.
    #
    #   If there was no current element, then the new element is placed at the end of the sequence.
    #
    #   In all cases, the new element becomes the new current element of this sequence.
    #
    # Exception: MemoryError
    #   Indicates insufficient memory for a new node.
    ##/
    def addAfter(self, element):

        # Attempt to add Node to sequence
        try:

            # Sequence has a current element
            if self.isCurrent():

                # Create a node with the data element after the current node
                self.currentElement.addNodeAfter(element)

                # Move the currentElement to the link made in the previous step
                self.currentElement = self.currentElement.link

            # Sequence does not have a current element
            else:
                node = Node(element)

                if self.head is not None:
                    node.setLink(self.head)

                # Head data becomes data element
                self.head = node

                # Current element becomes head
                self.currentElement = self.head

            # Increment node count
            self.manyNodes += 1

        # Insufficient memory condition
        except MemoryError as e:
            print(e)

    ###
    # Add a new element to this sequence, before the current element. 
    # Argument: element
    #   the new element that is being added
    # Postcondition:
    #   A new copy of the element has been added to this sequence. If there was
    #   a current element, then the new element is placed before the current
    #   element. If there was no current element, then the new element is placed
    #   at the start of the sequence. In all cases, the new element becomes the
    #   new current element of this sequence. 
    # Exception: MemoryError
    #   Indicates insufficient memory for a new node.
    ##/
    def addBefore(self, element):
        try:
            #
            if self.isCurrent():

                #
                cursor = self.head

                #
                while cursor.link is not self.currentElement:
                    #
                    cursor = cursor.link

                #
                cursor.addNodeAfter(element)

                #
                self.currentElement = cursor.link
            #
            else:

                #
                new_node = Node(element, self.head)

                #
                self.head = new_node

                #
                self.currentElement = new_node

            #
            self.manyNodes += 1

        except AttributeError:
            self.head = Node(element)
            self.currentElement = self.head

    ###
    # Place the contents of another sequence at the end of this sequence.
    # Argument: addend
    #   a sequence whose contents will be placed at the end of this sequence
    # Precondition:
    #   The parameter, addend, is not None. 
    # Postcondition:
    #   The elements from addend have been placed at the end of 
    #   this sequence. The current element of this sequence remains where it 
    #   was, and the addend is also unchanged.
    # Exception: TypeError
    #   Indicates that addend is None. 
    # Exception: MemoryError
    #   Indicates insufficient memory to increase the size of this sequence.
    ##/
    def addAll(self, addend):

        #
        length = self.manyNodes

        #
        tail = self.head.listPosition(length)

        #
        tail.setLink(addend.head)

        #
        added_length = addend.head.listLength(addend.head)

        #
        self.manyNodes += added_length

    ###
    # Move forward, so that the current element is now the next element in
    # this sequence.
    # Argument: - none
    # Precondition:cursor = cursor.getLink()
    #   isCurrent() returns True. 
    # Postcondition:
    #   If the current element was already the end element of this sequence 
    #   (with nothing after it), then there is no longer any current element. 
    #   Otherwise, the new element is the element immediately after the 
    #   original current element.
    # Exception: TypeError
    #   Indicates that there is no current element, so 
    #   advance may not be called.
    ##/
    def advance(self):

        #
        try:

            #
            self.currentElement = self.currentElement.getLink()

        #
        except TypeError:

            #
            print("There is no current element, so advance may not be called.")

        except AttributeError:

            self.currentElement = None

    ###
    # Generate a copy of this sequence.
    # Argument: - none
    # Returns
    #   The return value is a copy of this sequence. Subsequent changes to the
    #   copy will not affect the original, nor vice versa. Note that the return
    #   value must be type cast to a FloatLinkedSeq before it can be used.
    # Exception: MemoryError
    #   Indicates insufficient memory for creating the clone.
    ##/ 
    def clone(self):

        #
        holder = None

        #
        try:

            #
            holder = copy.deepcopy(self)

        #
        except MemoryError:

            #
            print("Deep copy could not be created")

        #
        return holder

    ###
    # Create a new sequence that contains all the elements from one sequence
    # followed by another.
    # Argument: s1
    #   the first of two sequences
    # Argument: s2
    #   the second of two sequences
    # Precondition:
    #   Neither s1 nor s2 is None.
    # Returns
    #   a new sequence that has the elements of s1 followed by the
    #   elements of s2 (with no current element)
    # Exception: TypeError.
    #   Indicates that one of the Argument: is None.
    # Exception: MemoryError
    #   Indicates insufficient memory for the new sequence.
    ##/   
    @staticmethod
    def catenation(s1, s2):

        try:

            #
            s1_copy = s1.head.listCopy()

            #
            s2_copy = s2.head.listCopy()

            #
            linked_sequence = LinkedSeq()

            #
            linked_sequence.addAll(s1_copy)

            #
            linked_sequence.addAll(s2_copy)

        except TypeError:
            print("addend is None.")

        except MemoryError:
            print("Insufficient memory to increase the size of this sequence.")

    ###
    # Accessor method to get the current element of this sequence. 
    # Argument: - none
    # Precondition:
    #   isCurrent() returns True.
    # Returns
    #   the current capacity of this sequence
    # Exception: TypeError
    #   Indicates that there is no current element, so 
    #   getCurrent may not be called.
    ##/
    def getCurrent(self):

        #
        try:

            #
            if self.isCurrent():
                #
                return self.currentElement

        #
        except TypeError:

            #
            print("Error: There is no current element, so getCurrent may not be called.")

        #
        return None

    ###
    # Accessor method to determine whether this sequence has a specified 
    #    current element that can be retrieved with the 
    #    getCurrent method. 
    # Argument: - none
    # Returns
    #   True (there is a current element) or False (there is no current element at the moment)
    ##/
    def isCurrent(self):
        # If current element is not None, return True
        return self.currentElement is not None

    ###
    # Remove the current element from this sequence.
    # Argument: - none
    # Precondition:
    #   isCurrent() returns True.
    # Postcondition:
    #   The current element has been removed from this sequence, and the 
    #   following element (if there is one) is now the new current element. 
    #   If there was no following element, then there is now no current 
    #   element.
    # Exception: TypeError
    #   Indicates that there is no current element, so 
    #   removeCurrent may not be called. 
    ##/
    def removeCurrent(self):

        #
        try:

            #
            if self.isCurrent():
                #
                self.currentElement = self.currentElement.getLink()

        #
        except TypeError as e:

            # Debug
            print(e)
            print("There is no current element, so removeCurrent may not be called.")

    ###
    # Determine the number of elements in this sequence.
    # Argument: - none
    # Returns
    #   the number of elements in this sequence
    ##/ 
    def size(self):
        return self.head.listLength(self.head)

    ###
    # Set the current element at the front of this sequence.
    # Argument: - none
    # Postcondition:
    #   The front element of this sequence is now the current element (but 
    #   if this sequence has no elements at all, then there is no current 
    #   element).
    ##/ 
    def start(self):
        self.head = self.currentElement

    ###
    # Prints the target sequence to the terminal.
    # Argument: - none
    # Postcondition:
    #   Prints out all of the elements in the sequence to the terminal.
    #   No change to sequence elements.
    def print(self):

        print("length = ", self.manyNodes)
        if self.isCurrent() is True:

            print("current element = ", self.getCurrent())

        else:

            print("there is no current element")

        print("elements:  ", end="")
        if self.manyNodes != 0:
            current = self.head
            while current is not None:
                print(" " + str(current.getData()), end="")
                current = current.getLink()

        print("")
        print("")
