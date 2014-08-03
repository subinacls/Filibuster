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

import socket
import datetime
import __builtin__
from encoder import clientencoder
from padme import padgen


class tcpsocks(object):

	def __init__(self):
		pass

	def connectsocket(self):
		try:
			ldate = datetime.datetime.now()
			__builtin__.proto = str("tcp").upper()
			try:
				#if str(paddata).lower() in ["true","yes"]:
				#	__builtin__.ident = bo + str(padgen().maxipad()) + be + "On " + str(proto) + bo + \
				#                    str(padgen().maxipad()) + be + " - Port: " + str(ls) + "\t" + bo + \
				#                    str(padgen().maxipad()) + be + " - By: " + str(consultant) + bo + \
				#                    str(padgen().maxipad()) + be + " - From: "  + str(location) + bo + \
				#                    str(padgen().maxipad()) + be + " - Date: "  + str(ldate) + bo + \
				#	                str(padgen().maxipad()) + be
				#else:
				#	__builtin__.ident = bo + "On " + be + str(proto) + bo + \
				#                    " Port: " + be + str(ls) + "\t" + bo + \
				#                    " - By: " + be + str(consultant) + bo + \
				#                    " - From: " + be + str(location) + bo + \
				#                    " - Date: " + be + str(ldate) + be
				ident = "GET /this/should/never/be/real_anywhere/Filterbuster.html"
			except Exception as e:
				print e
			clientencoder().dataencode(ident)
			sockobj = socket.socket()
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				pass
			sockobj.connect((ipaddr, ls))
			sockobj.send(ident)
			__builtin__.data = sockobj.recv(65535)
			sockobj.close()
			if data:
				passlist.append(str(proto).upper() + "/" + str(ls))
				#print "Client data encoder before" # diagnostics
				clientencoder().datadecode(data)
				#print "Client data encoder after" # diagnostics
			else:
				pass
			__builtin__.state = "Established"
			if str(paddata).lower() in ["true","yes"]:
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + bo + ": Padded data"
				passlist.append("TCP/" + str(ls))
			else:
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + str(data)
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log failed in tcpsock " + str(logfailed)
		except Exception as tcpconfail:
			__builtin__.state = str(tcpconfail).split("] ")[1]
			faillist.append(str(proto).upper() + "/" + str(ls))
			print bf + "\t\t[?] Connection attempt failed on port: TCP " + str(ls) + " - to IP Address: " + \
			      str(ipaddr) + " - " + str(tcpconfail) + be
			try:
				from log_enable import log_enabled

				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in tcpsock " + str(logfailed)
				pass
			pass

