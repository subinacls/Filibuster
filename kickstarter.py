# encoding: utf-8
#!/usr/bin/env python

"""
This application is useful for mapping egress filters for a network in which has some port filtering device between you
and another network segment. This can be the internet or used throughout different vlans etc etc. Use is based on INI
configuration file for the client portion of the application.
"""

""" standard lib imports here """

import __builtin__ as __builtin__
import sys
import thread
import datetime
#import socket as socket; __builtin__.socket = socket
import os
global ipaddr
__builtin__.ipaddr = "127.0.0.1"
global hostip
__builtin__.hostip = ""
global stack
__builtin__.stack = []
import numpy as np
global date
date = str(datetime.datetime.now()).split()[0]
__builtin__.date = date
__builtin__.u = 0

""" useful for diagnostics and error suppression """
__builtin__.diag = "yes"
__builtin__.dd = {}
"""
warning:
	running diagnostics will slow down the scanning process
	use only when adding modules to view the data flow
	You have been informed
"""

""" enable or disable diagnostics output """
__builtin__.suppress = "yes"
""" suppress error msgs from try and other exception handling """

""" list required directories for application to import custom modules """
directories = ["client", "color", "config", "covert", "diag", "error", "help", "iptables", "log", "server", "socket", "version"]

""" for each directory append to system $PATH for custom module importing """
for inc in directories:
	sys.path.append(os.getcwd()+"/"+inc)

""" import modules after directory structure appended to system $PATH """
from client_kicker import initclient
from bcolors import bcolors as b
from diagforall import diagclientheader as diagclientheader
import verinfo as verinfo
from pcolors import printfunction as printfunction
from helper import helper as helper
from diagforall import csconf as csconf
import verinfo
from diagforall import diagclientheader, modimporttest, ctest

print ""

if diag == "yes":
	diagclientheader().clientheader()

""" do an import test on all modules """
if diag == "no":
	modimporttest().runimporttest()

""" set some color variable shortcuts """
__builtin__.bh = b.HEADER
__builtin__.bf = b.FAIL
__builtin__.be = b.ENDC
__builtin__.bw = b.WARNING
__builtin__.bo = b.OKBLUE

""" do some basic testing of the colorization module """
if diag == "yes":
	ctest().colortest()

"""check for user supplied argument in position 1, assume blank is assumption """
try:
	if str(sys.argv[1]):
		""" set sa1 var to sys argument 1 """
		__builtin__.sa1 = str(sys.argv[1])
except Exception as nofirstargument:
	print "hit an exception in kickstarter.py no first argument: " + str(nofirstargument)
	helper().helpall()
	sys.exit(0)

""" function to check first user supplied argument before execution """
def checkfirstargument():
	try:
		print "checkfirstargument"
		if str(sa1).lower() in ["client","c"]: # if your looking for the client portion
			from client_kicker import initclient
			from scanconfig import initscanner
			from diagforall import checkdepends
			from diagforall import diagclientheader # import some functionality
			try:
				checkdepends().required_mods() # check dependencies before launch
			except Exception as requiredmodsfail: # if anything failed here
				if diag == "yes":
					print "hit an exception in checkdepends.py - required_mods(): " + str(requiredmodsfail)
				helper().helpall()
				sys.exit(0)
			try:
				initclient().clientrun() # run client kicker
			except Exception as clientrunfail: # if anything failed here
				if diag == "yes":
					print "hit an exception in initclient.py clientrun(): " + str(clientrunfail)
				helper().helpall()
				sys.exit(0)
			try:
				initscanner().scanengine() # configure and run scanning engine
			except Exception as scanenginefail: # if anything failed here
				if diag == "yes":
					print "hit an exception in initscanner.py scanengine(): " + str(scanenginefail)
				helper().helpall()
				sys.exit(0)
		if str(sa1).lower() in ["server", "s"]: # if your looking for the server portion
			print "server initialized"
			from servargs import args
			args().getservargs()
			from server_kicker import initserver # import some functionality
			try:
				initserver().serverrun()
			except Exception as serverrunfail:
				print "hit an exception in initserver.py serverrun(): " + str(serverrunfail)
			pass
		else:
			print "no servers found"
			helper().helpall() # get some help
			sys.exit(0)
	except Exception as nofirstargument:
		print "hit an exception in kickstarter.py last exception nofirstargument: " + str(nofirstargument)
		helper().helpall()
		sys.exit(0)

""" pain in the __main__ """
if __name__ == "__main__":
	print "Test1"
	"""  run checkfirstargument function """
	checkfirstargument()