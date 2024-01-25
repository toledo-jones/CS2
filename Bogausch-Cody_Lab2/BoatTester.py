#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Tester for the boat class   
"""

__author__ = "Prof. Mikijanic"
__version__ = "1.0"

from Boat import Boat
from Customer import Customer
from BoatServiceRecord import BoatServiceRecord

class BoatTester:

    firstCustomer = Customer("Eleanor", "Atlanta", "123-4567") 	
    firstBoat = Boat("MO34561", 28, "Tartan", 2002, firstCustomer)		
            
    a = BoatServiceRecord( 1, "Jan 21, 2010", "Engine repair", 1000.00, firstBoat)
    b = BoatServiceRecord( 2, "Jan 31, 2010", "Paint Stripping", 600.00, firstBoat)
    
    firstBoat.printRecord()

if __name__ == '__main__':
   tester = BoatTester()