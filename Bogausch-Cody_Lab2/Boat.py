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

from Customer import Customer
from BoatServiceRecord import BoatServiceRecord

class Boat:
    def __init__(self,
                 aStateRegistrationNo: str,
                 aLength: int,
                 aManufacturer: str,
                 aYear: int,
                 aCustomer: Customer):
        # Constructor. Set Class Attributes
        self.setStateRegistrationNo(aStateRegistrationNo)
        self.setLength(aLength)
        self.setManufacturer(aManufacturer)
        self.setYear(aYear)
        self.setCustomer(aCustomer)
        # Assignment between customer and boat 
        self.assignBoatToCustomer(aCustomer)
        self.setServiceRecord([])

    def tellAboutSelf(self) -> str:
        """ 
        Report the attributes of this boat
        :returns String containing the boat details and customer details.
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

    def assignBoatToCustomer(self, aCustomer: Customer) -> None:
        """ 
        Associate this boat with the correct customer
        :param aCustomer: The customer associated with this boat
        """
        aCustomer.setBoat(self)

    def addServiceRecord(self, record: BoatServiceRecord) -> None:
        """
        Add a record of a service rendered to this boat
        :param record: the service record
        """
        self.getServiceRecord().append(record)

    def printRecord(self) -> None:
        """ 
        Print the record of all services rendered to this boat
        """
        # Locate the service record
        service_record = self.getServiceRecord()
        
        if not service_record:
            print("No service record")
            # If we do not find a service record return early
            return None
        
        # Print the form for each record in the service record list
        for record in service_record:
            record.printForm()


    def setStateRegistrationNo(self, aStateRegistrationNo: str) -> None:
        """
        Set state registration number
        :param aStateRegistrationNo: the unique identifier assigned to this boat
        """
        self._stateRegistrationNo = aStateRegistrationNo

    def setLength(self, aLength: int) -> None:
        """
        Set Length
        :param aLength: the length, in feet of this boat. A whole number
        """
        self._length = aLength

    def setManufacturer(self, aManufacturer: str) -> None:
        """
        Set manufacturer
        :param aManufacturer: the manufacturer associated with this boat
        """
        self._manufacturer = aManufacturer

    def setYear(self, aYear: int) -> None:
        """
        Set Year 
        :param aYear the year this boat was manufactured
        """
        self._year = aYear
    
    def setServiceRecord(self, aServiceRecord: list) -> None:
        """
        Set Service Record, should be initialized to an empty list
        :param store the initial values of the services that will be rendered to this boat
        """
        self._serviceRecord = aServiceRecord

    def setCustomer(self, aCustomer) -> None:
        """
        Set Customer
        :param Customer: customer associated with this boat
        """
        self._customer = aCustomer

    def getStateRegistrationNo(self) -> str:
        """
        Get State Registration Number
        :returns: unique registration number associated with this boat
        """
        return self._stateRegistrationNo

    def getLength(self) -> int:
        """
        Get Length
        :returns: Length: how long the boat is
        """
        return self._length

    def getManufacturer(self) -> str:
        """
        Get manufacturer
        :returns: Manufacturer: name of manufacturer
        """
        return self._manufacturer

    def getYear(self) -> int:
        """
        Get Year
        :returns: Year: Year this boat was manufactured
        """
        return self._year

    def getCustomer(self) -> Customer:
        """
        Get Customer
        :returns: Customer: customer associated with this boat
        """
        return self._customer


    def getServiceRecord(self) -> list[BoatServiceRecord]:
        """
        Get Service Record. 
        :returns: ServiceRecord: list of all BoatServiceRecord() 
        """
        return self._serviceRecord
