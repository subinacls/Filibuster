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

class bothsocks():

	def __init__(self):
		pass

	def connectsocket(self):
		try:
			ldate = datetime.datetime.now()
			__builtin__.proto = str("tcp").upper()
			__builtin__.ident = bo + "On " + be + str(proto) + bo + " Port: " + be + str(ls) + bo + \
			                    " - By: " + be + str(consultant) + bo + " - From: " + be + \
			                    str(location) + bo + " - On: " + be + str(ldate)
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
				passlist.append("TCP/" + str(ls))
				#print "Client data encoder before" # diagnostics
				clientencoder().datadecode(data)
			#print "Client data encoder after" # diagnostics
			else:
				pass
			__builtin__.state = "Established"
			print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + str(data)
			try:
				from log_enable import log_enabled

				log_enabled().logging()
			except Exception as logfailed:
				print "log failed in tcpsock " + str(logfailed)
		except Exception as tcpconfail:
			__builtin__.state = str(tcpconfail).split("] ")[1]
			faillist.append(str(proto).upper() + "/" + str(ls))
			print bf + "\t\t[?] Connection attempt failed on port: TCP " + str(ls) + " - to IP Address: " + str(
				ipaddr) + " - " + str(tcpconfail) + be
			try:
				from log_enable import log_enabled

				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in tcpsock " + str(logfailed)
				pass
			pass
		try:
			ldate = datetime.datetime.now()
			__builtin__.state = ""
			__builtin__.proto = str("udp").upper()
			#print "current protocol set to: ", proto  # diagnostics
			__builtin__.ident = bo + "On " + be + str(proto) + bo + " Port: " + be + \
			                    str(ls) + bo + " - By: " + be + str(consultant) + bo + " - From: " + be + \
			                    str(location) + bo + " - On: " + be + str(ldate)
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
			#print "socket attempted to send ident string"  # diagnostics
			__builtin__.data = sockobj.recv(2048)
			#print "socket attempting to get data returned"  # diagnostics
			sockobj.close()
			#print "closed socket"  # diagnostics
			if data:
				#print "data string is as follows: ", str(data)  # diagnostics
				passlist.append(str(proto).upper() + "/" + str(ls))
				clientencoder().datadecode(data)
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