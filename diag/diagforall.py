# encoding: utf-8
#!/usr/bin/env python
#
# module author: subinacls
#

""" Useful information
exactly what it says - handles all the printing of diagnostic information
"""

import sys
import binascii
from module_error_handling import modreporter as mp
from diagfun import diagfun
from bcolors import bcolors as b
import verinfo

bh = b.HEADER
bf = b.FAIL
be = b.ENDC
bw = b.WARNING
bo = b.OKBLUE
bg = b.OKGREEN

pfunc = diagfun().pfunc
pfuncok = diagfun().pfuncok
pfuncbad = diagfun().pfuncbad

class checkdepends():

	def __init__(self):
		pass

	def required_mods(self):

		if diag == "yes":
			print bh+"\t[-] Checking for required modules for proper operation\n"+be
			try:
				import numpy as np
				print bo+"\t\t[-] Numpy module passed"+be
			except Exception as numpy_fail:
				print bf+"\t\t[-] Numpy module failed"+be
				print bf+"\t[!] Please install numpy with easy_install numpy, error: "+str(numpy_fail)+"\n"+be
				sys.exit()
			try:
				import ConfigParser
				print bo+"\t\t[-] Config Parser module passed"+be
			except Exception as cparser:
				print bf+"\t\t[-] Config Parser module failed"+be
				print bf+"\t[!] Please install ConfigParser with easy_install configparser, error: "+str(cparser)+"\n"+be
				sys.exit()
			try:
				import dns.resolver
				print bo+"\t\t[-] DNS Resolver module passed\n"+be
			except Exception as dns_res:
				print bf+"\t\t[-] Dns.Resolver module failed"+be
				print bf+"\t[!] Please install python DNS module with easy_install dnspython, error: "+str(dns_res)+"\n"+be
				sys.exit()

class csconf():

	def __init__(self):
		pass

	def clientsockconf(self, randomness, stack, lowport, highport, u):
		try: # attempt
			print bh+"\t\t[-] Diagnostics for client socket configuration\n" + be
			pfunc("\t\t\t[!] STACK randomness is set to: ",str(randomness))
			pfunc("\t\t\t[!] STACK length: ",str(len(stack)))
			pfunc("\t\t\t[!] Start port is set to: ",str(lowport))
			pfunc("\t\t\t[!] End port is: ",str(highport))
			pfunc("\t\t\t[!] Process count is set to: ",str(u))
			print("")
		except Exception, csockconffail:
			print "\n"+bh +"[*] " + "-"*80 + be+"\n" 
			print "\t"+bf+"ATTENTION "+be+bw+"[?] Client diagnostics of sockets "+bf+"FAILED"+be+bw+" due to "+be+bf+str(csockconffail)+be
			sys.exit(0)

class portrng():

	def __init__(self):
		pass

	def prange(self, lowport, highport, end_port):
		try:
			print bh+"\t\t[-] Diagnostics for portrange parameters\n" + be
			pfunc("\t\t\t[!] target port range is: ",str(portr))
			pfunc("\t\t\t[!] target lowport is: ",str(lowport))
			pfunc("\t\t\t[!] target highport is: ",str(highport))
			if fb == "both" or fb == "Both" or fb == "BOTH" or fb == "b" or fb == "B":
				pfunc("\t\t\t[!] total ports to scan: ", str(int(highport)-int(lowport)+int(highport)-int(lowport)))
			else:
				pfunc("\t\t\t[!] total ports to scan: ", str(int(highport)-int(lowport)))
			pfunc("\t\t\t[!] target base port is: ",str(lowport))
			pfunc("\t\t\t[!] target end port is: ",str(end_port))
			pfunc("\t\t\t[!] target start time and date is: ",str(ldate))
		except Exception as sysarg2fail:
			print "\n"+bh +"[*] " + "-"*80 + be+"\n"
			print "\t"+bf+"ATTENTION "+be+bw+"[?] System Argument position 2 has "+bf+"FAILED"+be+bw+" due to "+be+str(sysarg2fail)
			sys.exit(0)

class ctsc():

	def __init__(self):
		pass

	def clienttcpsockconf(self, total_stack, u, ipaddr, base_port, consultant, location ):
		try:
			print bh+"\n\t[-] Diagnostics for TCP Socket Creator\n"+be
			pfunc("\t\t[!] Total ports in stack to test: ",str(total_stack)) 
			pfunc("\t\t[!] Counter incremented per test: ",str(u)) 
			pfunc("\t\t[!] IP sent to TCP socket creator: ",str(ipaddr)) 
			pfunc("\t\t[!] Base port sent to TCP socket creator: ",str(base_port)) 
			pfunc("\t\t[!] Consultants name sent to TCP socket creator: ",str(consultant)) 
			pfunc("\t\t[!] Testing location sent to TCP socket creator: ",str(location))
		except Exception as clienttcpsockfail:
			print "\n"+bh +"[*] " + "-"*80 + be+"\n" 
			print "\t"+bf+"ATTENTION "+be+bw+"[?] Client preparation for TCP Socket Creator "+bf+"FAILED"+be+bw+" due to "+be+str(clienttcpsockfail)
			sys.exit(0)

class cusc():

	def __init__(self):
		pass

	def clientudpsockconf(self, total_stack, u, ipaddr, base_port, consultant, location ):
		try:
			print bh+"\n\t[-] Diagnostics for UDP Socket Creator\n"+be
			pfunc("\t\t[!] Total ports in stack to test: ",str(total_stack)) 
			pfunc("\t\t[!] Counter incremented per test: ",str(u))
			pfunc("\t\t[!] IP sent to UDP socket creator: ",str(ipaddr)) 
			pfunc("\t\t[!] Base port sent to UDP socket creator: ",str(base_port)) 
			pfunc("\t\t[!] Consultants name sent to UDP socket creator: ",str(consultant)) 
			pfunc("\t\t[!] Testing location sent to UDP socket creator: ",str(location)) 
			print "" 
		except Exception as udpsockfail:
			print "\n"+bh +"[*] " + "-"*80 + be+"\n" 
			print "\t"+bf+"ATTENTION "+be+bw+"[?] Client preparation for UDP Socket Creator "+bf+"FAILED"+be+bw+" due to "+be+str(udpsockfail)
			sys.exit(0)

class diagserverheader():

	def serverheader(self):
		try: 
			print bh+"\t[-] Displaying Application Development Information\n"+be
			pfunc("\t\t[!] Application Codename: ",  __appname__)
			pfunc("\t\t[!] Application Functionality: ",  "Server")
			pfunc("\t\t[!] Original Author: ",  __author__)
			pfunc("\t\t[!] Year of Copyright: ", __copyright__ )
			pfunc("\t\t[!] Credits Given: ", __credits__  )
			pfunc("\t\t[!] License version: ", __license__  )
			pfunc("\t\t[!] Application Version: ", __version__  )
			pfunc("\t\t[!] Application Maintainer: ",__maintainer__)
			pfunc("\t\t[!] Development Status: ", __status__)
			print ""
		except Exception as serverheaderfail:
			print "\n"+bh +"[*] " + "-"*80 + be+"\n" 
			print "\t"+bf+"ATTENTION "+be+bw+"[?] Server Header "+bf+"FAILED"+be+bw+" due to "+be+str(serverheaderfail)
			sys.exit(0) 

class diagclientheader():

	def __init__(self):
		pass

	def clientheader(self):
		try:
			print bh+"\t[-] Displaying Application Development Information\n"+be
			pfunc("\t\t[!] Application Codename: ", __appname__)
			pfunc("\t\t[!] Application Functionality: ",  "Client")
			pfunc("\t\t[!] Original Author: ", __author__)
			pfunc("\t\t[!] Years of development: ", __copyright__ )
			pfunc("\t\t[!] Credits Given: ", __credits__  )
			pfunc("\t\t[!] License version: ", __license__  )
			pfunc("\t\t[!] Application Version: ", __version__  )
			pfunc("\t\t[!] Application Maintainer: ", __maintainer__)
			pfunc("\t\t[!] Development Status: ", __status__)
			print ""
		except Exception as clientheaderfail:
			print "\n"+bh +"[*] " + "-"*80 + be+"\n" 
			print "\t"+bf+"ATTENTION "+be+bw+"[?] Client Header "+bf+"FAILED"+be+bw+" due to "+be+str(clientheaderfail)
			sys.exit(0) 

class clientconfdiag():

	def __init__(self):
		pass

	def diagconfig(self):
		try:
			print bh+"\t[-] Displaying client configuration information\n"+be
			pfunc("\t\t[!] Client target server: ",  ipaddr)
			pfunc("\t\t[!] Client scan type: ",  scantype)
			pfunc("\t\t[!] Do we spoof the source: ",  spoofipaddr)
			pfunc("\t\t[!] Configured portrange: ",  portr)
			pfunc("\t\t[!] Client protocol to use: ",  flipbit)
			pfunc("\t\t[!] Consultant who is scanning: ",  consultant)
			pfunc("\t\t[!] Location of consultant: ",  location)
			pfunc("\t\t[!] Do we randomize the ports: ",  randomness)
			pfunc("\t\t[!] Random or Static sleep: ",  sleepy)
			pfunc("\t\t[!] How long do we sleep: ",  nappy)
			pfunc("\t\t[!] How long is the dwell: ",  rester)
			pfunc("\t\t[!] Do we suppress error: ",  suppress)
			pfunc("\t\t[!] Are we logging the scan: ",  logging)
			pfunc("\t\t[!] How are we storing it: ",  logtype)
			pfunc("\t\t[!] Are we testing covert tunnels: ",  covert)
			print ""
		except Exception as clidiagfail:
			print "\n"+bh +"[*] " + "-"*80 + be+"\n"
			print "\t"+bf+"ATTENTION "+be+bw+"[?] Client Configuration diagnostics "+bf+"FAILED"+be+bw+" due to "+be+str(clidiagfail)
			sys.exit(0)

class modimporttest():

	def __init__(self):
		pass

	def runimporttest(self):
		# import modules for functionality
		try:
			if diag == "yes":
				print bh+"\n\t[-] Module importing testing\n"+be
				import verinfo
				pfunc("\t\t[-] Version module imported ", "successfully")
				import client_kicker
				pfunc("\t\t[-] client_kicker module imported ",  "successfully")
				import scanconfig
				pfunc("\t\t[-] scanconfig module imported ",  "successfully")
				import diagfun
				pfunc("\t\t[-] diagfun module imported ",  "successfully")
				import logging
				pfunc("\t\t[-] logging module imported ", "successfully")
				import killswitch
				pfunc("\t\t[-] killer module imported ", "successfully")
				import module_error_handling
				pfunc("\t\t[-] error handler module imported ", "successfully")
				import perror
				pfunc("\t\t[-] perror module imported ",  "successfully")
				import helper
				pfunc("\t\t[-] helper module imported ",  "successfully")
				from bcolors import bcolors as b
				pfunc("\t\t[-] print color module imported ", "successfully")
				import pcolors
				pfunc("\t\t[-] print fancy module imported ", "successfully")
				import csvloggen
				pfunc("\t\t[-] csv logging module imported ",  "successfully")
				import log_enable
				pfunc("\t\t[-] logging module imported ",  "successfully")
				import txtloggen
				pfunc("\t\t[-] text logging module imported ",  "successfully")
				import xmlloggen
				pfunc("\t\t[-] xml logging module imported ",  "successfully")
				import servargs
				pfunc("\t\t[-] server args module imported ",  "successfully")
				import server_func
				pfunc("\t\t[-] server function module imported ",  "successfully")
				import threadedtcpserver
				pfunc("\t\t[-] threaded tcp server module imported ",  "successfully")
				print ""
		except Exception, importsfail:
			if diag == "yes":
				print bf+"\n\t[?] Application failure in the "+str(mp().mod_inspect())+" module" \
						 "\n\t\t[-] Resolution to error: ensure all imported modules are on the system" \
						 "\n\t\t[-] Exception reported: "+str(importsfail)+"\n"+be
			if suppress != True:
				print bf+"\n\t[?] Error generated in ./diagforall.py module" \
						 "\n\t\t[-] File location: "+str(mp().mod_inspect()) + \
						 "\n\t\t[-] Exception reported: "+str(importsfail)+"\n"+be
			pass

class ctest():

	def __init__(self):
		pass

	def colortest(self):
		try:
			from bcolors import bcolors as b
			bh = b.HEADER
			bf = b.FAIL
			be = b.ENDC
			bw = b.WARNING
			bo = b.OKBLUE
			bg = b.OKGREEN
			print bh+"\t[!] Colorization Diagnostics and testing\n"+be
			print bh+"\t\t[-] This is the HEADER color test"+be
			print bf+"\t\t[-] This is the FAIL color test"+be
			print bw+"\t\t[-] This is the WARNING color test"+be
			print bo+"\t\t[-] This is the OKBLUE color test"+be
			print bg+"\t\t[-] This is the OKGREEN color test"+be+"\n"
		except Exception, colordiag:
			print colordiag

class socktesting():

	def __init__(self):
		pass

	def sockdiag(self):
		pfunc("\t\t[!] print target scan type: ", str(scantype))
		if hostip != ipaddr:
			pfunc("\t\t[!] print target host DNS name: ", str(ipaddr))
		else:
			pfunc("\t\t[!] print target host ip: ", str(hostip))

		try:
			if respshow:
				pfunc("\t\t[!] print port condition - Open: ", str(ls))
			else:
				pfunc("\t\t[!] print port condition - Closed: ", str(ls))
		except:
			pass
		pfunc("\t\t[!] print total port count: ", str(len(stack)))
		pfunc("\t\t[!] print current port count: ", str(u))

		if scantype.lower() in ("c", "connect"):
			pass
		else:
			pfunc("\t\t[-] print raw sent packet: ",str(spacket).strip())
			base16spack = binascii.hexlify(str(spacket))
			pfunc("\t\t[-] print hexdump of sent packet: ",base16spack)
		if scantype.lower() in ("c", "connect"):
			pass
		else:
			try:
				pfunc("\t\t[-] print raw received packet: ", str(respshow).strip())
				if str(respshow) != "None":
					base16rpack = binascii.hexlify(str(respshow))
					pfunc("\t\t[-] print hexdump of received packet: ",base16rpack)
					pfunc("\t\t[-] print packet arrival times: ", str(packettime))
			except:
				pass
		pfuncok("\n\t\t[!] print passlist "+be+str(len(passlist))+":",str(passlist[-6:-1:]))
		pfuncbad("\n\t\t[!] print faillist "+be+str(len(faillist))+":",str(faillist[-6:-1:]))
		print("")