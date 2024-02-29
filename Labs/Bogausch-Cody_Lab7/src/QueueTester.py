#!/usr/bin/env python3
# coding: utf-8
##By: Professor Mikijanic

###############################################################################
# The Queue Tester class tests the functionality of the Queue.py class.
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
 
from Queues import *

###############################################################################
# Step 1: Create an empty queue
#
##############################################################################/

#After all steps, print queue and print check to see if queue is empty.

print("_______________________")

print("Create an empty queue object", end="\n\n")

aQueue = Queue()
print(str(aQueue))
print("Is empty: " + str(aQueue.isEmpty()))

###############################################################################
# Step 2: Fill a queue object with 3 elements
#
##############################################################################/

print("_______________________")

print("Fill a queue object with 3 elements", end="\n\n")

aQueue.enqueue(1)
aQueue.enqueue(2)
aQueue.enqueue(3)
print(str(aQueue))

print("Is empty: " + str(aQueue.isEmpty()))

###############################################################################
# Step 3: Dequeue 3 elements from Queue 1, one at a time
#
##############################################################################/

print("_______________________")
print("Dequeue 3 elements from Queue 1, one at a time", end="\n\n")

aQueue.dequeue()
print(str(aQueue))
aQueue.dequeue()
print(str(aQueue))
aQueue.dequeue()
print(str(aQueue))

print("Is empty: " + str(aQueue.isEmpty()))

print("_______________________")
