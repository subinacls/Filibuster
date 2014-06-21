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
import os
import socket
from bcolors import bcolors as b
bh = b.HEADER
bf = b.FAIL
be = b.ENDC
bw = b.WARNING
bo = b.OKBLUE

import __builtin__ as bi

class udpsocks():

	def __init__(self):
		pass

	def connectsocket(self):
		try:
			d = os.popen("date")
			dft = d.readline()
			global state
			bi.state = ""
			global proto
			bi.proto = str(fb).upper()
			ident = bo+"On UDP Port: "+ be +str(ls) + bo+" - By: "+ be +  str(location) +bo+ " - From: " +be + str(consultant) + bo+ " - On: " +  be +str(dft)
			sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				sockobj.settimeout(float(0.1))
			sockobj.connect((ipaddr, ls))
			sockobj.send(ident)
			data = sockobj.recv(1024)
			sockobj.close()
			if data:
				passlist.append(str(fb).upper()+"/"+str(ls))
			state = "Successful"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to: - "+be+str(ipaddr) +bo+" - "+ be + str(data)
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logenbfail:
				print "Failed in udpsock logging: " + str(logenbfail)

		except Exception as logenbfail:
			print "test2"
			print bf+"\t\t[?] Connection attempt failed on port: UDP " + str(ls) + " - to IP Address: " + str(ipaddr) + " - " + str(logenbfail)+be
			bi.state = "Failed"
			try:
				from log_enable import log_enabled
				log_enabled().logging()

			except Exception as e:
				print "Failed in udpsock logging: " + str(e)
				pass
			faillist.append(str(fb).upper()+"/"+str(ls))
			pass


