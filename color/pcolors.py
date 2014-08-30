#!/usr/bin/python2
# encoding: utf-8
#
# module author: subinacls
#


""" Useful information
colorization  handled in this file
"""


class printfunction(object):

	def __init__(self):
		pass

	def pfunc(self, userstr, var):
		collen = 95
		pip = bo + userstr + be
		pips = " " + var
		pipri = pip + pips.rjust((collen - len(pip)), '.')
		print pipri