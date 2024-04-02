#!/usr/bin/env python3
# coding: utf-8

###############################################################################
# This is a tester file for BinarySearchTree
# 
# A BinaryTreeNode provides a node for a binary tree. Each node 
# contains a piece of data and references to a left and right child. 
# The references to children may be None to indicate
# that there is no child. 
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

__author__ = "C. Mikijanic"
__version__ = 1.0

# Used to create random data for BinarySearchTrees
import random 
# BinarySearchTree class used to build BinarySearchTrees
from BinarySearchTree import *

#######################################################################
# This class is a tester for BinaryTreeNode and BinarySearchTree 
######################################################################/
# use BinaryTreeNode, BinarySearchTree 

class BinarySearchTree_Test: 
        
    def main():

        # Binary Search Trees used during the process  
        treeA = None 
        treeB = None
        treeC = None
        treeD = None

        #Low and high number limits used during random integer generation
        randomLimit_low = 0
        randomLimit_high = 101

        # Pre-set of integer lists used during creation of Trees in Phase A 
        # These have been created to trigger certain conditions
        setOfInts = [32, 91, 96, 22, 49, 65, 49, 68, 67, 76]
        setOfInts2 = [1, 41, 82, 83, 60, 96, 45, 60, 46, 88]    

        ###############################################################################
        # A) Create trees using Non-Random Data:
        ###############################################################################
        print("")
        print("A) Create NON-Random Trees:")
        print("===========")  

        # GenerateTrees
        print("Insert Random Integers: ")
        # Create variable for BinarySearchTree
        treeA = BinarySearchTree()
        # Create a tree using a pre-set series of integers (not sorted)
        # Fill treeA with data
        for i in setOfInts:
            treeA.add( i )
            # Print out each element added to the tree (SAN check)
            print(str(i) + " " , end="")


        print("")
        print("Insert Random Integers: ")

        # Create variable for BinarySearchTree
        treeB = BinarySearchTree()
        # Create a tree using a pre-set series of integers (not sorted)
        # Fill treeB with data
        for i in setOfInts2:
            treeB.add( i )
            # Print out each element added to the tree (SAN check)
            print(str(i) + " " , end="")
        print("")
        
        # Display TreeA 
        print("treeA: ")
        treeA.getRoot().inorderPrint()
        print("")
        # Display TreeB 
        print("treeB: ")
        treeB.getRoot().inorderPrint()
        print("", end = "\n\n\n")


        ###############################################################################
        # B) TEST BinarySearchTree functionality using NON-random data:
        ###############################################################################
        
        print("B) TEST:")
        print("===========")
        

        # 1) Display TreeA (preorder, inorder, postorder, then print tree):
        print("")
        print("1) Display treeA:")
        print("")
        print(" Preorder treeA:")
        treeA.preorderPrint()
        print("")
        print(" Inorder treeA:")
        treeA.inorderPrint()    
        print("")
        print(" Postorder treeA: ")
        treeA.postorderPrint()
        print("")
        treeA.print()
        print("")


        # 2) Display TreeA:
        # Add Tree reference, BinarySearch tree object
        # By using BinaryTreeNode functions
        #     getting the root, and setting it manually
        print("2) Add Tree reference, using BinaryTreeNode functions:")
        print("Pointing to TreeA to BStreeA....")
        BStreeA = BinarySearchTree()
        BStreeA.setRoot(treeA.getRoot())
        print("Object TYPE CHECK:")
        print("TreeA is of Type: ", type(treeA))
        print("NewlyCreated BStreeA is of Type: ", type(treeA))
        BStreeA.print()
        print("")
        

        # 3) Add treeB to treeA via Union
        print("3) treeB has been added to treeA => tree C")
        treeC = BinarySearchTree.union(treeA, treeB)
        print("treeC:")
        treeC.print()
        print("")    

        # 4) Check the SIZE of treec
        print("4) Duplicates are removed during the insertion process.")
        print("TreeA should have 9 items. (One duplicate in list.)")
        print("treeA's SIZE = ", treeA.size()) 
        print("TreeB should have 9 items. (One duplicate in list.)")
        print("treeB's SIZE = ", treeB.size())     
        print("Combined tree should have 17 items. (One duplicate between two lists.)")
        print("treeC's SIZE = ", treeC.size())
        print("")       

        # 5) SEARCH for two Nodes (do not have to be the same)
        # Promt for user input
        print("5) Enter the Value of a node Z to SEARCH:", end="")
        print("")
        nodeData = int(input())
        occurances = treeC.contains(nodeData)
        print("\t", nodeData, "has appeared: " + str(occurances))
        print("")

        # Promt for user input
        print("Enter the Value of a node Z to SEARCH:", end="")
        print("")
        nodeData = int(input())
        occurances = treeC.contains(nodeData)
        print("\t", nodeData, "has appeared " + str(occurances))
        print("")


        # 5) Make a COPY of treeC
        print("5) Make a COPY of treeD using treeCopy Function")
        treeD = BinarySearchTree( BinaryTreeNode.treeCopy(treeC.getRoot()) )
        # Display treeD 
        treeD.print()
        print("")
        

        # 6) Check the SIZE of treeD
        print("6) treeD's SIZE = ", treeD.size())
        print("")
        
        # 7) ADD NODEs
        print("7) Adding nodes to the tree:")
        print("Adding 16777216....")
        treeD.add( 16777216 )
        treeD.print()
        print("")    
        print("Adding 16777216....") 
        treeD.add( 16777216 ) 
        treeD.print()
        print("")    
        print("Adding 32....") 
        treeD.add( 32 )
        treeD.print()
        print("")    
        print("Adding 1....")    
        treeD.add( 1 )
        treeD.print()
        print("")

        # 8) REMOVE a NODE
        print("8) REMOVING inserted nodes from tree (integrity check):")
        print("")    
        print("Removing 16777216....") 
        treeD.remove( 16777216 ) 
        treeD.print()
        print("")    
        print("Removing 16777216....") 
        treeD.remove( 16777216 ) 
        treeD.print()   
        print("")    
        print("Removing 1....")     
        treeD.remove( 1 ) 
        treeD.print()
        print("")    
        print("Removing root, 32....")     
        treeD.remove( 32 )  
        treeD.print()  
        print("")

    
        # Display treeD after removals
        print("TreeD after removals:")
        treeD = treeD
        treeD.print()
        #treeD.print(7)
        print("")
        print("", end = "\n\n\n")

        ###############################################################################
        # C) Random Data:
        print("C) Create RANDOM trees:")
        print("===========")


        # GenerateTrees
        print("Insert Random Integers for TreeA: ")
        #Reset TreeA to empty binary search tree 
        treeA = BinarySearchTree()
        # For ten items
        for i in range(10):
            number = random.randint(randomLimit_low,  randomLimit_high)
            treeA.add( number )
            print(str(number) + " " , end="")


        print("")
        print("Insert Random Integers for TreeB: ")
        #Reset TreeB to empty binary search tree
        treeB = BinarySearchTree()
        # For ten items
        for i in range(10):
            #Get a random number from 0 to 101
            number = random.randint(randomLimit_low, randomLimit_high)
            treeB.add( number )
            print(str(number) + " " , end="")
        print("")

        
        # Display TreeA 
        print("treeA: ")
        treeA.inorderPrint()
        print("")
        # Display TreeB 
        print("treeB: ")
        treeB.inorderPrint()
        print("", end = "\n\n\n")


        

        ###############################################################################
        # D) TEST BinarySearchTree functionality using RANDOM data:
        ###############################################################################

        print("D) TEST Random Data:")
        print("========")
        print("")
        

        # 1) Display TreeA:
        print("")
        print("1) Display treeA:")
        print("")
        print(" Preorder treeA:")
        treeA.preorderPrint()
        print("")
        print(" Inorder treeA:")
        treeA.inorderPrint()    
        print("")
        print(" Postorder treeA: ")
        treeA.postorderPrint()
        print("")
        treeA.print()
        print("")


        # 2) Display TreeA:
        # Copy Tree from BinarySearch tree object,
        # By using BinaryTreeNode functions
        #     copying the root, and setting it manually
        print("2) Copy Tree from BinarySearch tree object using BinaryTreeNode functions:")
        print("Copying tree from TreeA to BStreeA....")
        BStreeA = BinarySearchTree()
        BStreeA.setRoot(treeA.getRoot())
        print("TreeA is of Type: ", type(treeA))
        print("NewlyCreated BStreeA is of Type: ", type(treeA))
        BStreeA.print()
        print("")
        

        # 3) Add treeB to treeA via Union
        print("3) treeB has been added to treeA => tree C")
        treeC = BinarySearchTree.union(treeA, treeB)
        print("treeC:")
        treeC.print()  
        print("")     

        # 4) SEARCH for two Nodes (do not have to be the same)
        print("4) Enter the Value of a node Z to SEARCH:", end="")
        print("")
        nodeData = int(input())
        #nodeData = 72
        occurances = treeC.contains(nodeData)
        print("\t", nodeData, "has appeared: " + str(occurances))
        print("")

        print("Enter the Value of a node Z to SEARCH:", end="")
        print("")
        nodeData = int(input())
        #nodeData = 60
        occurances = treeC.contains(nodeData)
        print("\t", nodeData, "has appeared " + str(occurances))
        print("")


        # 5) Make a COPY of treeC
        print("5) Make a COPY of treeC using treeCopy Function")
        treeD = BinarySearchTree()
        # Copy using the treeCopy function - line separated out for clarity
        treeCopy = BinaryTreeNode.treeCopy(treeC.getRoot())
        # Save the tree copy into treeD
        treeD.setRoot(treeCopy)
        # Display treeD 
        treeD.print()
        print("")
        

        # 6) Check the SIZE of treeD
        print("6) treeD's SIZE = ", treeD.size())
        
        # 7) ADD NODEs
        print("7) Adding nodes to the tree:")
        print("Adding 16777216....")
        treeD.add( 16777216 )
        treeD.print()
        print("")    
        print("Adding 16777216....") 
        treeD.add( 16777216 ) 
        treeD.print()
        print("")    
        print("Adding 32....") 
        treeD.add( 32 )
        treeD.print()
        print("")    
        print("Adding 1....")    
        treeD.add( 1 )
        treeD.print()
        print("")

        # 8) REMOVE NODEs
        print("8) REMOVING inserted nodes from tree (integrity check):")
        print("")    
        print("Removing 16777216....") 
        print( treeD.remove( 16777216 ) )
        treeD.print()
        print("")    
        print("Removing 16777216....") 
        print( treeD.remove( 16777216 ) )
        treeD.print()   
        print("")    
        print("Removing 1....")     
        print( treeD.remove( 1 ) )
        treeD.print()
        print("")    
        print("Removing 32....")     
        print( treeD.remove( 32 ) ) 
        treeD.print()  
        print("")

    
        # Display treeD 
        print("TreeD after removals:")
        treeD.print()
        print("")

    if __name__ == "__main__":
        main()