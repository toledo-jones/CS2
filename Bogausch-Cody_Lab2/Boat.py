# !/usr/bin/env python
# coding: utf-8

# !/usr/bin/env python3

""""
   Description:
      A boat is owned by a customer and has related details attached.
   
   Functions:
      tellAboutSelf
      assignBoatToCustomer
      addServiceRecord
      printRecord
      setStateRegistrationNo
      setLength
      setManufacturer
      setYear
      setCustomer
      getStateRegistrationNo
      getLength
      getManufacturer
      getYear
      getCustomer

   Constants:
      None 
"""

# Description:
#    ???
# INPUT:
#    ???
# OUTPUT
#    ???

__author__ = "Cody Bogausch"
__version__ = "1.0"


class Boat:
    def __init__(self,
                 aStateRegistrationNo,
                 aLength,
                 aManufacturer,
                 aYear,
                 aCustomer):
        # Constructor. Set Class Attributes
        self.setStateRegistrationNo(aStateRegistrationNo)
        self.setLength(aLength)
        self.setManufacturer(aManufacturer)
        self.setYear(aYear)
        self.setCustomer(aCustomer)
        # Assignment between customer and boat 
        self.assignBoatToCustomer(aCustomer)
        self._serviceRecord = []

    def tellAboutSelf(self):
        """ Description: Report the attributes of the boat
        INPUT: None
        OUTPUT: Print each attribute of the boat
        """
        boatDetails = "I am a Boat" + \
                      " state reg number " + str(self.getStateRegistrationNo()) + \
                      " length " + str(self.getLength()) + \
                      " Manufacturer " + str(self.getManufacturer()) + \
                      " Year " + str(self.getYear())
        customerDetails = "\n and Owner is " + str(self.getCustomer().getName()) + \
                          " living in " + str(self.getCustomer().getAddress()) + \
                          " with phone " + str(self.getCustomer().getPhoneNo())
        return boatDetails + customerDetails

    def assignBoatToCustomer(self, aCustomer):
        """ Description: associate this boat with the correct customer
        INPUT: Customer() object
        OUTPUT: None
        """
        aCustomer.setBoat(self)

    def addServiceRecord(self, record):
        self._serviceRecord.append(record)

    def printRecord(self):
        """ Description: 
        INPUT: Customer() object
        OUTPUT: None
        """
        service_record = self.getServiceRecord()
        if not self.getServiceRecord():
            print("No service record")
            return None
        for record in service_record:
            record.printForm()

    def setStateRegistrationNo(self, aStateRegistrationNo):
        self._stateRegistrationNo = aStateRegistrationNo

    def setLength(self, aLength):
        self._length = aLength

    def setManufacturer(self, aManufacturer):
        self._manufacturer = aManufacturer

    def setYear(self, aYear):
        self._year = aYear

    def setCustomer(self, aCustomer):
        self._customer = aCustomer

    def getStateRegistrationNo(self):
        return self._stateRegistrationNo

    def getLength(self):
        return self._length

    def getManufacturer(self):
        return self._manufacturer

    def getYear(self):
        return self._year

    def getCustomer(self):
        return self._customer

    def getServiceRecord(self):
        return self._serviceRecord
