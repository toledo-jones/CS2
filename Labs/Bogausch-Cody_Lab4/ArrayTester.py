#!/usr/bin/env python3
# coding: utf-8

"""
    This file will test the array class that we created
"""

__author__ = "Cody Bogausch"
__version__ = "1.0"


from Array import Array

# Creates an array with ten positions.
print("Create array")
myArray = Array(10)

# Displays the length of the array.
print(f"Length of array: {len(myArray)}")

# Prints the contents.
print(str(myArray))

# Fills in the array with the sequence of 1 to 10.
print("Filling in the array with 1-10")
for index in range(len(myArray)):
    myArray[index] = index + 1

# Prints the new array.
print(str(myArray))

# Accesses the first item, and prints it.
print(f"The first item in the array is {myArray[0]}")

# Accesses the last item, and prints it.
print(f"The last item in the array is {myArray[-1]}")

# Traverses the array.
print("Traversing the array")
for item in myArray:
    print(item)

print("Create a new array with same data as the original:")
# Creates a new array with the same data as the original,
newArray = myArray[:]
print(newArray)

print("Sets the old array variable to new array object:")
# Sets the old array variable to the new array object.
myArray = newArray
print(myArray)

print("Insert the number 11 in the array object at index 2:")
# Inserts the number 11 in the new array object in position 2.
newArray[2] = 11
print(newArray)

# Create a 10x10 grid object out of two arrays
grid = Array(10, 0)
for item in range(len(grid)):
    grid[item] = Array(10, 0)

# Fill it with the sequence 1, 2, 3…and so on.
count = 0
for column in range(10):
    for row in range(10):
        count += 1
        grid[column][row] = count

print("Here is the filled in grid:")
# Print out the filled grid.
for column in grid:
    print(str(column))
        