#!/usr/bin/env python3
# coding: utf-8

###############################################################################
# This class is a lab assignment.
# 
# A BinarySearchTree is a binary tree. Each node in the tree
# contains a piece of data and references to a left and right child. 
# The references to children may be None to indicate
# that there is no child. 
# A tree can be empty (no nodes), have one node (root), or many nodes.
#
# DATA fields of the BinaryTreeNode class:
#  1. Each node has one integer, stored in the instance variable data.
#  2. The instance variables left and right are references to the node's 
#         left and right children.
#
# Functions:
#   ???
#
# ChangeLog: C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#
# Version
#   January 1, 2024
#
##############################################################################/

__author__ = "C. Mikijanic, Cody Bogausch"
__version__ = 1.01

# BinaryTreeNode class used to build BinarySearchTrees
from BinaryTreeNode import *


class BinarySearchTree(BinaryTreeNode):

    def __init__(self, newRoot=None):

        # Initialize attributes
        self.setRoot(newRoot)

    ###
    # Description: 
    #    Change or set ROOT of the tree to a given node(newRoot)
    ###
    def setRoot(self, newRoot):
        self.root = newRoot

    ###
    # Description: 
    #    Get or return the ROOT of the tree
    ###
    def getRoot(self):
        return self.root

    def preorderPrint(self):
        self.getRoot().preorderPrint()

    def inorderPrint(self):
        self.getRoot().inorderPrint()

    def postorderPrint(self):
        self.getRoot().postorderPrint()

    def print(self):
        self.getRoot().print()

    ###
    # Description: 
    #    ADD or Insert a new node (element) into this TREE (Helper function declared outside)
    #    DOES NOT ALLOW DUPLICATES !!!    
    ###
    def add(self, data):

        # Set root to the new value
        self.setRoot(

            # Root will be the return value of the inner, static __add() method
            BinarySearchTree.__add(

                # data to be placed inside the new node
                data,

                # Current root, used for finding position
                self.getRoot()
            )
        )

    def __add(data, cursor):

        # Base Case: Cursor is None
        if cursor is None:
            # Create new tree node with data and no links
            return BinaryTreeNode(data)

        # Arg data is LESS than cursor data
        if data < cursor.data:

            # Recurse, checking the next deeper layer for greater than or less than
            cursor.setLeft(BinarySearchTree.__add(data, cursor.getLeft()))

        # Arg data is GREATER than cursor data
        elif data > cursor.data:

            # Recurse, checking the next layer for greater than, less than or the same.
            cursor.setRight(BinarySearchTree.__add(data, cursor.getLeft()))

        #
        return cursor

    ###
    # Description: 
    #    REMOVE a node which has its DATA = target in this tree. (Helper function declared INSIDE)
    # Precondition: 
    #   the target tree must have a root node
    # Parameters: 
    #   (BinaryTree) self, (BinaryTreeNode) target - the data of the node to be removed from the tree
    # Post condition:
    #    If "target" was found in the tree, then the node containing "target" is 
    #    removed and the method returns True. If no "target" is found then the method returns false. 
    # Returns: N/A
    ###
    def remove(self, target):
        def __remove(_target, cursor):

            # Alias for target data
            data = _target.getData()

            # Target data matches cursor
            if data == cursor.getData():

                # No Child Case:
                if cursor.isLeaf():
                    return None

                if cursor.getLeft() is not None and cursor.getRight() is None:
                    pass

                if cursor.getRight() is not None:
                    pass

            # Arg data is LESS than cursor data
            if data < cursor.getData():

                # Recurse, checking the next deeper layer for greater than or less than
                cursor.setLeft(__remove(data, cursor.getLeft()))

            # Arg data is GREATER than cursor data
            elif data > cursor.getData():

                # Recurse, checking the next layer for greater than, less than or the same.
                cursor.setRight(__remove(data, cursor.getLeft()))

            #
            return cursor

        self.setRoot(__remove(target, self.getRoot()))
        raise NotImplementedError("Not Finished")

    ###
    # Description:
    #   Check to see if a particular DATA(target) is in this tree.
    # Parameters: 
    #   (BinarySearchTree) self, (BinaryTreeNode) target - the element that needs to be counted
    # Returns: 
    #   bool if target is in tree
    ###
    def contains(self, target):
        "This function is not completed..."

    def __contains(target, cursor):
        "This function is not completed..."

    ###
    # Description:
    #   Determine the SIZE of the tree or the number of nodes in this tree. 
    # Parameters: 
    #   (BinaryTree) self
    # Returns: 
    #   the number of elements in this tree, if the tree is empty, returns 0
    # Note: Do not use super() or treeSize from BinaryTreeNode
    ###
    def size(self):

        # Wrapper for BinarySearchTree.__size()
        BinarySearchTree.__size(self)

    def __size(cursor):

        # Initialize count variables (?)
        left_size = 0
        right_size = 0

        # Check left side of sub-tree
        if cursor.getLeft() is not None:

            # Recurse down into left tree, extracting the height
            left_size = BinaryTreeNode.__size(cursor.getLeft())

        # Check right side of the sub-tree
        if cursor.getRight() is not None:

            # Recurse down into right tree, extracting the height
            right_size = BinarySearchTree.__size(cursor.getRight())

        # Return two sizes plus one for this Node
        return 1 + left_size + right_size

    ###
    # Description:
    #  Create a new tree that contains all the elements from two other trees.
    # Parameters: 
    #  b1 the first of two trees
    # Parameters: 
    #  b2 the second of two trees
    # Precondition:
    #  Neither b1 nor b2 is None.
    # Returns: 
    #  the union of b1 and b2
    ### 
    def union(b1, b2):

        # Join two trees using the _add function and the BinaryTreeNode.treeCopy()
        return BinaryTreeNode.treeCopy(b1).__addTree(BinaryTreeNode.treeCopy(b2))

    ###
    # Description:
    #   Add the contents of another tree to this tree.
    # Parameters: Precondition: addend
    #   a tree whose contents will be added to this tree
    # Precondition: 
    #   The parameter, addend, is not None.
    # Postcondition: 
    #   The elements from addend have been added to this tree.
    ###
    def addAll(self, addend):
        # Wrapper?
        # Or do these two methods have different functionality?
        raise NotImplementedError("?")

    ###
    # Description:    
    # Add the contents of another binary search tree to this tree.
    # Parameters: addroot
    #   the root of a binary search tree whose contents will be added to this tree
    # Postcondition: 
    #   The elements from the binary search tree specified by
    #   addroot have been added to this tree.
    ###
    def __addTree(self, addroot):

        #
        if addroot is None:
            pass

        #
        if addroot.getRight() is not None:
            pass

        #
        if addroot.getLeft() is not None:
            pass

