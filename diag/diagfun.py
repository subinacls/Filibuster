#!/usr/bin/python2
# encoding: utf-8
#
# module author: subinacls
#

"""
This file is for pretty printing on stdout
"""


class diagfun(object):

	def __init__(self):
		pass

	def pfunc(self, userstr, var):
		from bcolors import bcolors
		collen = 95
		pip = bcolors.OKBLUE + userstr + bcolors.ENDC
		pips = " " + var
		pipri = pip + pips.rjust((collen - len(pip)), '.')
		print pipri

	def pfuncok(self, userstr, var):
		from bcolors import bcolors
		collen = 109
		pip = bcolors.OKBLUE + userstr + bcolors.ENDC
		pips = " " + bcolors.OKGREEN + var + bcolors.ENDC
		pipri = pip + pips.rjust((collen - len(pip)), '.')
		print pipri

	def pfuncbad(self, userstr, var):
		from bcolors import bcolors
		collen = 109
		pip = bcolors.OKBLUE + userstr + bcolors.ENDC
		pips = " " + bcolors.FAIL + var + bcolors.ENDC
		pipri = pip + pips.rjust((collen - len(pip)), '.')
		print pipri