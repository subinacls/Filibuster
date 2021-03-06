#!/usr/bin/python2
# encoding: utf-8
#
# module author: subinacls
#

""" Useful information
exactly what it says - handles all the printing of diagnostic information
"""
import __builtin__
import sys
from bcolors import bcolors as b
from diagfun import diagfun

__builtin__.bh = b.HEADER
__builtin__.bf = b.FAIL
__builtin__.be = b.ENDC
__builtin__.bw = b.WARNING
__builtin__.bo = b.OKBLUE

pfunc = diagfun().pfunc
pfuncok = diagfun().pfuncok
pfuncbad = diagfun().pfuncbad


class checkdepends(object):

	def __init__(self):
		pass

	def required_mods(self):
		if str(diag).lower() in ["true", "yes"]:
			print "Test1"
			print bh + "\t[-] Checking for required modules for proper operation\n" + be
			try:
				import numpy as np
				print bo + "\t\t[-] Numpy module passed" + be
			except Exception as numpy_fail:
				print bf + "\t\t[-] Numpy module failed" + be
				print bf + "\t[!] Please install numpy with easy_install numpy, error: " + \
				      str(numpy_fail) + "\n" + be
				sys.exit()
			try:
				import ConfigParser
				print bo + "\t\t[-] Config Parser module passed" + be
			except Exception as cparser:
				print bf + "\t\t[-] Config Parser module failed" + be
				print bf + "\t[!] Please install ConfigParser with easy_install configparser, error: " + \
				      str(cparser) + "\n" + be
				sys.exit()
			try:
				import dns.resolver
				print bo + "\t\t[-] DNS Resolver module passed\n" + be
			except Exception as dns_res:
				print bf + "\t\t[-] Dns.Resolver module failed" + be
				print bf + "\t[!] Please install python DNS module with easy_install dnspython, error: " + \
				      str(dns_res) + "\n" + be
				sys.exit()


class csconf(object):

	def __init__(self):
		pass

	def clientsockconf(self):
		if str(diag).lower() in ["true", "yes"]:
			print bh + "\t\t[-] Diagnostics for client socket configuration\n" + be
			pfunc("\t\t\t[!] STACK randomness is set to: ", str(randomness))
			pfunc("\t\t\t[!] STACK length: ", str(len(stack)))
			pfunc("\t\t\t[!] Start port is set to: ", str(lowport))
			pfunc("\t\t\t[!] End port is: ", str(highport))
			pfunc("\t\t\t[!] Process count is set to: ", str(u))
			print("")



class portrng(object):

	def __init__(self):
		pass

	def prange(self):
		if str(diag).lower() in ["true", "yes"]:
			print bh + "\t[-] Diagnostics for portrange parameters\n" + be
			pfunc("\t\t[!] Port range is: ", str(portr))
			pfunc("\t\t[!] Lowport is: ", str(lowport))
			pfunc("\t\t[!] Highport is: ", str(highport))
			if str(fb) in ["both", "b"]:
				pfunc("\t\t[!] Total ports to scan: ",
				      str(int(highport) - int(lowport) + int(highport) - int(lowport) + 1))
			else:
				pfunc("\t\t[!] Total ports to scan: ", str(int(highport) - int(lowport) + 1))
			pfunc("\t\t[!] Starting port is: ", str(lowport))
			pfunc("\t\t[!] Ending port is: ", str(end_port))
			pfunc("\t\t[!] Start time and date is: ", str(ldate))



class ctsc(object):

	def __init__(self):
		pass

	def clienttcpsockconf(self):
		if str(diag).lower() in ["true", "yes"]:
			print bh + "\n\t[-] Diagnostics for TCP Socket Creator\n" + be
			pfunc("\t\t[!] Total ports in stack to test: ", str(total_stack))
			pfunc("\t\t[!] Counter incremented per test: ", str(u))
			pfunc("\t\t[!] IP sent to TCP socket creator: ", str(ipaddr))
			pfunc("\t\t[!] Server port sent to socket creator: ", str(ls))
			pfunc("\t\t[!] Consultants name sent to TCP socket creator: ", str(consultant))
			pfunc("\t\t[!] Testing location sent to TCP socket creator: ", str(location))



class cusc(object):

	def __init__(self):
		pass

	def clientudpsockconf(self):
		if str(diag).lower() in ["true", "yes"]:
			print bh + "\n\t[-] Diagnostics for UDP Socket Creator\n" + be
			pfunc("\t\t[!] Total ports in stack to test: ", str(total_stack))
			pfunc("\t\t[!] Counter incremented per test: ", str(u))
			pfunc("\t\t[!] IP sent to UDP socket creator: ", str(ipaddr))
			pfunc("\t\t[!] Server port sent to socket creator: ", str(ls))
			pfunc("\t\t[!] Consultants name sent to UDP socket creator: ", str(consultant))
			pfunc("\t\t[!] Testing location sent to UDP socket creator: ", str(location))



class diagserverheader(object):

	def serverheader(self):
		if str(diag).lower() in ["true", "yes"]:
			print bh + "\t[-] Displaying Application Development Information\n" + be
			pfunc("\t\t[!] Application Codename: ", __appname__)
			pfunc("\t\t[!] Application Functionality: ", "Server")
			pfunc("\t\t[!] Original Author: ", __author__)
			pfunc("\t\t[!] Year of Conception: ", __concept__)
			pfunc("\t\t[!] Credits Given: ", __credits__)
			pfunc("\t\t[!] License version: ", __license__)
			pfunc("\t\t[!] Application Version: ", __version__)
			pfunc("\t\t[!] Application Maintainer: ", __maintainer__)
			pfunc("\t\t[!] Development Status: ", __status__)
			print ""



class diagclientheader(object):

	def __init__(self):
		pass

	def clientheader(self):
		if str(diag).lower() in ["true", "yes"]:
			print bh + "\t[-] Displaying Application Development Information\n" + be
			pfunc("\t\t[!] Application Codename: ", __appname__)
			pfunc("\t\t[!] Application Functionality: ", "Client")
			pfunc("\t\t[!] Original Author: ", __author__)
			pfunc("\t\t[!] Years of development: ", __concept__)
			pfunc("\t\t[!] Credits Given: ", __credits__)
			pfunc("\t\t[!] License version: ", __license__)
			pfunc("\t\t[!] Application Version: ", __version__)
			pfunc("\t\t[!] Application Maintainer: ", __maintainer__)
			pfunc("\t\t[!] Development Status: ", __status__)
			print ""


class clientconfdiag(object):

	def __init__(self):
		pass

	def diagconfig(self):
		if str(diag).lower() in ["true", "yes"]:
			print bh + "\t[-] Displaying client configuration information\n" + be
			pfunc("\t\t[!] Client target server: ", ipaddr)
			pfunc("\t\t[!] Client scan type: ", scantype)
			pfunc("\t\t[!] Do we spoof the source: ", spoofipaddr)
			pfunc("\t\t[!] Configured portrange: ", portr)
			pfunc("\t\t[!] Client protocol to use: ", flipbit)
			pfunc("\t\t[!] Consultant who is scanning: ", consultant)
			pfunc("\t\t[!] Location of consultant: ", location)
			pfunc("\t\t[!] Do we randomize the ports: ", randomness)
			pfunc("\t\t[!] Random or Static sleep: ", sleepy)
			pfunc("\t\t[!] How long do we sleep: ", nappy)
			pfunc("\t\t[!] How long is the dwell: ", rester)
			pfunc("\t\t[!] Do we suppress error: ", suppress)
			pfunc("\t\t[!] Are we logging the scan: ", logging)
			pfunc("\t\t[!] How are we storing it: ", logtype)
			pfunc("\t\t[!] Are we testing covert tunnels: ", covert)
			print ""



class modimporttest(object):

	def __init__(self):
		pass

	def runimporttest(self):
		if str(diag).lower() in ["true", "yes"]:
			if str(diag).lower() in ["true", "yes"]:
				print bh + "\n\t[-] Module importing testing\n" + be
				import verinfo
				pfunc("\t\t[-] Version module imported ", "successfully")
				import client_kicker
				pfunc("\t\t[-] Client_kicker module imported ", "successfully")
				import scanconfig
				pfunc("\t\t[-] Scanconfig module imported ", "successfully")
				import diagfun
				pfunc("\t\t[-] Diagfun module imported ", "successfully")
				import killswitch
				pfunc("\t\t[-] Killer module imported ", "successfully")
				import helper
				pfunc("\t\t[-] Helper module imported ", "successfully")
				from bcolors import bcolors as b
				pfunc("\t\t[-] Color module imported ", "successfully")
				import pcolors
				pfunc("\t\t[-] Fancy module imported ", "successfully")
				import csvloggen
				pfunc("\t\t[-] CSV logging module imported ", "successfully")
				import txtloggen
				pfunc("\t\t[-] TXT logging module imported ", "successfully")
				import xmlloggen
				pfunc("\t\t[-] XML logging module imported ", "successfully")
				import jsonloggen
				pfunc("\t\t[-] JSON logging module imported ", "successfully")
				import servargs
				pfunc("\t\t[-] Server arguments module imported ", "successfully")
				import server_func
				pfunc("\t\t[-] Server function module imported ", "successfully")
				import threadedtcpserver
				pfunc("\t\t[-] Threaded TCP server module imported ", "successfully")
				import threadedudpserver
				pfunc("\t\t[-] Threaded UDP server module imported ", "successfully")
				print ""



class ctest(object):

	def __init__(self):
		pass

	def colortest(self):
		if str(diag).lower() in ["true", "yes"]:
			from bcolors import bcolors as b
			bh = b.HEADER
			bf = b.FAIL
			be = b.ENDC
			bw = b.WARNING
			bo = b.OKBLUE
			bg = b.OKGREEN
			print bh + "\t[!] Colorization Diagnostics and testing\n" + be
			print bh + "\t\t[-] This is the HEADER color test" + be
			print bf + "\t\t[-] This is the FAIL color test" + be
			print bw + "\t\t[-] This is the WARNING color test" + be
			print bo + "\t\t[-] This is the OKBLUE color test" + be
			print bg + "\t\t[-] This is the OKGREEN color test" + be + "\n"



class socktesting(object):

	def __init__(self):
		pass

	def sockdiag(self):
		if str(diag).lower() in ["true", "yes"]:
			pfunc("\t\t[!] Target scan type: ", str(scantype))
			if hostip != ipaddr:
				pfunc("\t\t[!] Target host is: ", str(ipaddr))
			else:
				pfunc("\t\t[!] Target host is: ", str(hostip))
			pfunc("\t\t[!] Total port count: ", str(len(stack)))
			pfunc("\t\t[!] Current port count: ", str(u))
			if len(passlist) != 0:
				pfuncok("\n\t\t[!] Passlist " + be + str(len(passlist) + 1) + ":", str(passlist[-6:-1:]))
			else:
				pfuncok("\n\t\t[!] Passlist " + be + str(len(passlist)) + ":", str(passlist[-6:-1:]))
			if len(faillist) != 0:
				pfuncbad("\n\t\t[!] Faillist " + be + str(len(faillist) + 1) + ":", str(faillist[-6:-1:]))
			else:
				pfuncbad("\n\t\t[!] Faillist " + be + str(len(faillist)) + ":", str(faillist[-6:-1:]))
			print ""



class piechartdiag(object):

	def __init__(self):
		pass

	def getaslice(self):
		if str(diag).lower() in ["true", "yes"]:
			if str(sa1).lower() in ["client", "c"]:
				import matplotlib
				matplotlib.use('Agg')
				import matplotlib.pyplot as plt
				pll = len(passlist)
				fll = len(faillist)
				from pylab import gcf
				from pylab import pie
				from pylab import show
				fracs = [fll, pll]
				fig = gcf()
				fig.canvas.set_window_title(str(consultant) + "-" + str(ipaddr))
				mycolors=['red', 'green']
				mylabels=['Failed :'+str(fll), 'Passed: '+str(pll)]
				pie(fracs, labels=mylabels, colors=mycolors)
				plt.savefig(str(consultant) + "-" + str(location) + "-" + str(date))
