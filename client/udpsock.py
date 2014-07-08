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

import __builtin__
import socket
import datetime
from bcolors import bcolors as b

bh = b.HEADER
bf = b.FAIL
be = b.ENDC
bw = b.WARNING
bo = b.OKBLUE
from encoder import clientencoder


class udpsocks(object):

	def __init__(self):
		pass

	def connectsocket(self):
		try:
			ldate = datetime.datetime.now()
			state = ""
			proto = str("udp").upper()
			#print "current protocol set to: ", proto  # diagnostics
			ident = bo + "On " + be + str(proto) + bo + " Port: " + be + \
			                    str(ls) + bo + " - By: " + be + str(consultant) + bo + " - From: " + be + \
			                    str(location) + bo + " - Date: " + be + str(ldate)
			#print "string being sent: ", ident  # diagnostics
			clientencoder().dataencode(ident)
			#print "encoded string being sent: ", ident  # diagnostics
			sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			if nappy > "1":
				#print "nap time is a float: ", nappy  # diagnostics
				sockobj.settimeout(float(nappy))
			else:
				#print "nap time is an integer:", nappy  # diagnostics
				sockobj.settimeout(float(0.1))
			sockobj.connect((ipaddr, ls))
			#print "socket connection attempted"  # diagnostics
			sockobj.send(ident)
			#print "socket sent ident string"  # diagnostics
			data = sockobj.recvfrom(65535)
			#print "socket attempting to get data returned"  # diagnostics
			sockobj.close()
			#print "closed socket"  # diagnostics
			if data:
				#print "data string is as follows: ", str(data)  # diagnostics
				passlist.append(str(proto).upper() + "/" + str(ls))
				clientencoder().datadecode(data)
				__builtin__.state = "Established"
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + str(data[0])
			else:
				pass
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logenbfail:
				print "Failed in udpsock logging: " + str(logenbfail)
		except Exception as udpconfail:
			__builtin__.state = str(udpconfail).split("] ")[1]
			faillist.append(str(proto).upper() + "/" + str(ls))
			print bf + "\t\t[?] Connection attempt failed on UDP port: " + str(ls) + " - to IP Address: " + \
			      str(ipaddr) + " - " + str(udpconfail) + be
			try:
				from log_enable import log_enabled

				log_enabled().logging()
			except Exception as e:
				print "Failed in udpsock logging: " + str(e)
				pass
			pass
