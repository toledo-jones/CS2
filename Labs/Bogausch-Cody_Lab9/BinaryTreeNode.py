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
#   __init__
#   getData
#   getLeft
#   getLeftmostData
#   getRight
#   getRightmostData
#   height
#   inorderPrint
#   isLeaf
#   postorderPrint
#   preorderPrint
#   print
#   removeLeftmost
#   removeLeftmost_helper
#   removeRightmost
#   removeRightmost_helper
#   setData
#   setLeft
#   setRight
#   treeCopy
#   treeSize
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
    # Parameters:
    #   self
    #   initialData - data in this node
    #   initialLeft - left link/child node
    #   initialRight - right link/child node
    #
    # Returns:
    #   BinaryTreeNode() object
    #
    ###
    def __init__(self, initialData=None, initialLeft=None, initialRight=None):

        # Initialize Attributes
        self.data: any = initialData
        self.left: BinaryTreeNode = initialLeft
        self.right: BinaryTreeNode = initialRight


    ### 
    # Description:
    #    Read DATA of the node
    #
    # Parameters:
    #   self
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
    # Parameters:
    #   self
    #
    # Returns:
    #   Node object corresponding to left link
    #
    ###
    def getLeft(self):
        return self.left

    ###
    # Description:
    #    Read the DATA of the LEFT-MOST node
    #
    # Parameters:
    #   self
    #
    # Returns:
    #   Data in the deepest left node
    ###
    def getLeftmostData(self):

        # Determine depth
        if self.getLeft() is not None:

            # Can go deeper, recurse:
            self.getLeft().getLeftmostData()

        # This node is the deepest left:
        else:

            # Return data in leftmost node
            return self.getData()

    ### 
    # Description:
    #    Read the RIGHT LINK of the node
    #
    # Parameters:
    #   self
    #
    # Returns:
    #   Node object corresponding to right link
    #
    ###
    def getRight(self):
        return self.right

    ###
    # Description:
    #    Read the DATA of the RIGHT-MOST node
    #
    # Parameters:
    #   self
    #
    # Returns:
    #   Data in the deepest left node
    ###
    def getRightmostData(self):

        # Determine depth
        if self.getRight() is not None:

            # Can go deeper, recurse:
            self.getRight().getRightmostData()

        # This node is the deepest right:
        else:

            # Return data in right-most node
            return self.getData()

    ### 
    # Description:
    #   Compute the depth/height of a tree--the number of nodes
    #   along the longest path from the root node down to
    #   the farthest leaf node
    #    
    # Parameters:
    #   node - BinaryTreeNode() object representing the root of the tree to be searched.
    #
    # Returns:
    #   height - int total height of the highest node structure in the tree
    ###
    @staticmethod
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
    #   self
    #
    # Returns:
    #   Bool if this Node is a leaf
    #
    ###
    def isLeaf(self):

        # return True if this node has no right AND no left link
        return self.getLeft() is None and self.getRight() is None

    ### 
    # Description:
    #   uses an PREORDER traversal to PRINT on SCREEN the DATA 
    #    of each node at or below this node of the binary tree. 
    #    
    # Parameters:
    #   self
    #
    # Returns:
    #   None
    #
    ###
    def preorderPrint(self):

        # Pre order print
        print(f"{self.data} ")

        # If there is a left node
        if self.getLeft() is not None:
            # Recurse
            self.getLeft().preorderPrint()

        # If there is a right node:
        if self.getRight() is not None:
            # Recurse
            self.getRight().preorderPrint()

    ### 
    # Description:
    #    uses an INORDER traversal to PRINT on SCREEN the DATA 
    #    of each node at or below this node of the binary tree. 
    #    
    # Parameters:
    #   self
    #
    # Returns:
    #   None
    #
    ###
    def inorderPrint(self):

        # If there is a left node:
        if self.getLeft() is not None:

            # Recurse
            self.getLeft().preorderPrint()

        # In order print
        print(f"{self.data} ")

        # If there is a right node:
        if self.getRight() is not None:

            # Recurse
            self.getRight().preorderPrint()

    ### 
    # Description:
    #    uses an POSTORDER traversal to PRINT on SCREEN the DATA 
    #    of each node at or below this node of the binary tree.
    #    
    # Parameters:
    #   self
    #
    # Returns:
    #   None
    #
    ###
    def postorderPrint(self):

        # If there is a left node:
        if self.getLeft() is not None:

            # Recurse
            self.getLeft().preorderPrint()

        # If there is a right node:
        if self.getRight() is not None:

            # Recurse
            self.getRight().preorderPrint()

        # Post order print
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
        while i <= depth:
            # Print out spaces
            print("  ", end="")
            # Increase index
            i += 1
        # Print the current node    
        print(self.data)

        # Print/traverse the left subtree (or a dash "--" if there is no left child) 
        if self.left != None:
            self.left.print(depth + 1)
        # ELSE (No Left subtree)    
        else:
            # Check to see if there is a right subtree      
            if self.right != None:
                # Reset the spacing index
                i = 0
                # Print out spacing for level (nodes/blank marks will be on end of spacing)
                while i <= depth + 1:
                    print("  ", end="")
                    i += 1
                # No child = Print "--"    
                print("--")

        # Print/traverse the right subtree (or a dash "--" if there is no left child)
        if self.right != None:
            self.right.print(depth + 1)
        # ELSE (No Right subtree)      
        else:
            # Check to see if there is a left subtree 
            if self.left != None:
                # Reset the spacing index
                i = 0
                # Print out spacing for level (nodes/blank marks will be on end of spacing)
                while i <= depth + 1:
                    print("  ", end="")
                    i += 1
                # No child = Print "--"    
                print("--")

    ###
    # Description:
    # REMOVE the LEFTMOST Node of the tree below this node.
    #   Wrapper function for removeLeftmost_helper.
    #   See removeLeftmost_helper() function for more information.
    #
    # Parameters:
    #   self
    #
    # Returns:
    #   None
    #
    ###
    def removeLeftmost(self):

        # This function is an alias for:
        BinaryTreeNode.removeLeftmost_helper(self)

    ###
    # Description: 
    # REMOVE the LEFTMOST Node of the tree below this node.
    #   The return value is a reference to the root of the new (smaller) tree.
    #   This return value could be None if the original tree had only one
    #   node (since that one node has now been removed).
    # Helper function for removeLeftmost
    #    
    # Parameters:
    #   cursor - BinaryTreeNode() object, the current node in our depth search
    #
    # Returns:
    #   None
    #
    ###
    @staticmethod
    def removeLeftmost_helper(cursor):

        # Pointer to move between nodes. Looks down two levels.
        pointer = cursor.getLeft().getLeft()

        # If pointer is none:
        if pointer is None:

            # Pointer is none so the right link must be the leftmost. Set it to None.
            cursor.setLeft(None)

        # Pointer is not none so there must be a deeper node
        else:

            # Recurse down further into binary tree
            BinaryTreeNode.removeLeftmost_helper(cursor.getLeft())

    ###
    # Description:      
    # REMOVE the RIGHTMOST Node of the tree below this node.
    #   Wrapper function for removeRightmost_helper.
    #   See removeRightmost_helper() function for more information.
    #    
    # Parameters:
    #   self
    #
    # Returns:
    #   None
    #
    ###
    def removeRightmost(self):

        # This function is an alias for:
        BinaryTreeNode.removeRightmost_helper(self)

    ###
    # Description:     
    # REMOVE the RIGHTMOST Node of the tree below this node.
    #   The return value is a reference to the root of the new (smaller) tree.
    #   This return value could be None if the original tree had only one
    #   node (since that one node has now been removed).
    # Helper function for removeRightmost
    #
    # Parameters:
    #   cursor - BinaryTreeNode() object, the current node in our depth search
    #
    # Returns:
    #   None
    #
    ###
    @staticmethod
    def removeRightmost_helper(cursor):

        # Pointer to move between nodes. Looks down two levels.
        pointer = cursor.getRight().getRight()

        # If pointer is none:
        if pointer is None:

            # Pointer is none so the right link must be the rightmost. Set it to None.
            cursor.setRight(None)

        # Pointer is not none so there must be a deeper node
        else:

            # Recurse down further into binary tree
            BinaryTreeNode.removeRightmost_helper(cursor.getRight())

    # Description: 
    # WRITE or change data of the node
    #    
    # Parameters:
    #   newData - data to be written to the node
    #
    # Returns:
    #   None
    #
    ###
    def setData(self, newData):
        self.data = newData

    # Description: 
    # WRITE or change LEFT LINK of the node
    #    
    # Parameters:
    #   newLeft - new BinaryTreeNode() object to be made a child of this node at it's left link
    #
    # Returns:
    #   None
    #
    ###
    def setLeft(self, newLeft):
        self.left = newLeft

    # Description: 
    # WRITE or change RIGHT LINK of the node
    #
    # Parameters:
    #   newLeft - new BinaryTreeNode() object to be made a child of this node at it's right link
    #
    # Returns:
    #   None
    #
    ###
    def setRight(self, newRight):
        self.right = newRight

    ###
    # Description: 
    # COPY a binary tree.
    # The return value is a reference to the root of the copy.
    #    
    # Parameters:
    #   source - BinaryTreeNode() object root to be copied
    #
    # Returns:
    #   BinaryTreeNode() root of copy
    #
    ###
    @staticmethod
    def treeCopy(source):

        # Initialize copies for each side of the node tree
        left_copy = None
        right_copy = None

        # Alias for the left and right side of node tree ( for readability )
        left = source.getLeft()
        right = source.getRight()

        # There is a left link:
        if left is not None:

            # Recurse, assigning left_copy to the return value of this function
            left_copy = BinaryTreeNode.treeCopy(left)

        # There is a right link:
        if right is not None:

            # Recurse, assigning right_copy to the return value of this function
            right_copy = BinaryTreeNode.treeCopy(right)

        # Return a new binary tree node with the data from the source and the copies made of deeper nodes above
        return BinaryTreeNode(source.getData(), left_copy, right_copy)

    ###
    # Description: 
    # SIZE of a tree => Count the NUMBER of NODEs in a binary tree.
    #    
    # Parameters:
    #   root - BinaryTreeNode() object root to be counted
    #
    # Returns:
    #   int - total size of tree
    #
    ###
    @staticmethod
    def treeSize(root):

        # Initialize size values for each side of the node tree
        left_size = 0
        right_size = 0

        # Alias for the left and right side of node tree ( for readability )
        left = root.getLeft()
        right = root.getRight()

        # There is a left link:
        if left is not None:

            # Recurse, assigning left_size to the output of this function
            left_size = BinaryTreeNode.treeSize(left)

        # There is a right link:
        if right is not None:

            # Recurse, assigning right_size to the output of this function
            right_size = BinaryTreeNode.treeSize(right)

        # Return an int of the above sizes summed + 1 for this node
        return left_size + right_size + 1
