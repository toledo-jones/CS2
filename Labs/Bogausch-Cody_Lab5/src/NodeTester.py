# All of the code you create will be submitted using Lab 5 submission link.

# Compress all of your files into a .zip file, and use the following naming convention:

# Firstname-Lastname_Lab{number}.zip

# In this exercise, you will be learning and using basic linked list concepts. There are three files given in this lab:

# Node.py – which contains the class for the basic node structure.

# LinkedSeq.py – a class which extends the functionality of Node to a collection of elements

# FloatLinkedSeqDemonstration.py – a tester file for LinkedSeq.py.

# We will be working on Node.py together in class, through a process that is colloquially called “walking through the code”. This is a process that is commonly used in code reviews.

# In addition to the files that have been given, create a tester file for the Node.py class. The tester file must include code that does the following:

from Node import Node

# 1) Creates an empty node, and a node with an integer.
empty_node = Node(None)
print(empty_node)
int_node = Node(0)
print(int_node)


# 2) Adds a node after the node with the integer, to make a short sequence. (Use the number 13).
int_node.addNodeAfter(13)
print(int_node)


# 3) Adds a node after the sequence head, between the two existing nodes. (Use the number 42).
int_node.addNodeAfter(42)
print("Add a node with 42 to our previous node")
print(int_node)

# 4) Copies the sequence.
copy = int_node.listCopy()
print("Printing Copy...")
int_node.data = 1
print(f"First List: {int_node}")
print(f"Copy: {copy}")


# 5) Adds the copy of the sequence onto the original.
def get_last_node_in_sequence(head: Node) -> Node:
    """
    Retrieve the last node in the sequence of nodes starting from the "head". 
    
    :param: head: Node to begin searching down into
    
    :returns: Node with a link of None
    """
    # Cursor will point to different potential nodes until it gets to the end
    cursor = head
    
    # Search recursively until we reach None
    while cursor.link is not None:
        
        # Cursor becomes the next link in the sequence
        cursor = cursor.getLink()
        print(f"cursor points to: {cursor}")
    

    return cursor

tail = get_last_node_in_sequence(int_node)
print(f"Tail: {tail}")
print("Adding copy to original...")
tail.setLink(copy)
print(int_node)

# 6) Create a list copy with a tail, attach it onto the original.

# 7) Get the length of the original sequence.

# 8) Get the first half of the list.

# 9) Get the second node in the list.

# 10) Get the location of the first item with the contents (42).

# 11) Remove the node after the first item with the contents (42).

# 12) Change the first item in the list so that it contains the number (73).

# Separate each item on the list with print statements (which describe the step), and print out the results of each step to the terminal.

# You can do an early pre-submission which will be reviewed with your professor’s tester file, and by the end of the weekend, I will get back to you with comments. As a suggestion, if you want to check your code in this fashion, submit all of your work at the end of class. (This mimics one form of development-test organization, where development usually does not directly see test files.)

