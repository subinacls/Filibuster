# encoding: utf-8
#!/usr/bin/env python
#
# module author: subinacls
#


""" Useful information
Used to check for dependencies required for operation
run client user argument variables
check configuration ini file
kick off configuration parser
"""

import __builtin__

class initclient():
	
	def __init__(self):
		pass

	""" checking for required dependencies before any further execution """
	""" if dependency is not found, print helper text to install modules """
	def check_depends(self):
		# check depends ,,, the joke writes it's self...
		try:
			""" required for graphing """
			import numpy as np
		except Exception as nonumpyinstalled:
			print("Please install numpy with: easy_install numpy")
			if diag == "yes":
				print "Dependency exception caught as: " +str(nonumpyinstalled)
			sys.exit()
		try:
			""" import configparser for user supplied configuration file """
			import ConfigParser
		except Exception as noconfigparserinstalled:
			print("Please install ConfigParser with: easy_install configparser")
			if diag == "yes":
				print "Dependency exception caught as: " +str(noconfigparserinstalled)
			sys.exit()
		try:
			""" required for covert testing """
			import dns.resolver
		except Exception as covertdnsimportfail:
			print("Please install python DNS module with: easy_install dnspython")
			if diag == "yes":
				print "Dependency exception caught as: " +str(covertdnsimportfail)
			sys.exit()

	""" starting client portion of the application """
	def clientrun(self):
		"""
		"""
		""" check for system argument to initialize client portion of application """
		""" log start time of application """
		__builtin__.start_timer = time.time()
		try:
			is_host = re.match("^(([a-zA-Z]|[a-zA-Z][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z]|[A-Za-z][A-Za-z0-9\-]*[A-Za-z0-9])$", ipaddr)
			if is_host:
				__builtin__.host_ip = socket.gethostbyname(ipaddr)
			else:
				__builtin__.hostip == ipaddr
				pass

		except Exception as  csetvarfail:
			print "could not set hostip address from ipaddress in conf.py" + str(csetvarfail)

		""" get system argument 2 which handles the configuration INI file"""
		try:
			__builtin__.conffile = sys.argv[2]
		except Exception as conffilefail:
			if diag == "yes":
				print("\n"+bh +"[*] " + "-"*80 + be+"\n")
				print("\t"+bf+"ATTENTION "+be+bw+"[?] SYSARG position 2 has "+bf+"FAILED"+be+bw+" due to absence"+be)
				print("\t[?] " +van+" v."+vv+" - CRASHED: " + bf + str(conffilefail) + "\n" +be)
			print("")
			from helper import helper
			helper().chelp()
			sys.exit(0)
		""" get system argument 3, which handles SSL/TLS - addin extra encryption layer due to heartbleed """
		try:
			if not sys.argv[3]:
				__builtin__.mytls = ""
			else:
				__builtin__.mytls = str(sys.argv[3])
		except Exception as nosysarg3:
			if diag == "yes":
				print("\n"+bh +"[*] " + "-"*80 + be+"\n")
				print("\t"+bf+"ATTENTION "+be+bw+"[?] SYSARG position 3 is "+bf+str(mytls)+be+bw+be)
				print("\t[?] " +van+" v."+vv+" - CRASHED: " +
				      bf + str(nosysarg3) + "\n" +be)
			print("")
			from helper import helper
			helper().chelp()
			sys.exit(0)
		""" set vars to user input provided from INI file from system argument 3 """
		try:
			if conffile: # if var is set from system argument import confsecmap
				try:
					from conf import confsecmap
				except Exception as confsecmapfail:
					print("Failed at system argument configuration in main.py: " + str(confsecmapfail))
				""" check and make sure its a file and not some malicious user input """
				if os.path.isfile(sys.argv[2]):
					confsecmap
				if diag == "yes":
					from diagforall import clientconfdiag
					clientconfdiag().diagconfig
		except Exception as conffilefail:
			if diag == "yes":
				print("\n"+bh +"[*] " + "-"*80 + be+"\n")
				print("\t"+bf+"ATTENTION "+be+bw+"[?] config file failed "+bf+str(conffilefail)+be+bw+be)
				print("\t[?] " +van+" v."+vv+" - CRASHED: " + bf + str(nosysarg3) + "\n" +be)
			print("")
			from helper import helper
			helper().chelp()
			sys.exit(0)