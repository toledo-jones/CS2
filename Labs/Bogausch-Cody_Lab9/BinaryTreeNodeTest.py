#!/usr/bin/env python3
# coding: utf-8

###############################################################################
# This is a tester file for BinaryTreeNode
# 
# A BinaryTreeNode provides a node for a binary tree. Each node 
# contains a piece of data and references to a left and right child. 
# The references to children may be None to indicate
# that there is no child. The reference stored in a node can also be None.
#
# DATA fields of the BinaryTreeNode class:
#  1. Each node has one integer, stored in the instance variable data.
#  2. The instance variables left and right are references to the node's 
#         left and right children.
#
# Functions:
#   main - Mainline for the program
#
# ChangeLog: C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
#
# Version
#   January 1, 2024
#
##############################################################################/

__author__ = "C. Mikijanic"
__version__ = 1.0

# BinaryTreeNode class used to build trees
from BinaryTreeNode import *


#######################################################################
# This class is a tester for BinaryTreeNode 
######################################################################/
# use BinaryTreeNode, BinarySearchTree 

class BinarySearchTree_Test:

    def main():
        # CLASS VARIABLES

        # Binary Search Trees used during the process  
        treeA = None
        treeB = None

        # Low and high number limits used during random integer generation
        randomLimit_low = 0
        randomLimit_high = 101

        # Pre-set of integer lists used during creation of Trees in Phase A 
        # These have been created to trigger certain conditions
        setOfInts = [32, 91, 50, 22, 49, 65, 49, 68, 67, 96]

        ###############################################################################
        # A) Create trees using Non-Random Data:
        ###############################################################################

        print("A) NON-Random:")
        print("===========")

        # GenerateTrees
        print("Insert Pre-set Integers: ")
        # Create variable for BinarySearchTree
        treeA = BinaryTreeNode(setOfInts[0])

        # Iterative traversal/adding binary tree nodes 
        # (Showing that this is possible - for demonstration's sake)
        # Set cursor
        cursor = treeA
        # Since we are going through a partial list, use a for loop and range
        # Start at the second element in the list
        for i in range(1, len(setOfInts)):
            # Set end of process indicator
            endProcess = False
            # Data has not been inserted  
            while (not endProcess):
                # If the incoming data is less than cursor data
                if (setOfInts[i] <= cursor.getData()):
                    # If there is no left child
                    if (cursor.getLeft() == None):
                        # Create a new node for the left child
                        cursor.setLeft(BinaryTreeNode(setOfInts[i], None, None))
                        # Reset the cursor
                        cursor = treeA
                        # Indicate end of process
                        endProcess = True
                    else:
                        # Otherwise, shift cursor to the left child    
                        cursor = cursor.getLeft()
                else:
                    # If the incoming data is equal to than cursor data
                    if (cursor.getRight() == None):
                        # Create a new node for the right child
                        cursor.setRight(BinaryTreeNode(setOfInts[i], None, None))
                        # Reset the cursor
                        cursor = treeA
                        # Indicate end of process
                        endProcess = True
                    else:
                        # Otherwise, Shift cursor to the right child
                        cursor = cursor.getRight()
        print("Completed.")
        print("")

        # Display TreeA - height
        print("treeA (height): ")
        h = treeA.height()
        print("The height of the tree is:", h)
        print("")

        # Display TreeA - print full tree
        print("treeA (print full tree): ")
        treeA.print(h)
        print("")

        # Display TreeA - preorder
        print("treeA (preorder): ")
        treeA.preorderPrint()
        print("", end="\n\n")
        # Display TreeA - inorder
        print("treeA (inorder): ")
        treeA.inorderPrint()
        print("", end="\n\n")
        # Display TreeA - postorder
        print("treeA (postorder): ")
        treeA.postorderPrint()
        print("", end="\n\n")

        # Get root in the tree
        print("treeA root: ", treeA.getData())
        print("Visual check through preorder print, (first item):")
        treeA.preorderPrint()
        print("", end="\n\n")

        # Get left child's data
        print("treeA left child's data: ", treeA.getLeft().getData())
        print("Visual check through preorder print, (second item):")
        treeA.preorderPrint()
        print("", end="\n\n")

        # Get right child's data
        print("treeA left child's data: ", treeA.getRight().getData())
        print("Visual check through preorder print, (third item):")
        treeA.preorderPrint()
        print("", end="\n\n")

        # Get leftmost (lowest number) in the tree
        print("treeA leftmost (lowest number): ", treeA.getLeftmostData())
        print("Visual check through inorder print, (first item):")
        treeA.inorderPrint()
        print("", end="\n\n")

        # Remove leftmost (lowest number) in the tree
        print("treeA Remove leftmost (lowest number), checked through inorder print: ")
        treeA.removeLeftmost()
        treeA.inorderPrint()
        print("", end="\n\n")

        # Get rightmost (highest number) in the tree
        print("treeA rightmost (lowest number): ", treeA.getRightmostData())
        print("Visual check through inorder print (last item):")
        treeA.inorderPrint()
        print("", end="\n\n")

        # Remove rightmost (highest number) in the tree
        print("treeA Remove rightmost (highest number), checked through inorder print: ")
        treeA.removeRightmost()
        print("Visual check through inorder print (last item):")
        treeA.inorderPrint()
        print("", end="\n\n")

        # Set the left child of the root
        treeA.setLeft(BinaryTreeNode(1, None, None))
        print("treeA left child's data retrieved: ", treeA.getLeft().getData())
        print("Visual check through inorder print, (first item):")
        treeA.inorderPrint()
        print("", end="\n\n")

        # Change the left child of the root
        treeA.getLeft().setData(2)
        print("treeA left child's data changed: ", treeA.getLeft().getData())
        print("Visual check through inorder print, (first item):")
        treeA.inorderPrint()
        print("", end="\n\n")

        # Change the right child of the root
        treeA.getRight().setData(101)
        print("treeA right child's data changed: ", treeA.getRight().getData())
        print("Visual check through inorder print, (third item):")
        treeA.inorderPrint()
        print("", end="\n\n")

        # Copy the entire tree (copy is treeB)
        print("Copy treeA = treeB:")
        treeB = BinaryTreeNode.treeCopy(treeA)
        print("Visual check through inorder print (should be same data as treeA):")
        treeB.inorderPrint()
        print("", end="\n\n")

        # Get size of tree B
        print("Size of treeB:", BinaryTreeNode.treeSize(treeB))
        print("")

    if __name__ == "__main__":
        main()
