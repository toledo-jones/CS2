#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      A customer has details and has a boat.
   Functions:
      setName
      setAddress
      setPhoneNo
      setBoat
      getName
      getAddress
      getPhoneNo
      getBoat
   Constants:
      None 
"""

__author__ = "Cody Bogausch"
__version__ = "1.0"


class Customer:

	# constructor with parameters
    def __init__(self, aName, anAddress, aPhoneNo):
        # invoke accessors to populate attributes
        self.setName(aName)
        self.setAddress(anAddress)
        self.setPhoneNo(aPhoneNo)
        # initially no Boat
        self.setBoat(None)				 
	
    # set accessors
    def setName(self, newName):
        self._name = newName
        
    def setAddress(self, newAddress):
        self._address = newAddress

    def setPhoneNo(self, newPhoneNo):
        self._phoneNumber = newPhoneNo

    def setBoat(self, aBoat):
        self._boat = aBoat

    # get accessors
    def getName(self):
        return self._name

    def getAddress(self):
        return self._address

    def getPhoneNo(self):
        return self._phoneNumber
        
    def getBoat(self):
        return self._boat