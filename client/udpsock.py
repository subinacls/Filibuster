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
import base64 as b64
import socket
from bcolors import bcolors as b
bh = b.HEADER
bf = b.FAIL
be = b.ENDC
bw = b.WARNING
bo = b.OKBLUE



class udpsocks():


	def __init__(self):
		pass

	def connectsocket(self):
		try:
			__builtin__.state = ""
			__builtin__.proto = str("udp").upper()
			ident = bo+"On "+be+str(proto)+bo+" Port: "+be+str(ls)+bo+" - By: "+be+str(consultant)+bo+" - From: "+be+str(location)+bo+" - On: "+be +str(ldate)
			if encodedata == "base85":
				ident = b64.b85encode(ident)
			if encodedata == "base64":
				ident = b64.b64encode(ident)
			if encodedata == "base32":
				ident = b64.b32encode(ident)
			if encodedata == "base16":
				ident = b64.b16encode(ident)
			if encodedata == "base85":
				ident = b64.b85encode(ident)
			if encodedata == "rot13":
				ident = str(ident).encode('rot13')
			if encodedata == "xor":
				#xor routing taken from https://dustri.org/
				# Stupid XOR demo
				from itertools import cycle, izip
				key = 's3cr3t'
				ident = ''.join(chr(ord(c)^ord(k)) for c,k in izip(ident, cycle(key)))
			if encodedata == "url":
				pass # do url
			if encodedata == "lzma":
				pass # do lzma
			if encodedata in ["gz", "gzip"]:
				pass # do gzip
			if encodedata in ["binary", "bytestring"]:
				pass # do gzip
			if encodedata in ["plain", "plaintext", "cleartext", "clear"]:
				pass # do gzip
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
				if encodedata == "base85":
					data = b64.b85decode(data)
				if encodedata == "base64":
					data = b64.b64decode(data)
				if encodedata == "base16":
					data = b64.b16decode(data)
				if encodedata == "base32":
					data = b64.b32decode(data)
				if encodedata == "rot13":
					data = str(data).decode('rot13')
				if encodedata == "xor":
					data = ''.join(chr(ord(c)^ord(k)) for c,k in izip(data, cycle(key)))
				__builtin__.state = "connected"
				print bf+"\t\tATTENTION " +be+bo+"[*] Connected to: "+be+str(ipaddr) +bo+" - "+ be + str(data)
			else:
				pass
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logenbfail:
				print "Failed in udpsock logging: " + str(logenbfail)
		except Exception as logenbfail:
			print bf+"\t\t[?] Connection attempt failed on UDP port: " + str(ls) + " - to IP Address: " + str(ipaddr) + " - " + str(logenbfail)+be
			state = "Failed"
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as e:
				print "Failed in udpsock logging: " + str(e)
				pass
			faillist.append(str(proto).upper()+"/"+str(ls))
			print ls
			pass


