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

from socket import *
import datetime
import __builtin__
from encoder import clientencoder


class tcpsocks():

	def __init__(self):
		pass

	def connectsocket(self):
		try:
			ldate = datetime.datetime.now()
			__builtin__.proto = str("tcp").upper()
			__builtin__.ident = bo+"On "+be+str(proto)+bo+" Port: "+be+str(ls)+bo+" - By: "+be+str(consultant)+bo+" - From: "+be+str(location)+bo+" - On: "+be +str(ldate)
			clientencoder().dataencode(ident)
			sockobj = socket(AF_INET, SOCK_STREAM)
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				pass
			sockobj.connect((ipaddr, ls))
			sockobj.send(ident)
			__builtin__.data = sockobj.recv(1024)
			sockobj.close()
			if data:
				passlist.append("TCP/"+str(ls))
				#print "Client data encoder before" # diagnostics
				clientencoder().datadecode(data)
				#print "Client data encoder after" # diagnostics
			else:
				pass
			__builtin__.state = "Established"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to: "+be+str(ipaddr) + str(data)
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log failed in tcpsock " + str(logfailed)
		except Exception as tcpconfail:
			__builtin__.state = str(tcpconfail).split("] ")[1]
			faillist.append(str(proto).upper()+"/"+str(ls))
			print bf+"\t\t[?] Connection attempt failed on port: TCP " + str(ls) + " - to IP Address: " + str(ipaddr) + " - " + str(tcpconfail)+be
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in tcpsock " + str(logfailed)
				pass
			pass
