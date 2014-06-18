# encoding: utf-8
#!/usr/bin/env python
import verinfo
from bcolors import bcolors
import os
import sys
import time

va = __appname__
vv = __version__
vauth = __author__

bh = bcolors.HEADER
bf = bcolors.FAIL
be = bcolors.ENDC
bw = bcolors.WARNING
bo = bcolors.OKBLUE

class tcp_servers():

	def __init__(self):
		pass

	def tserver(self,serverport):
		try:
			from threadedtcpserver import ThreadedTCPRequestHandler 
			from threadedtcpserver import ThreadedTCPServer
			from threadedtcpserver import tcpserver
			tcpserver().mytcpserver(int(serverport))
			while 1: 
				try:
					time.sleep(0) 
				except KeyboardInterrupt: 
					pid = os.getpid()
					os.popen("iptables -t nat -F")
					print bo+"\t[!] User exited - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + be
					killer = "kill -9 "+str(pid)
					os.popen(killer) 
					sys.exit(0) 
		except Exception as e: 
			print "\t[?] " +va+" v."+vv+" - CRASHED during import of tcp server: " + bf + str(e) + "\n" +be 
			sys.exit(0)

class udp_servers:

	def __init__(self):
		pass

	def userver(self, serverport):
		try:
			from threadedudpserver import ThreadedUDPRequestHandler
			from threadedudpserver import ThreadedUDPServer
			from threadedudpserver import udpserver
			udpserver(int(serverport)).myudpserver(int(serverport))
			while 1: 
				try: 
					time.sleep(0)
				except KeyboardInterrupt:
					pid = os.getpid()
					os.popen("iptables -t nat -F") 
					print bo+"\t[!] User exited - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + be
					killer = "kill -9 "+str(pid)
					os.popen(killer)
					sys.exit(0) 
		except Exception as e: 
			print "\t[?] " +va+" v."+vv+" - CRASHED during import of udp servers: " + bf + str(e) + "\n" +be 
			sys.exit(0)

class both_servers:

	def __init__(self):
		pass

	def bserver(self, serverport):
		try:
			from threadedbothserver import ThreadedTCPRequestHandler
			from threadedbothserver import ThreadedTCPServer
			from threadedbothserver import btcpserver
			from threadedbothserver import ThreadedUDPRequestHandler
			from threadedbothserver import ThreadedUDPServer
			from threadedbothserver import budpserver
			budpserver(int(serverport)).myudpserver(int(serverport)) 
			btcpserver(int(serverport)).mytcpserver(int(serverport))
			while 1:
				try:
					time.sleep(0)
				except KeyboardInterrupt:
					pid = os.getpid()
					os.popen("iptables -t nat -F")
					print bo+"\t[!] User initialized exit - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + be
					killer = "kill -9 "+str(pid)
					os.popen(killer)
					sys.exit(0) 
		except Exception as e:
			print "\t[?] " +va+" v."+vv+" - CRASHED during import of both servers: " + bf + str(e) + "\n" +be 
			sys.exit(0)