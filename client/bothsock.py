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
			__builtin__.state = ""
			__builtin__.proto = str("tcp").upper()
			ident = bo+"On "+be+str(proto)+bo+" Port: "+be+str(ls)+bo+" - By: "+be+str(consultant)+bo+" - From: "+be+str(location)+bo+" - On: "+be +str(ldate)
			sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
			__builtin__.state = "Established"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to: "+be+str(ipaddr) +bo+" - " +be+str(data).strip()
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
			pass
		try:
			__builtin__.state = ""
			__builtin__.proto = str("udp").upper()
			ident = bo+"On "+ be +str(proto) + bo+" Port: "+ be +str(ls) + bo+" - By: "+ be +  str(consultant) +bo+ " - From: " +be + str(location) + bo+ " - On: " +  be +str(ldate)
			sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				sockobj.settimeout(float(0.1))
			sockobj.connect((ipaddr, ls))
			sockobj.send(ident)
			data = sockobj.recv(1024)
			sockobj.close()
			if data != "":
				passlist.append(str(proto).upper()+"/"+str(ls))
				__builtin__.state = "Established"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to: "+be+str(ipaddr) +bo+" - "+ be + str(data)
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logenbfail:
				print "Failed in udpsock logging: " + str(logenbfail)

		except Exception as logenbfail:
			print bf+"\t\t[?] Connection attempt failed on UDP port: " + str(ls) + " - to IP Address: " + str(ipaddr) + " - " + str(logenbfail)+be
			__builtin__.state = str(logenbfail).split("] ")[1]
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in bothsock " + str(logfailed)
			faillist.append("UDP/"+str(ls))
			pass
