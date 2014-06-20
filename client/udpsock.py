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
			ident = bo+"On UDP Port: "+be+str(ls)+bo+" - By: "+be+str(consultant)+bo+" - From: "+be+str(location)+bo+" - On: "+be +str(dft)
			sockobj = socket(AF_INET, SOCK_DGRAM)
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				pass
			sockobj.connect((ipaddr, ls))
			sockobj.send(ident)
			data = sockobj.recv(1024)
			if data:
				passlist.append(str(fb).upper()+"/"+str(ls))
			sockobj.close()
			__builtin__.state = "connected"
			__builtin__.proto = "udp"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to IP Address: "+be+str(ipaddr) +bo+" - " +be+str(data).strip()
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log failed in udpsock " + str(logfailed)

		except Exception as confailudp:
			__builtin__.state = "failed"
			print bf+"\t\t[?] Connection attempt failed on port: UDP " + str(ls) + " - to IP Address: " + str(ipaddr) + " - " + str(confailudp)+be
			__builtin__.proto = "TCP"
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in udpsock " + str(logfailed)
			faillist.append(str(fb).upper()+"/"+str(ls))
