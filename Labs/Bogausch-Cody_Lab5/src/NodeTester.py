#!/usr/bin/env python3
# coding: utf-8

__author__ = "Cody Bogausch"
__version__ = "Pre_Alpha_0.01_Dev"

from Node import Node


def print_under_seperator(printable: any) -> None:
    """
    Converts parameter to a string and prints it to the console with a seperator above it

    @param printable: any object to be converted into a string and printed to the console
    @return None
    """

    def seperator():
        print("---------------------------------------------------------------")

    seperator()
    print(str(printable))


# 1) Creates an empty node
print_under_seperator("(1a) Create an empty node:")
empty = Node(None)
print_under_seperator(empty)

# and a node with an integer.
print_under_seperator("(1b) Create a node with an integer:")
original = Node(-10)
print_under_seperator(original)

# 2) Adds a node after the node with the integer, to make a short sequence. (Use the number 13).
print_under_seperator("(2) Add a node (13) after the node with the integer: ")
original.addNodeAfter(13)
print_under_seperator(original)

# 3) Adds a node after the sequence head, between the two existing nodes. (Use the number 42).
print_under_seperator("(3) Add a node (42) to the sequence head:")
original.addNodeAfter(42)
print_under_seperator(original)

# 4) Copy the sequence.
print_under_seperator("(4) Copy the sequence:")
copy = original.listCopy()
print_under_seperator("Original:")
print_under_seperator(original)
print_under_seperator("Copy:")
print_under_seperator(copy)


# 5) Adds the copy of the sequence onto the original.
def get_last_node_in_sequence(head: Node) -> Node:
    """
    Retrieve the last node in the sequence of nodes starting from the "head". 
    
    :param head: Node to begin searching down into
    
    :return: Node with a link of None
    """
    # Cursor will point to different potential nodes until it gets to the end
    cursor = head

    # Search recursively until we reach None
    while cursor.link is not None:
        # Cursor becomes the next link in the sequence
        cursor = cursor.getLink()

    return cursor


print_under_seperator("(5) Add a copy of the sequence onto the end of the original:")
tail = get_last_node_in_sequence(original)
tail.setLink(copy)
print_under_seperator(original)

# 6) Create a list copy with a tail and attach it onto the original.
print_under_seperator("(6) Create a list copy with a tail and attach it to the original")
copy = original.listCopyWithTail()
print_under_seperator("Copy head:")
print_under_seperator(copy[0])
print_under_seperator("Copy Tail:")
print_under_seperator(copy[1])
tail = get_last_node_in_sequence(original)
tail.setLink(copy[0])
print_under_seperator("Add copy head to the original:")
print_under_seperator(original)

# 7) Get the length of the original sequence.
length = original.listLength(original)
print_under_seperator("(7) Get the length of the original sequence")
print_under_seperator("Original:")
print_under_seperator(original)
print_under_seperator(f"Length: {length}")

# 8) Get the first half of the list.
print_under_seperator("(8) Get the first half of the list:")
mid_point = original.listPosition(length // 2)
list_part = original.listPart(original, mid_point)
print_under_seperator("First half:")
print_under_seperator("Head:")
print_under_seperator(list_part[0])
print_under_seperator("Mid_Point:")
print_under_seperator(list_part[1])

# 9) Get the second node in the list.
print_under_seperator("(9) Get the second node in the list:")
second_node = original.listPosition(2)
print_under_seperator(second_node)

# 10) Get the location of the first item with the contents (42).
print_under_seperator("(10) Get the location of the first item with the contents 42:")
searched_node = original.listSearch(42)
print_under_seperator(searched_node)

# 11) Remove the node after the first item with the contents (42).
print_under_seperator("(11) Remove the node after the first item with the contents 42:")
searched_node.removeNodeAfter()
print_under_seperator(original)

# 12) Change the first item in the list so that it contains the number (73).
print_under_seperator("(12) Change the first item in the list so that it contains the number 73:")
original.setData(73)
print_under_seperator(original)
