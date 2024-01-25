
#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      A boat is owned by a customer and has related details attached.
   Functions:
      ???
   Constants:
      ??? 
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
    def __init__(self, aStateRegistrationNo, aLength, aManufacturer, aYear, aCustomer):
    
        self.setStateRegistrationNo(aStateRegistrationNo)
        self.setLength(aLength)
        self.setManufacturer(aManufacturer)
        self.setYear(aYear)
        self.setCustomer(aCustomer)
        # association between boat and customer done here
        self.assignBoatToCustomer(aCustomer)
        self._serviceRecord = []     
    
    def tellAboutSelf(self):
    
        boatDetails = "I am a Boat" +\
            " state reg number " + str(self.getStateRegistrationNo()) +\
            " length " + str(self.getLength()) +\
            " Manufacturer " + str(self.getManufacturer()) +\
            " Year " + str(self.getYear())
        customerDetails = "\n and Owner is " + str(self.getCustomer().getName()) +\
            " living in " + str(self.getCustomer().getAddress()) +\
            " with phone " + str(self.getCustomer().getPhoneNo())
        return boatDetails + customerDetails
      
    def assignBoatToCustomer(self, aCustomer):
        aCustomer.setBoat(self)
    
    def addServiceRecord(self, record):
        self._serviceRecord.append(record)
      
    def printRecord(self):
        service_record = self.getServiceRecord()
        if self.getServiceRecord():
            print("No service record")
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