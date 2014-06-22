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
import os
import __builtin__
import socket
from bcolors import bcolors as b
bh = b.HEADER
bf = b.FAIL
be = b.ENDC
bw = b.WARNING
bo = b.OKBLUE

import __builtin__

class udpsocks():

	def __init__(self):
		pass

	def connectsocket(self):
		try:

			__builtin__.state = ""
			__builtin__.proto = str("udp").upper()
			ident = bo+"On "+ be +str(proto) + bo+" Port: "+ be +str(ls) + bo+" - By: "+ be +  str(consultant) +bo+ " - From: " +be + str(location) + bo+ " - On: " +  be +str(ldate)
			sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				sockobj.settimeout(float(0.1))
			sockobj.connect((ipaddr, base_port))
			sockobj.send(ident)
			data = sockobj.recv(1024)
			sockobj.close()
			if data != "":
				passlist.append(str(proto).upper()+"/"+str(ls))
			__builtin__.state = "connected"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to: "+be+str(ipaddr) +bo+" - "+ be + str(data)
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logenbfail:
				print "Failed in udpsock logging: " + str(logenbfail)

		except Exception as logenbfail:
			print bf+"\t\t[?] Connection attempt failed on UDP port: " + str(ls) + " - to IP Address: " + str(ipaddr) + " - " + str(logenbfail)+be
			bi.state = "Failed"
			try:
				from log_enable import log_enabled
				log_enabled().logging()

			except Exception as e:
				print "Failed in udpsock logging: " + str(e)
				pass
			faillist.append(str(proto).upper()+"/"+str(ls))
			pass


