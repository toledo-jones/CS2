#!/usr/bin/env python
# coding: utf-8

# !/usr/bin/env python3

""""
   Description:
      A service record contains details about the customer and boat.
   
   Functions:
      printForm
      getInvoiceNumber
      getServiceData
      getBoat
      getServiceType
      getTotalCharges
      setInvoiceNumber
      setServiceData
      setBoat
      setServiceType
      setTotalCharges
      
   Constants:
      None    

"""

__author__ = "Cody Bogausch"
__version__ = "1.0"

from Boat import Boat
from Customer import Customer

class BoatServiceRecord:
    def __init__(self, theInvoiceNumber, theServiceDate, theServiceType, theTotalCharges, aBoat):
        # Invoke mutators to populate attributes
        self.setInvoiceNumber(theInvoiceNumber)
        self.setServiceDate(theServiceDate)
        self.setServiceType(theServiceType)
        self.setTotalChargers(theTotalCharges)

        # Associate this service record with the boat
        aBoat.addServiceRecord(self)

        # Then set the boat with the service record added
        self.setBoat(aBoat)

    def printForm(self):
        """ Print all attributes associated with this service record """
        print("The invoice number is: " + str(self.getInvoiceNumber()))
        print("The service date is is: " + str(self.getServiceDate()))
        print("The service type is: " + str(self.getServiceType()))
        print("The boat information is: " + str(self.getBoat().tellAboutSelf()))
        print("The total charge is: " + str(self.getTotalCharges()))

    def getInvoiceNumber(self) -> int:
        """
        Get invoice number
        :returns: invoice number associated with this service record
        """
        return self._invoiceNumber

    def getServiceDate(self) -> str:
        """
        Get service date associated with the service record
        :returns: service date
        """
        return self._serviceDate

    def getBoat(self) -> Boat:
        """
        Get boat associated with this service record
        :returns: associated boat
        """
        return self._boat

    def getServiceType(self) -> str:
        """ 
        Get service type, type of service rendered
        :returns: type of service 
        """
        return self._serviceType

    def getTotalCharges(self) -> float:
        """
        Get total charges, cost of service rendered
        :returns: total charges
        """
        return self._totalCharges

    def setInvoiceNumber(self, theInvoiceNumber: int) -> None:
        """
        Set invoice number
        :param theInvoiceNumber: identifier for invoice number
        """
        self._invoiceNumber = theInvoiceNumber

    def setServiceDate(self, theServiceDate: str) -> None:
        """
        Set service date
        :param theServiceDate: date service was performed, looks like "January 1, 1999"
        """
        self._serviceDate = theServiceDate

    def setServiceType(self, theServiceType: str) -> None:
        """ 
        Set service type, type of service rendered
        :param theServiceType: service rendered
        :returns: None
        """
        self._serviceType = theServiceType

    def setTotalChargers(self, theTotalCharges: float) -> None:
        """ 
        Set total charges, cost of service
        :param theTotalCharges: service cost
        :returns: None
        """
        self._totalCharges = theTotalCharges

    def setBoat(self, aBoat: Boat):
        """
        Associate a boat to this service record
        :param aBoat: The boat which is associated with this service record
        """
        self._boat = aBoat
