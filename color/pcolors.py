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

  def __init__(self):
      pass

  def pfunc(self, userstr, var):
      collen = 95
      pip = bo+ userstr + be
      pips = " " + var
      pipri = pip + pips.rjust((collen-len(pip)), '.')
      print pipri

