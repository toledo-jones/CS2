##By: Christine Mikijanic
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
#   (main@colorado.edu)
#            C. Mikijanic
#   (christine.mikijani@sunycgcc.edu)
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
      self.data = initialData
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
      try: 
         self.link = Node(item, self.link)
      except MemoryError:
         print("There is insufficient memory for a new Node")
             
   
   
   ###
   # Accessor method to get the data from this node.   
   # Argument: - none
   # Returns
   #   the data from this node
   ##/
   def getData(self):   
      return self.data
   
   
   
   ###
   # Accessor method to get a reference to the next node after this node. 
   # Argument: - none
   # Returns
   #   a reference to the node after this node (or the None reference if there
   #   is nothing after this node)
   ##/
   def getLink(self):
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
      try:
      ## Handle the special case of the empty list.
         if (source is None):
            return None
            
         ## Make the first node for the newly created list.
         copyHead = Node(source.data, None)
         copyTail = copyHead
         
         ## Make the rest of the nodes for the newly created list.
         while (source.link is not None):
            source = source.link
            copyTail.addNodeAfter(source.data)
            copyTail = copyTail.link

      except MemoryError:
         print("There is insufficient memory for the new list")
      ## Return the head reference for the new list.
      return copyHead
   
   
   
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
      
      answer = [None] * 2
     
      ## Handle the special case of the empty list.   
      if (source is None):
         return answer ## The answer has two None references .
      try: 
         ## Make the first node for the newly created list.
         copyHead = Node(source.data, None)
         copyTail = copyHead
         
         ## Make the rest of the nodes for the newly created list.
         while (source.link is not None):
            source = source.link
            copyTail.addNodeAfter(source.data)
            copyTail = copyTail.link
         
         
         ## Return the head and tail references.
         answer[0] = copyHead
         answer[1] = copyTail
      except MemoryError:
         print("Insufficient memory for the new list")
      return answer
   
   
   
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
   
      cursor = head
      answer = 0

      while (cursor is not None):
         answer += 1
         cursor = cursor.link
        
      return answer
   
   

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

      if (start is not None):

         answer = [None] * 2
         try:
            ## Make the first node for the newly created list. Notice that this will
            ## cause a TypeError if start is None.
            copyHead = Node(start.data, None)
            copyTail = copyHead
            cursor = start
            
            ## Make the rest of the nodes for the newly created list.
            while (cursor is not end):
            
               cursor = cursor.link
               if (cursor is None):
                  raise TypeError("end node was not found on the list")
               copyTail.addNodeAfter(cursor.data)
               copyTail = copyTail.link
         except MemoryError:
            print("Insufficient memory for the new list")
      else:
         raise TypeError("start is None")
      
      ## Return the head and tail references
      answer[0] = copyHead
      answer[1] = copyTail
      return answer
           
   
   
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
   
      if (position <= 0):
           print("TypeError: position is not positive")
      
      cursor = head
      i = 1
      while ((i < position) and (cursor is not None)):
         cursor = cursor.link
         i+= 1

      return cursor
   


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
   
      cursor = head
      
      while(cursor is not None):
         if (target is cursor.data):
            return cursor
         cursor = cursor.link
        
      return None
   

   
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
      if (self.link is not None):
         self.link = self.link.link
      else:
         raise TypeError("Tail node of the list, nothing to remove.")
             
   
   
   ###
   # Modification method to set the data in this node.   
   # Argument: newData
   #   the new data to place in this node
   # Post Condition:
   #   The data of this node has been set to newData.
   ##/
   def setData(self, newData):   
      self.data = newData
                                                                  
   
   
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
      self.link = newLink
   

           
