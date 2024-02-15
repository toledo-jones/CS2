#!/usr/bin/env python3
# coding: utf-8

## File: LinkedSeq.py, based on DoubleLinkedSeq from edu.colorado.collections
## This is an assignment for students to complete

###############################################################################
# A Node provides a node for a linked list with 
# double data in each node.
#
# Note:
#   Lists of nodes can be made of any length, limited only by the amount of
#   free memory in the heap. But beyond Integer.MAX_VALUE,
#   the answer from listLength is incorrect because of arithmetic
#   overflow. 
#
#
# ChangeLog: Michael Main 
#            C. Mikijanic
#
# Version
#   January 1, 2024
#
##############################################################################/
class Node:

   ## Invariant of the Node class:
   ##   1. The node's double data is in the instance variable data.
   ##   2. For the final node of a list, the link part is None.
   ##      Otherwise, the link part is a reference to the
   ##      next node of the list. 


   ###
   # Initialize a node with a specified initial data and link to the next
   # node. Note that the initialLink may be the None reference, 
   # which indicates that the new node has nothing after it.
   # Argument: initialData
   #   the initial data of this new node
   # Argument: initialLink
   #   a reference to the node after this new node--this reference may be None
   #   to indicate that there is no node after this new node.
   # Post Condition:
   #   This node contains the specified data and link to the next node.
   ##/   
   def __init__(self, initialData, initialLink=None):
      # Store the data that this node will contain
      self.data = initialData

      # Store the link to the next node in the sequence. Default is none. 
      self.link = initialLink
   


   ###
   # Modification method to add a new node after this node.   
   # Argument: item
   #   the data to place in the new node
   # Post Condition:
   #   A new node has been created and placed after this node.
   #   The data for the new node is item. Any other nodes
   #   that used to be after this node are now after the new node.
   # Exception: MemoryError
   #   Indicates that there is insufficient memory for a new 
   #   Node. 
   ##/
   def addNodeAfter(self, item):   
      # Set the link to the item argument
      self.link = item

   
   
   ###
   # Accessor method to get the data from this node.   
   # Argument: - none
   # Returns
   #   the data from this node
   ##/
   def getData(self):   
      # The data from this node
      return self.data
   
   
   
   ###
   # Accessor method to get a reference to the next node after this node. 
   # Argument: - none
   # Returns
   #   a reference to the node after this node (or the None reference if there
   #   is nothing after this node)
   ##/
   def getLink(self):
      # Link to the next node in the chain
      return self.link                                               
    
    
    
   ###
   # Copy a list.
   # Argument: source
   #   the head of a linked list that will be copied (which may be
   #   an empty list in where source is None)
   # Returns
   #   The method has made a copy of the linked list starting at 
   #   source. The return value is the head reference for the
   #   copy. 
   # Exception: MemoryError
   #   Indicates that there is insufficient memory for the new list.   
   ##/ 
   def listCopy(source):
      # I'm assuming this is wrong but I don't really know why? 
      
      # Create a blank list
      copy = list()
      
      # Recursively searh nodes:
      while True:   
         
         # Return the head reference for the copy if the source is blank 
         if source is None:
            
            # If the copy has been filled we return the head reference
            try:
               return copy[0]
            
            # If the copy is empty just return the None source
            except IndexError:
               return source
         
         # Copy the current node
         copy.append(source)
         
         # Set the source to be the next link
         source = source.getLink()
      
      
   
   
   
   ###
   # Copy a list, returning both a head and tail reference for the copy.
   # Argument: source
   #   the head of a linked list that will be copied (which may be
   #   an empty list in where source is None)
   # Returns
   #   The method has made a copy of the linked list starting at 
   #   source.  The return value is an
   #   array where the [0] element is a head reference for the copy and the [1]
   #   element is a tail reference for the copy.
   # Exception: MemoryError
   #   Indicates that there is insufficient memory for the new list.   
   ##/
   def listCopyWithTail(source):
      "This function is not completed..."
   
   
   
   ###
   # Compute the number of nodes in a linked list.
   # Argument: head
   #   the head reference for a linked list (which may be an empty list
   #   with a None head)
   # Returns
   #   the number of nodes in the list with the given head 
   # Note:
   #   A wrong answer occurs for lists longer than the max value of integers in Python.     
   ##/   
   def listLength(self, head):
      "This function is not completed..."
   
   

   ###
   # Copy part of a list, providing a head and tail reference for the new copy. 
   # Argument: start/end
   #   references to two nodes of a linked list
   # Argument: copyHead/copyTail
   #   the method sets these to refer to the head and tail node of the new
   #   list that is created
   # @precondition
   #   start and end are non-None references to nodes
   #   on the same linked list,
   #   with the start node at or before the end node. 
   # Returns
   #   The method has made a copy of the part of a linked list, from the
   #   specified start node to the specified end node. The return value is an
   #   array where the [0] component is a head reference for the copy and the
   #   [1] component is a tail reference for the copy.
   # Exception: TypeError
   #   Indicates that start and end are not references
   #   to nodes on the same list.
   # Exception: TypeError
   #   Indicates that start is None.
   # Exception: MemoryError
   #   Indicates that there is insufficient memory for the new list.    
   ##/   
   def listPart(self, start, end):
      "This function is not completed..."
           
   
   
   ###
   # Find a node at a specified position in a linked list.
   # Argument: head
   #   the head reference for a linked list (which may be an empty list in
   #   which case the head is None)
   # Argument: position
   #   a node number
   # @precondition
   #   position > 0.
   # Returns
   #   The return value is a reference to the node at the specified position in
   #   the list. (The head node is position 1, the next node is position 2, and
   #   so on.) If there is no such position (because the list is too short),
   #   then the None reference is returned.
   # Exception: TypeError
   #   Indicates that position is not positive.    
   ##/   
   def listPosition(head, position):
      "This function is not completed..."
   


   ###
   # Search for a particular piece of data in a linked list.
   # Argument: head
   #   the head reference for a linked list (which may be an empty list in
   #   which case the head is None)
   # Argument: target
   #   a piece of data to search for
   # Returns
   #   The return value is a reference to the first node that contains the
   #   specified target. If there is no such node, the None reference is 
   #   returned.     
   ##/   
   def listSearch(head, target):
      "This function is not completed..."
   

   
   ###
   # Modification method to remove the node after this node.   
   # Argument: - none
   # @precondition
   #   This node must not be the tail node of the list.
   # Post Condition:
   #   The node after this node has been removed from the linked list.
   #   If there were further nodes after that one, they are still
   #   present on the list.
   # Exception: TypeError
   #   Indicates that this was the tail node of the list, so there is nothing
   #   after it to remove.
   ##/
   def removeNodeAfter(self):   
      "This function is not completed..."
             
   
   
   ###
   # Modification method to set the data in this node.   
   # Argument: newData
   #   the new data to place in this node
   # Post Condition:
   #   The data of this node has been set to newData.
   ##/
   def setData(self, newData):   
      "This function is not completed..."
                                                                  
   
   
   ###
   # Modification method to set the link to the next node after this node.
   # Argument: newLink
   #   a reference to the node that should appear after this node in the linked
   #   list (or the None reference if there is no node after this node)
   # Post Condition:
   #   The link to the node after this node has been set to newLink.
   #   Any other node (that used to be in this link) is no longer connected to
   #   this node.
   ##/
   def setLink(self, newLink):             
      "This function is not completed..."
   

           
