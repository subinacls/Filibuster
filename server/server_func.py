#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

import os
import sys
import time
import verinfo
import __builtin__
from bcolors import bcolors

__builtin__.va = __appname__
__builtin__.vv = __version__
__builtin__.vauth = __author__

bh = bcolors.HEADER
bf = bcolors.FAIL
be = bcolors.ENDC
bw = bcolors.WARNING
bo = bcolors.OKBLUE

class tcp_servers():

	def __init__(self):
		pass

	def tserver(self):
		try:
			from threadedtcpserver import ThreadedTCPRequestHandler, ThreadedTCPServer, tcpserver
			tcpserver().mytcpserver()
			try:
				while 1:
					time.sleep(0)
			except KeyboardInterrupt:
				pid = os.getpid()
				os.popen("iptables -t nat -F")
				print bo+"\t[!] User exited - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + be
				killer = "kill -9 "+str(pid)
				os.popen(killer)
				sys.exit(0)
		except Exception as tcpserverfail:
			print "\t[?] " +va+" v."+vv+" - CRASHED during import of tcp server: " + bf + str(tcpserverfail) + "\n" +be
			sys.exit(0)

class udp_servers:

	def __init__(self):
		pass

	def userver(self):
		try:
			from threadedudpserver import ThreadedUDPRequestHandler, ThreadedUDPServer, udpserver
			udpserver().myudpserver()
			try:
				while 1:
					time.sleep(0)
			except KeyboardInterrupt:
				pid = os.getpid()
				os.popen("iptables -t nat -F")
				print bo+"\t[!] User exited - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + be
				killer = "kill -9 "+str(pid)
				os.popen(killer)
				sys.exit(0)
		except Exception as udpserverfail:
			print "\t[?] " +va+" v."+vv+" - CRASHED during import of udp servers: " + bf + str(udpserverfail) + "\n" +be
			sys.exit(0)

class both_servers:

	def __init__(self):
		pass

	def bserver(self):
		try:
			from threadedbothserver import ThreadedTCPRequestHandler, ThreadedTCPServer, bothserver
			from threadedbothserver import ThreadedUDPRequestHandler, ThreadedUDPServer
			bothserver().mybothserver()
			try:
				while 1:
					time.sleep(0)
			except KeyboardInterrupt:
				pid = os.getpid()
				os.popen("iptables -t nat -F")
				print bo+"\t[!] User initialized exit - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + be
				killer = "kill -9 "+str(pid)
				os.popen(killer)
				sys.exit(0)
		except Exception as bothserverfail:
			print "\t[?] " +va+" v."+vv+" - CRASHED during import of both servers: " + bf + str(bothserverfail) + "\n" +be
			sys.exit(0)