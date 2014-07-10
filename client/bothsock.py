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
from padme import padgen
bh = b.HEADER
bf = b.FAIL
be = b.ENDC
bw = b.WARNING
bo = b.OKBLUE
from encoder import clientencoder


class bothsocks(object):

	def __init__(self):
		pass

	def connecttcpsocket(self):
		try:
			ldate = datetime.datetime.now()
			__builtin__.proto = str("tcp").upper()
			try:
				if str(paddata).lower() in ["true","yes"]:
					ident1 = bo + str(padgen().maxipad()) + be + "On " + str(proto) + bo + \
				                    str(padgen().maxipad()) + be + " - Port: " + str(lst) + bo + \
				                    str(padgen().maxipad()) + be + " - By: " + str(consultant) + bo + \
				                    str(padgen().maxipad()) + be + " - From: "  + str(location) + bo + \
				                    str(padgen().maxipad()) + be + " - Date: "  + str(ldate) + be + str(padgen().maxipad())
				else:
					ident1 = bo + "On " + be + str(proto) + bo + \
				                    " Port: " + be + str(lst) + bo + \
				                    " - By: " + be + str(consultant) + bo + \
				                    " - From: " + be + str(location) + bo + \
				                    " - Date: " + be + str(ldate) + be
			except Exception as e:
				print e
			clientencoder().dataencode(ident1)
			sockobj = socket.socket()
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				pass
			sockobj.connect((ipaddr, lst))
			sockobj.send(ident)
			data1 = sockobj.recv(65535)
			sockobj.close()
			if data1:
				passlist.append("TCP/" + str(lst))
				#print "Client data encoder before" # diagnostics
				clientencoder().datadecode(data1)
				#print "Client data encoder after" # diagnostics
			else:
				pass
			__builtin__.state = "Established"
			if str(paddata).lower() in ["true","yes"]:
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + bo + ": Padded data"
				passlist.append("TCP/" + str(lst))
			else:
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + " " + str(data)
				passlist.append("TCP/" + str(lst))
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log failed in tcpsock " + str(logfailed)
		except Exception as tcpconfail:
			__builtin__.state = str(tcpconfail).split("] ")[1]
			faillist.append(str(proto).upper() + "/" + str(lst))
			print bf + "\t\t[?] Connection attempt failed on port: TCP " + str(lst) + " - to IP Address: " + \
			      str(ipaddr) + " - " + str(tcpconfail) + be
			try:
				from log_enable import log_enabled

				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in tcpsock " + str(logfailed)
				pass
			pass

	def connectudpsocket(self):
		try:
			ldate = datetime.datetime.now()
			state = ""
			proto = str("udp").upper()
			try:
				if str(paddata).lower() in ["true","yes"]:
					ident2 = bo + str(padgen().maxipad()) + be + "On " + str(proto) + bo + \
				                    str(padgen().maxipad()) + be + " - Port: " + str(lsu) + bo + \
				                    str(padgen().maxipad()) + be + " - By: " + str(consultant) + bo + \
				                    str(padgen().maxipad()) + be + " - From: "  + str(location) + bo + \
				                    str(padgen().maxipad()) + be + " - Date: "  + str(ldate) + be + str(padgen().maxipad())
				else:
					ident2 = bo + "On " + be + str(proto) + bo + \
				                    " Port: " + be + str(lsu) + bo + \
				                    " - By: " + be + str(consultant) + bo + \
				                    " - From: " + be + str(location) + bo + \
				                    " - Date: " + be + str(ldate) + be
			except Exception as paddingfailed:
				print paddingfailed

			#print "string being sent: ", ident  # diagnostics
			clientencoder().dataencode(ident2)
			#print "encoded string being sent: ", ident  # diagnostics
			sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			if nappy > "1":
				#print "nap time is a float: ", nappy  # diagnostics
				sockobj.settimeout(float(nappy))
			else:
				#print "nap time is an integer:", nappy  # diagnostics
				sockobj.settimeout(float(0.1))
			sockobj.connect((ipaddr, lsu))
			#print "socket connection attempted"  # diagnostics
			sockobj.send(ident)
			#print "socket sent ident string"  # diagnostics
			data2 = sockobj.recv(65535)
			#print "socket attempting to get data returned"  # diagnostics
			sockobj.close()
			#print "closed socket"  # diagnostics
			if data2:
				#print "data string is as follows: ", str(data)  # diagnostics
				passlist.append(str(proto).upper() + "/" + str(lsu))
				clientencoder().datadecode(data2)
				__builtin__.state = "Established"
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + str(data)
			else:
				pass
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logenbfail:
				print "Failed in udpsock logging: " + str(logenbfail)
		except Exception as udpconfail:
			__builtin__.state = str(udpconfail).split("] ")[1]
			faillist.append(str(proto).upper() + "/" + str(lsu))
			print bf + "\t\t[?] Connection attempt failed on UDP port: " + str(lsu) + " - to IP Address: " + \
			      str(ipaddr) + " - " + str(udpconfail) + be
			try:
				from log_enable import log_enabled

				log_enabled().logging()
			except Exception as e:
				print "Failed in udpsock logging: " + str(e)
				pass
			pass
