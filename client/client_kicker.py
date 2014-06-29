#!/usr/bin/env python

"""
encoding: utf-8
module author: subinacls

Used to check for dependencies required for operation
collect user arguments for processing
check configuration ini file
kick off configuration parser
"""

import __builtin__
import sys
import time
import re
import os
import verinfo
from diagforall import clientconfdiag

van = __appname__
vv = __version__

class initclient():

	"""
	"""
	""" checking for required dependencies before any further execution """
	""" if dependency is not found, print helper text to install modules """

	def __init__(self):
		pass

	def check_depends(self):
		# check depends ,,, the joke writes it's self...
		#print "Start checking for dependencies" # diagnostics
		try:
			""" required for graphing """
			import numpy as np
		except Exception as nonumpyinstalled:
			print bo + "\n\n\t" + be + "[?] Please install numpy with: easy_install numpy"
			if str(diag).lower() in ["true", "yes"]:
				print bo + "\n\n\t" + be + "[?] Dependency exception caught as: " + str(nonumpyinstalled)
			sys.exit(0)
		try:
			""" import configparser for user supplied configuration file """
			import ConfigParser
		except Exception as noconfigparserinstalled:
			print bo + "\n\n\t" + be + "[?] Please install ConfigParser with: easy_install configparser"
			if str(diag).lower() in ["true", "yes"]:
				print bo + "\n\n\t" + be + "[?] Dependency exception caught as: " + str(noconfigparserinstalled)
			sys.exit(0)
		try:
			""" required for covert testing """
			import dns.resolver
		except Exception as covertdnsimportfail:
			print bo + "\n\n\t" + be + "[?] Please install python DNS module with: easy_install dnspython"
			if str(diag).lower() in ["true", "yes"]:
				print bo + "\n\n\t" + be + "[?] Dependency exception caught as: " + str(covertdnsimportfail)
			sys.exit(0)
		#print "End checking for dependencies" # diagnostics

	""" starting client portion of the application """
	def clientrun(self):
		"""
		"""
		""" check for system argument to initialize client portion of application """
		""" log start time of application """
		__builtin__.start_timer = time.time()
		try:
			is_host = re.match(
				"^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$"
				, ipaddr)
			if is_host:
				__builtin__.host_ip = socket.gethostbyname(ipaddr)
			else:
				__builtin__.hostip == ipaddr
				pass
		except Exception as csetvarfail:
			print bo + "\n\n\t" + be + "[?] Could not set hostip address from ipaddress in conf.py" + str(csetvarfail)
		""" get system argument 2 which handles the configuration INI file"""
		try:
			__builtin__.conffile = sys.argv[2]
		except Exception as conffilefail:
			from helper import helper
			print bo + "\n\n\t[?] Please ensure all arguments are given\n" + be
			helper().chelp()
			sys.exit(0)
		""" get system argument 3, which handles SSL/TLS - addin extra encryption layer ( AES ) """
		try:
			if not sys.argv[3]:
				__builtin__.mytls = ""
			else:
				__builtin__.mytls = str(sys.argv[3])
		except Exception as nosysarg3:
			from helper import helper
			print bo + "\n\n\t[?] Please ensure all arguments are given\n" + be
			helper().chelp()
			sys.exit(0)
		""" set vars to user input provided from INI file from system argument 3 """
		try:
			if conffile:  # if var is set from system argument import confsecmap
				try:
					from conf import confsecmap
				except Exception as confsecmapfail:
					print("Failed at system argument configuration in main.py: " + str(confsecmapfail))
				""" check and make sure its a file and not some malicious user input """
				if os.path.isfile(sys.argv[2]):
					confsecmap
				#print "Client config diagnostics before" # diagnostics
				clientconfdiag().diagconfig
				#print "Client config diagnostics after" # diagnostics
		except Exception as conffilefail:
			from helper import helper
			print bo + "\n\n\t[?] Please ensure all arguments are given\n" + be
			helper().chelp()
			sys.exit(0)