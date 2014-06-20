# encoding: utf-8
#!/usr/bin/env python
#
# module author: subinacls
#

""" Useful information
initializes client scanner for further configuration
	checks if port range is a file or string
	builds port list used to scan from
	gets current date
	checks for randomness of port scanning
	check protocol being scanned (tcp / udp / both)
	check for scan type(currently: connect)
	checks for TLS wrapped communication
	calls socket creation function
		displays any diagnostics information as processes happen
"""

import random
import time
import os
import numpy as np
import __builtin__
from diagforall import diagclientheader
from diagforall import csconf
from pcolors import printfunction
from helper import helper

class initscanner():

	def __init__(self):
		pass
	def scanengine(self):
		if scantype:
			print(bh+"\t[-] Starting "+be+str(scantype)+be+bh+" scanning process now, aganst: "+be+ipaddr+"\n"+be)
		if 1 == 1 :
			""" start stack build timer """
			__builtin__.stack_timer = time.time()
			__builtin__.stack = [] # stored port numbers here when generated from user specifications"
			__builtin__.passlist = []
			__builtin__.faillist = []
			# get the date information from local system
			""" maybe future addition, if NTP test passes use NTP server in EDU for data information """
			d = os.popen("date")
			dft = d.readline()
			__builtin__.ldate = str(dft.strip('\n')[4:7])+"-"+str(dft.strip('\n')[8:10])+"-"+str(dft.strip('\n')[24:29])
			__builtin__.u = 0

			""" check if the portrange configuration variable is a file or a range """
			if os.path.isfile(portr):
				with open(portr) as prange:
					for sport in prange:
						nstrip = sport.strip()
						stack.append(nstrip)
						try:
							stack.remove('\n')
						except Exception as stackrfail: # add in diagnostics handling for this error if one is caught
							print "stack remove failed: " + str(stackrfail)
							pass
						try:
							stack.remove('')
						except Exception as stackrfail: # add in diagnostics handling for this error if one is caught
							print "stack remove failed: " + str(stackrfail)
							pass
			else:
				if not os.path.isfile(portr):
					portrange = portr
					__builtin__.portranges = str(portrange).split("-")
					__builtin__.lowport = int(portranges[0])
					__builtin__.highport = int(portranges[1])
					__builtin__.base_port = int(lowport)
					__builtin__.end_port = int(highport)
					if diag == "yes":
						try:
							from diagforall import portrng
							portrng().prange(lowport, highport, end_port)
						except Exception as prangefail:
							print("\t"+bf+"ATTENTION "+be+bw+"[?] Client preperation for portrange "+bf+"FAILED"+be +" to:" + str(prangefail))
					__builtin__.s = int(lowport)
					__builtin__.t = int(highport)

					# iterate over port start and finish range
			for x in range(s,t):
				stack.append(x)
			stack.append(highport)
			if diag:
				print("")
			if str(randomness).lower() in ["1","t","true","y","yes","on"]:
				#ls = random.choice(stack)
				random.shuffle(stack)
			else:
				pass
			__builtin__.total_stack = len(stack)
			while int(u) != total_stack:
				#__builtin__.run_timer = time.time()
				if stack[0]:
					__builtin__.ls = stack[0]
					if sleepy == "random":
						__builtin__.rest = int(random.choice(np.arange(1,int(nappy),int(rester))))
					else:
						__builtin__.rest = rester
					__builtin__.u = int(u) + 1
					base_port = ls
					__builtin__.thread_count = int(u)
					__builtin__.cfb = str(flipbit)
					# configure connect scanner
					if  str(scantype).lower() == "connect":
						if (str(mytls)) == (str("no")):
							cfb = str(flipbit).lower()
							# initalize socket creation
							if cfb == "tcp":
								from tcpsock import tcpsocks
								from diagforall import ctsc
								if diag =="yes":
									try:
										ctsc().clienttcpsockconf(total_stack, u, ipaddr, ls, consultant, location)
									except Exception as diagclientsockconfigfail:
										print("\t"+bf+"ATTENTION "+be+bw+"[?] Client preparation for TCP sockets "+ \
										      bf+"FAILED"+be+bw+" due to "+be+str(diagclientsockconfigfail))
								try:
									if diag == "yes":
										from diagforall import socktesting
										socktesting().sockdiag()
									tcpsocks().connectsocket(ipaddr,base_port, consultant, location, ldate, passlist,faillist)
								except Exception as tcpconnectsocketfail:
									print("\t"+bf+"ATTENTION "+be+bw+"[?] Client failed to connect to TCP sockets "+ \
									      bf+"FAILED"+be+bw+" due to "+be+str(tcpconnectsocketfail))
									pass
								time.sleep(float(rest))
								stack.remove(ls)


							if cfb == "udp":
								from udpsock import *
								if diag =="yes":
									try:
										cusc().clientudpsockconf(total_stack, u, ipaddr, base_port, consultant, location)
									except Exception as cuscfail:
										print("\t"+bf+"ATTENTION "+be+bw+"[?] Client preparation for UDP sockets "+bf+"FAILED"+be+bw+" due to "+be+str(cuscfail))
								try:
									udpsocks().start_dgram(ipaddr,base_port, consultant, location, ldate, passlist,faillist)
								except Exception as udpsockfail:
									print("\t"+bf+"ATTENTION "+be+bw+"[?] Client failed to connect to UDP sockets "+bf+"FAILED"+be+bw+" due to "+be+str(udpsockfail))
									pass
								time.sleep(float(rest))
								stack.remove(ls)
								if diag == "yes":
									print("\n\t"+bh+"[-] Client UDP port passlist\n" + be)
									print(passlist)
									print("\n\t"+bh+"[-] Client UDP port faillist\n" + be)
									print(faillist)

							# initalize socket creation

							if cfb == "both":
								if diag =="yes":
									try:
										from diagforall import cusc, ctsc
										cusc(total_stack, u, ipaddr, base_port, consultant, location).clientudpsockconf(total_stack, u, ipaddr, base_port, consultant, location)
										ctsc(total_stack, u, ipaddr, base_port, consultant, location).clienttcpsockconf(total_stack, u, ipaddr, base_port, consultant, location)
									except Exception as diagsockfail:
										print("\t"+bf+"ATTENTION "+be+bw+"[?] Client preperation for TCP/UDP sockets "+bf+"FAILED"+be+bw+" due to "+be+str(diagsockfail))
								try:
									from tcpsock import *
									from udpsock import *
								except Exception as sockimportfail:
									print("\t"+bf+"ATTENTION "+be+bw+"[?] Client failed to connect to UDP/TCP sockets "+bf+"FAILED"+be+bw+" due to "+be+str(sockimportfail))
								try:
									tcpsocks().start_socket(ipaddr, base_port, location, consultant, ldate, passlist,faillist)
									udpsocks(ipaddr, base_port, consultant, location, ldate, passlist,faillist).start_dgram(ipaddr,base_port, location, consultant, ldate, passlist,faillist)
								except Exception as tcpsockfail:
									print("\t"+bf+"ATTENTION "+be+bw+"[?] Client failed to connect to TCP/UDP sockets "+bf+"FAILED"+be+bw+" due to "+be+str(tcpsockfail))
								time.sleep(float(rest))
								stack.remove(ls)
								if diag == "yes":
									print("\n\t"+bh+"[-] Client TCP/UDP port passlist\n" + be)
									print(passlist)
									print("\n\t"+bh+"[-] Client TCP/UDP port faillist\n" + be)
									print(faillist)
