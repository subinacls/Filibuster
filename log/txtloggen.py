#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#
'''
This file generates the txt log
'''

class txtlogfilegen:
  def __init__(self):
    pass
  def txtlog(self, proto, ipaddr, consultant, location, ldate, base_port, dft,state):
    with open(str(consultant)+'-'+str(location)+'-'+str(ldate)+'.txt', 'a', buffering=0) as txtlogwrite:
      txtlogwrite.write("Location: "+str(consultant)+" State: "+str(state) + " IP: "+str(ipaddr) +" Proto: "+str(proto)+" Port: "+ str(base_port)+ " Consultant: " +str(location)+" Date: "+str(dft))
      txtlogwrite.close()
