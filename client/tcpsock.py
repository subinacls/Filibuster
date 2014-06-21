#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

""" Useful information
gets logging type used if any
configures and starts socket for communication
	logs state and information about connection attempt
"""

import datetime
from socket import *
import __builtin__ as bi

class tcpsocks():

	def __init__(self):
		pass

	def connectsocket(self):
		try:

			bi.proto = str("tcp").upper()
			ident = bo+"On "+be+str(proto)+bo+" Port: "+be+str(ls)+bo+" - By: "+be+str(consultant)+bo+" - From: "+be+str(location)+bo+" - On: "+be +str(ldate)
			sockobj = socket(AF_INET, SOCK_STREAM)
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				pass
			sockobj.connect((ipaddr, ls))
			sockobj.send(ident)
			data = sockobj.recv(1024)
			if data != "":
				passlist.append("TCP/"+str(ls))
			else:
				pass
			sockobj.close()
			print "testa"
			state = "connected"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to IP Address: "+be+str(ipaddr) +bo+" - " +be+str(data).strip()
			print "testb"

			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log failed in tcpsock " + str(logfailed)

		except Exception as tcpconfail:
			__builtin__.state = str(tcpconfail).split("] ")[1]
			print bf+"\t\t[?] Connection attempt failed on port: TCP " + str(ls) + " - to IP Address: " + str(ipaddr) + " - " + str(tcpconfail)+be
			__builtin__.proto = "TCP"
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in tcpsock " + str(logfailed)
			faillist.append("TCP/"+str(base_port))