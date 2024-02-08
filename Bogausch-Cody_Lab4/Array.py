#!/usr/bin/env python3
# coding: utf-8

"""
    File: arrays.py
    An Array is like a list, but the client can use
    only [], len, iter, and str.
     
    To instantiate, use
    <variable> = Array(<capacity>, <optional fill value>)
     
    The fill value is None by default.

    Fuctions:
        ???
    Constants:
        ???
"""

__author__ = "Cody Bogausch"
__version__ = "1.0"

# REMEMBER TO PUT IN DETAILED COMMENTS!

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue=None):
        """Capacity is the static size of the array. fillValue is placed at each position."""
        self.items = list()
        
        # Set each item in the internal list to the fill value
        for _ in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        self.items[index] = newItem
