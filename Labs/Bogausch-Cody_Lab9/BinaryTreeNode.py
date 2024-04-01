#!/usr/bin/env python3
# coding: utf-8

###############################################################################
# This class is a lab assignment.
# 
# A BinaryTreeNode provides a node for a binary tree. Each node 
# contains a piece of data and references to a left and right child. 
# that there is no child. The reference stored in a node can also be None.
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
#           C. Bogausch
#   (cody.bogausch@sunycgcc.edu)
#
# Version
#   March 26, 2024
#
###############################################################################

__author__ = "C. Mikijanic, Cody Bogausch"
__version__ = 1.01


class BinaryTreeNode:

    ### 
    # Description:
    #    Constructor which initializes all three data fields
    #    
    #   ???
    #
    ###      
    def __init__(self, initialData=None, initialLeft=None, initialRight=None):
        self.data = initialData
        self.left = initialLeft
        self.right = initialRight

    ### 
    # Description:
    #    Read DATA of the node
    #
    # Parameters:
    #   None
    #
    # Returns:
    #   Data from this node
    #
    ###
    def getData(self):
        return self.data

    ### 
    # Description:
    #    Read the LEFT LINK of the node
    #    
    #   ???
    #
    ###      
    def getLeft(self):
        return self.left

        ###

    # Description:
    #    Read the DATA of the LEFT-MOST node
    #    
    #   ???
    #
    ###      
    def getLeftmostData(self):
        if self.getLeft() is not None:
            self.getLeft().getLeftmostData()
        else:
            return self.getData()

    ### 
    # Description:
    #    Read the RIGHT LINK of the node
    #    
    #   ???
    #
    ###      
    def getRight(self):
        return self.right

    ### 
    # Description:
    #    Read the DATA of the RIGHT-MOST node
    #    
    #   ???
    #
    ###      
    def getRightmostData(self):
        if self.getRight() is not None:
            self.getRight().getRightmostData()
        else:
            return self.getData()

    ### 
    # Description:
    #   Compute the depth/height of a tree--the number of nodes
    #   along the longest path from the root node down to
    #   the farthest leaf node
    #    
    #   ???
    #
    ###
    def height(node):
        # Initialize count variables (?)
        left_height = 0
        right_height = 0

        # Check left side of sub-tree
        if node.getLeft() is not None:
            # Recurse down into left tree, extracting the height
            left_height = node.getLeft().height()

        # Check right side of the sub-tree
        if node.getRight() is not None:
            # Recurse down into right tree, extracting the height
            right_height = node.getRight().height()

        # Return the larger of the two variables and add one to it for this level of the node
        return 1 + max(left_height, right_height)

    ###
    # Description:
    #    Check if the given node IS a LEAF 
    #    
    # Parameters:
    #   None
    #
    # Returns:
    #   Bool if this Node is a leaf
    #
    ###      
    def isLeaf(self):
        # If this node has no right Node and no Left Node
        return self.getLeft() is None and self.getRight() is None

    ### 
    # Description:
    #   uses an PREORDER traversal to PRINT on SCREEN the DATA 
    #    of each node at or below this node of the binary tree. 
    #    
    #   ???
    #
    ###      
    def preorderPrint(self):
        print(f"{self.data} ")
        if self.getLeft() is not None:
            self.getLeft().preorderPrint()
        if self.getRight() is not None:
            self.getRight().preorderPrint()

    ### 
    # Description:
    #    uses an INORDER traversal to PRINT on SCREEN the DATA 
    #    of each node at or below this node of the binary tree. 
    #    
    #   ???
    #
    ###      
    def inorderPrint(self):
        if self.getLeft() is not None:
            self.getLeft().preorderPrint()
        print(f"{self.data} ")
        if self.getRight() is not None:
            self.getRight().preorderPrint()

    ### 
    # Description:
    #    uses an POSTORDER traversal to PRINT on SCREEN the DATA 
    #    of each node at or below this node of the binary tree.
    #    
    #   ???
    #
    ###   
    def postorderPrint(self):
        if self.getLeft() is not None:
            self.getLeft().preorderPrint()
        if self.getRight() is not None:
            self.getRight().preorderPrint()
        print(f"{self.data} ")

    ###
    # Description: Show DEPTH of nodes (Vertical splay)
    #    uses an INORDER traversal to PRINT on the screen the DATA of each node at or below this node 
    #    of the binary tree(with INDENTATION to indicate the DEPTH of the nodes
    #    a dash "--" is printed at any place where a child has no sibling
    #    (the indentation of each line of data is four times its depth in the tree)
    # Parameters: (BinaryTreeNode) self, (int) depth
    # Returns: N/A
    ###
    def print(self, depth):

        # Create a start index (will be the number of spaces used to indent a level)
        i = 0
        # Ensure that depth is an integer object
        depth = int(depth)
        # Print the indentation and the data from the current node:
        while (i <= depth):
            # Print out spaces
            print("  ", end="")
            # Increase index
            i += 1
        # Print the current node    
        print(self.data)

        # Print/traverse the left subtree (or a dash "--" if there is no left child) 
        if (self.left != None):
            self.left.print(depth + 1)
        # ELSE (No Left subtree)    
        else:
            # Check to see if there is a right subtree      
            if (self.right != None):
                # Reset the spacing index
                i = 0
                # Print out spacing for level (nodes/blank marks will be on end of spacing)
                while (i <= depth + 1):
                    print("  ", end="")
                    i += 1
                # No child = Print "--"    
                print("--")

        # Print/traverse the right subtree (or a dash "--" if there is no left child)
        if (self.right != None):
            self.right.print(depth + 1)
        # ELSE (No Right subtree)      
        else:
            # Check to see if there is a left subtree 
            if (self.left != None):
                # Reset the spacing index
                i = 0
                # Print out spacing for level (nodes/blank marks will be on end of spacing)
                while (i <= depth + 1):
                    print("  ", end="")
                    i += 1
                # No child = Print "--"    
                print("--")

    ###
    # Description:
    # REMOVEs the LEFTMOST Node of the tree below this node.
    #   Wrapper function for removeLeftmost_helper.
    #   See removeLeftmost_helper() function for more information.
    #    
    #   ???
    #
    ### 
    def removeLeftmost(self):
        BinaryTreeNode.removeLeftmost_helper(self)

    ###
    # Description: 
    # REMOVE the RIGHTMOST Node of the tree below this node.
    #   The return value is a reference to the root of the new (smaller) tree.
    #   This return value could be None if the original tree had only one
    #   node (since that one node has now been removed).
    # Helper function for removeLeftmost
    #    
    #   ???
    #
    ###     

    @staticmethod
    def removeLeftmost_helper(cursor):
        pointer = cursor.getLeft().getLeft()

        if pointer is None:

            cursor.setLeft(None)

        else:

            BinaryTreeNode.removeLeftmost_helper(cursor.getLeft())

    ###
    # Description:      
    # REMOVE the RIGHTMOST Node of the tree below this node.
    #   Wrapper function for removeRightmost_helper.
    #   See removeRightmost_helper() function for more information.
    #    
    #   ???
    #
    ###     
    def removeRightmost(self):
        BinaryTreeNode.removeRightmost_helper(self)

    ###
    # Description:     
    # REMOVE the RIGHTMOST Node of the tree below this node.
    #   The return value is a reference to the root of the new (smaller) tree.
    #   This return value could be None if the original tree had only one
    #   node (since that one node has now been removed).
    # Helper function for removeRightmost
    ###
    @staticmethod
    def removeRightmost_helper(cursor):
        pointer = cursor.getRight().getRight()

        if pointer is None:

            cursor.setRight(None)

        else:
            BinaryTreeNode.removeLeftmost_helper(cursor.getRight())

    # Description: 
    # WRITE or change data of the node
    #    
    #   ???
    #
    ###     
    def setData(self, newData):
        self.data = newData

    # Description: 
    # WRITE or change LEFT LINK of the node
    #    
    #   ???
    #
    ###     
    def setLeft(self, newLeft):
        self.left = newLeft

    # Description: 
    # WRITE or change RIGHT LINK of the node
    #    
    #   ???
    #
    ###     
    def setRight(self, newRight):
        self.right = newRight

    ###
    # Description: 
    # COPY a binary tree.
    # The return value is a reference to the root of the copy.
    #    
    #   ???
    #
    ###
    @staticmethod
    def treeCopy(source):
        left_copy = None

        right_copy = None

        left = source.getLeft()

        right = source.getRight()

        if left is not None:
            left_copy = BinaryTreeNode.treeCopy(left)

        if right is not None:
            right_copy = BinaryTreeNode.treeCopy(right)

        return BinaryTreeNode(source.getData(), left_copy, right_copy)


    ###
    # Description: 
    # SIZE of a tree => Count the NUMBER of NODEs in a binary tree.
    #    
    #   ???
    #
    ###     
    @staticmethod
    def treeSize(root):
        left_size = 0

        right_size = 0

        left = root.getLeft()

        right = root.getRight()

        if left is not None:
            left_size = BinaryTreeNode.treeSize(left)

        if right is not None:
            right_size = BinaryTreeNode.treeSize(right)

        return left_size + right_size + 1

