#!/usr/bin/env python
# encoding: utf-8
"""
module author: subinacls

Some diagnostics was added to the application
To enable these print statements, remove all the starting # from lines ending in # diagnostics

This application is useful for mapping egress filters and simple covert tunnel testing
for a network which has a port filtering device bewtween you and another segment.

This can be used for internet access or vlans etc etc.
Client is enabled from the command line providing an INI file
Clients variables are taken from the supplied INI file
Server is configured from command line arguments

warning:
	running diagnostics will slow down the scanning process
	use only when adding modules to view the data flow
	You have been informed
"""

import __builtin__
import sys
import datetime
import os
__builtin__.ipaddr = "127.0.0.1"
__builtin__.hostip = ""
__builtin__.stack = []
global ident
__builtin__.ident = ""
date = str(datetime.datetime.now()).split()[0]
__builtin__.date = date
__builtin__.u = 0
""" useful for diagnostics and error suppression """
__builtin__.diag = ""
__builtin__.dd = {}
""" enable or disable error msg output """
__builtin__.suppress = "yes"

""" list required directories for application to import custom modules """
directories = ["client",
               "color",
               "config",
               "covert",
               "diag",
               "dlp",
               "error",
               "encoder",
               "help",
               "iptables",
               "log",
               "server",
               "socket",
               "version"]

""" for each directory append to system $PATH for custom module importing """
for inc in directories:
	sys.path.append(os.getcwd() + "/" + inc)

""" import modules after directory structure appended to system $PATH """
from bcolors import bcolors as b
import pcolors
from diagforall import diagclientheader
from diagforall import diagserverheader
import verinfo as verinfo
from pcolors import printfunction as printfunction
from helper import helper as helper
from diagforall import csconf as csconf
import verinfo
from diagforall import diagclientheader, modimporttest, ctest
from diagforall import piechartdiag

""" do an import test on all modules """
modimporttest().runimporttest()

""" set some color variable shortcuts """
__builtin__.bh = b.HEADER
__builtin__.bf = b.FAIL
__builtin__.be = b.ENDC
__builtin__.bw = b.WARNING
__builtin__.bo = b.OKBLUE

""" do some basic testing of the colorization module """
ctest().colortest()

"""check for user supplied argument in position 1, assume blank is assumption """
try:
	__builtin__.sa1 = str(sys.argv[1])
except Exception as nofirstargument:
	print bo + "\n\n\t[?] Please ensure all arguments are given\n" + be
	helper().helpall()
	sys.exit(0)

""" function to check first user supplied argument before execution """


def checkfirstargument():

	try:  # if your looking for the client portion
		if str(sa1).lower() in ["client", "c"]:
			from client_kicker import initclient
			from scanconfig import initscanner
			from diagforall import checkdepends
			from diagforall import diagclientheader
			try:
				#print 'Check depends before' # diagnostics
				checkdepends().required_mods()  # check dependencies before launch
				#print 'Check depends after' # diagnostics
			except Exception as requiredmodsfail:  # if anything failed here
				print bo + "\n\n\t[?] Please ensure all dependencies are installed\n" + be
				helper().chelp()
				sys.exit(0)
			try:
				#print 'Check client header before' # diagnostics
				diagclientheader().clientheader()
				#print 'Check client header after' # diagnostics
				#print 'Check client run before' # diagnostics
				initclient().clientrun()  # run client kicker
				#print 'Check client run after' # diagnostics
			except Exception as clientrunfail:  # if anything failed here
				print bo + "\n\n\t[?] Please ensure all arguments are given\n" + be
				helper().chelp()
				sys.exit(0)
			try:
				#print 'Check scanengine before' # diagnostics
				initscanner().scanengine()  # configure and run scanning engine
				#print 'Check scanengine atfer' # diagnostics
			except Exception as scanenginefail:  # if anything failed here
				print bo + "\n\n\t[?] Please ensure all arguments are given\n" + be
				helper().chelp()
				sys.exit(0)
		if str(sa1).lower() in ["server", "s"]:  # if your looking for the server portion
			__builtin__.diag = "yes"  # since server does not get settings from ini file
			try:
				from servargs import args
				#print "Check server argument before" # diagnostics
				args().getservargs()
				#print "Check server argument after" # diagnostics
				try:
					from server_kicker import initserver
					#print "Check initserver before" # diagnostics
					initserver().serverrun()
					#print "Check initserver after" # diagnostics
				except Exception as serverrunfail:
					print bo + "\n\n\t[?] Please ensure all variables are given\n" + be
				pass
			except Exception as serverinitfail:
				print bo + "\n\n\t[?] Failed server initialization" + str(serverinitfail)
	except Exception as nofirstargument:
		print bo + "\n\n\t[?] Please ensure all arguments are given\n" + be
		helper().helpall()
		sys.exit(0)

""" pain in the __main__ """
if __name__ == "__main__":
	"""  run checkfirstargument function """
	#print "Run checkfirstargument before" # diagnostics
	checkfirstargument()
	#print "Run checkfirstargument after" # diagnostics
	"""for diagnostics display a pie chart"""
	from diagforall import piechartdiag
	piechartdiag().getaslice()
	if str(covert).lower() in ["true", "yes"]:
		from covert import icmptunnel, ntptunnel, dnstunnel
		""" set basic list for gathering for covert tunnel testing """
		__builtin__.tunnelspass = []
		__builtin__.tunnelsfail = []
		""" initalize tunnel testing """
		""" actual covert testing calls to the previous set classes """
		icmptunnel().ping(tunnelspass, tunnelsfail)
		ntptunnel().ntp(tunnelspass, tunnelsfail)
		dnstunnel().dnsres(tunnelspass, tunnelsfail)
		""" print findings for covert testing """
		if str(tunnelspass) != "[]":
			print(bh + "\n\t[-] List of passed Covert tunnels ...\n" + be)
			printfunction().pfunc("\t\t[!] Cover tunnel: ", str(tunnelspass))
		if str(tunnelsfail) != "[]":
			print(bh + "\n\t[-] List of failed Covert tunnels ...\n" + be)
			printfunction().pfunc("\t\t[!] Cover tunnel: ", str(tunnelsfail))
		from jsonloggen import jsonlogger
		jsonlogger().jsontunnellog()
	print ""
