#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      A service record contains details about the customer and boat.
   Functions:
      ???
   Constants:
      ???    

"""

__author__ = "???"
__version__ = "1.0"

class BoatServiceRecord:
    
    def __init__(self, theInvoiceNumber, theServiceDate, theServiceType, theTotalCharges, aBoat):
        # invoke assessors to populate attributes
        self.setInvoiceNumber(theInvoiceNumber)
        self.setServiceDate(theServiceDate)
        self.setServiceType(theServiceType)
        self.setTotalChargers(theTotalCharges)
        aBoat.addServiceRecord(self)
        self.setBoat(aBoat)
        
        
    def printForm(self):
            print("The invoice number is: " + str(self.getInvoiceNumber()))
            print("The service date is is: " + str(self.getServiceDate()))
            print("The service type is: " + str(self.getServiceType()))
            print("The boat information is: " + str(self.getBoat().tellAboutSelf()))         
            print("The total charge is: " + str(self.getTotalCharges()))
		
    def getInvoiceNumber(self):    
        return self._invoiceNumber    
    
    def getServiceDate(self):
        return self._serviceDate
    
    def getBoat(self):
        return self._boat
    
    def getServiceType(self):
        return self._serviceType
    
    def getTotalCharges(self):
        return self._totalCharges         
    
    def setInvoiceNumber(self, theInvoiceNumber):
        self._invoiceNumber = theInvoiceNumber
    
    def setServiceDate(self, theServiceDate):
         self._serviceDate = theServiceDate
    
    def setServiceType(self, theServiceType):
        self._serviceType = theServiceType
    
    def setTotalChargers(self, theTotalCharges):
        self._totalCharges = theTotalCharges
    
    def setBoat(self, aBoat):
        self._boat = aBoat