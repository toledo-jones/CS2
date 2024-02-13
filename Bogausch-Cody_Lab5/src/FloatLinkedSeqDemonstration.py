#!/usr/bin/env python
# coding: utf-8

#!/usr/bin/env python3

""""
   Description:
      # Tester file for LinkedSeq.py
      # This demonstration program is a test of the LinkedSeq class
"""

__author__ = "Prof. Mikijanic"
__version__ = "1.0"

from LinkedSeq import *

class FloatLinkedSeqDemonstration:
   def main():
      s = LinkedSeq()
      for element in range(1, 11):
         s.addAfter(float(element))
      print("sequence s")
      s.print()

      t = s.clone()
      print("sequence t after clone from s")
      t.print()
      t.addAfter(-1.0) 
      t.addAfter(-2.0)
      t.start()
      for i in range(4):
         t.advance()
      t.addAfter(11.0) 
      t.addAfter(12.0)
      print("sequence t after addAfter")
      t.print()

      u = t.clone()
      print("sequence u after clone from t")
      u.print()
      u.start()
      for i in range(5):
         u.advance()
      u.removeCurrent() 
      u.removeCurrent()
      print("sequence u after removeCurrent")
      u.print()

      v = s.clone()
      print("sequence v after clone from s")
      v.print()
      v.start()
      v.addBefore(-1.0) 
      v.addBefore(-2.0)
      for i in range(6):
         v.advance()
      v.addBefore(11.0) 
      v.addBefore(12.0)
      print("sequence v after addBefore")
      v.print()
      v.addAll(s)
      print("sequence v after addAll(s)")
      v.print()

      w = LinkedSeq.catenation(s,t)
      print("sequence w = s + t")
      w.print()

      x = LinkedSeq()
      print("sequence x")
      x.print()
      print(x.getCurrent())

   if __name__ == "__main__":
      main()