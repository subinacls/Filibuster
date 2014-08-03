#!/usr/bin/env python
# encoding: utf-8
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
import datetime
from diagforall import socktesting
from diagforall import diagclientheader
from diagforall import csconf
from diagforall import ctsc
from diagforall import cusc
#from diagforall import cbsc
from pcolors import printfunction
from helper import helper
from tcpsock import tcpsocks
from udpsock import udpsocks
from bothsock import bothsocks
from killswitch import killswitch as ks


class initscanner(object):
	def __init__(self):
		pass

	def scanengine(self):
		# start stack build timer
		__builtin__.stack_timer = time.time()
		__builtin__.stack = []
		__builtin__.passlist = []
		__builtin__.faillist = []
		""" get the date information from local system """
		""" maybe future addition, if NTP test passes use NTP server update from .EDU"""
		__builtin__.ldate = str(datetime.datetime.now()).strip(".")
		__builtin__.dft = str(ldate).split(" ")[0]
		__builtin__.u = 0
		""" check if the portrange configuration variable is a file or a range """
		if os.path.isfile(portr):
			with open(portr) as prange:
				for sport in prange:
					nstrip = sport.strip()
					stack.append(nstrip)
					try:
						stack.remove('\n')
					except Exception as stackrfail:
						print "stack remove failed: " + str(stackrfail)
						pass
					try:
						stack.remove('')
					except Exception as stackrfail:
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
				if str(diag).lower() in ["true", "yes"]:
					try:
						from diagforall import portrng

						portrng().prange()
					except Exception as prangefail:
						print "\t" + bf + "ATTENTION " + be + bw + "[?] Client preperation for portrange " + \
						      bf + "FAILED" + be + " to:" + str(prangefail)
				__builtin__.s = int(lowport)
				__builtin__.t = int(highport)

		for x in range(s, t):  # iterate over port start and finish range
			stack.append(x)
		stack.append(highport)

		if str(flipbit).lower() == "both":  # check is flipbit is set and what the function is
			__builtin__.stack2 = list(stack)
			if str(randomness).lower() in ["true", "yes"]:  # if random do a shuffle on stack2
				random.shuffle(stack2)
			__builtin__.total_stack = len(stack)+len(stack2)  # get the total lenght of the ports to scan

		if str(randomness).lower() in ["true", "yes"]:  # if random do a shuffle on the stack
			random.shuffle(stack)

		__builtin__.total_stack = len(stack)  # get the total lenght of the ports to scan

		print bh + "\n\t[-] Starting " + be + str(scantype) + be + bh + \
		      " scanning process against server IP: " + be + ipaddr + be

		while int(u) != total_stack:  # while loop till counter = stack total
			ks().skillswitch()  # load killswitch to monitor for user interrupt
			__builtin__.state = ""  # blank out any previous set state
			__builtin__.run_timer = time.time()  # get start timer information
			if stack[0]:  # if there is anything in position 0 in the list, grab and move on
				if str(flipbit).lower() == "both":
					__builtin__.lst = stack[0]  # same function but for both TCP and UDP
					__builtin__.lsu = stack2[0]
				else:
					__builtin__.ls = stack[0]  # otherwise - use this for a single protocol
				if sleepy == "random":  # sets the sleep timer between scan attempts
					__builtin__.rest = int(random.choice(np.arange(int(nappy), int(rester))))
				else:
					__builtin__.rest = rester  # else set for static timing
				__builtin__.u = int(u) + 1  # add 1 to counter
				__builtin__.thread_count = int(u)  # set thread counter
				__builtin__.cfb = str(flipbit)  # rename flipbit for use elsewhere in the app

				# configure connect scanner

				if str(scantype).lower() == "connect":
					if (str(mytls)) == (str("no")):
						cfb = str(flipbit).lower()
						# initalize socket creation
						if cfb == "tcp":
							try:
								ctsc().clienttcpsockconf()
								socktesting().sockdiag()
								tcpsocks().connectsocket()
							except Exception as tcpconnectsocketfail:
								print "\t" + bf + "ATTENTION " + be + bw + \
								      "[?] Client failed to connect to TCP sockets " + bf + "FAILED" + be + bw + \
								      " due to " + be + str(tcpconnectsocketfail)
								pass
							time.sleep(float(rest))
							stack.remove(ls)

						# initalize socket creation

						if cfb == "udp":
							try:
								cusc().clientudpsockconf()
								socktesting().sockdiag()
								udpsocks().connectsocket()
							except Exception as udpsockfail:
								print "\t" + bf + "ATTENTION " + be + bw + \
								      "[?] Client failed to connect to UDP sockets " + bf + "FAILED" + be + bw + \
								      " due to " + be + str(udpsockfail)
								pass
							time.sleep(float(rest))
							stack.remove(ls)

						# initalize socket creation

						if cfb == "both":
							try:
								#cbsc().clientbothsockconf()
								bothsocks().connecttcpsocket()
								bothsocks().connectudpsocket()

							except Exception as tcpsockfail:
								print "\t" + bf + "ATTENTION " + be + bw + "[?] Client failed to connect to TCP/UDP sockets " + \
								      bf + "FAILED" + be + bw + " due to " + be + str(tcpsockfail)
							time.sleep(float(rest))
							try:  # had issues with stack counter failing so I just pass on exceptions
								stack.remove(lst)
								stack2.remove(lsu)
							except Exception as nomorestack:
								pass