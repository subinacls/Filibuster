#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

""" Useful information
colorization of output handled in this file
"""

global userstr
global var
  
class printfunction:

  def __init__(self, userstr, var):
    self.userstr = userstr
    self.var = var

  def pfunc(self, userstr, var): 
    collen = 75 
    pip = bo+ userstr + be
    pips = " " + var 
    pipri = pip + pips.rjust((collen-len(pip)), '.') 
    print pipri

