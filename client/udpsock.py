# encoding: utf-8
#!/usr/bin/env python
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
import __builtin__

class udpsocks():

	def __init__(self):
		pass

	def connectsocket(self):
		try:
			dft = str(datetime.datetime.now()).split(".")[0]
			ident = bo+"On UDP Port: "+be+str(base_port)+bo+" - By: "+be+str(consultant)+bo+" - From: "+be+str(location)+bo+" - On: "+be +str(dft)
			sockobj = socket(AF_INET, SOCK_STREAM)
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				pass
			sockobj.connect((ipaddr, base_port))
			sockobj.send(ident)
			data = sockobj.recv(1024)
			if data:
				passlist.append("TCP/"+str(base_port))
			sockobj.close()
			__builtin__.state = "connected"
			__builtin__.proto = "TCP"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to IP Address: "+be+str(ipaddr) +bo+" - " +be+str(data).strip()
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log failed in tcpsock " + str(logfailed)

		except Exception as confailtcp:
			__builtin__.state = "failed"
			print bf+"\t\t[?] Connection attempt failed on port: TCP " + str(base_port) + " - to IP Address: " + str(ipaddr) + " - " + str(confailtcp)+be
			__builtin__.proto = "TCP"
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in tcpsock " + str(logfailed)
			faillist.append("TCP/"+str(base_port))
