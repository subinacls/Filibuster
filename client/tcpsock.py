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

import sys
from socket import *
import __builtin__
import datetime
import base64 as b64

class tcpsocks():

	def __init__(self):
		pass

	def connectsocket(self):
		try:
			sdate = str(datetime.datetime.now()).strip(".")
			__builtin__.proto = str("tcp").upper()
			ident = bo+"On "+be+str(proto)+bo+" Port: "+be+str(ls)+bo+" - By: "+be+str(consultant)+bo+" - From: "+be+str(location)+bo+" - On: "+be +str(sdate)
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
			sockobj = socket(AF_INET, SOCK_STREAM)
			if nappy > "1":
				sockobj.settimeout(float(nappy))
			else:
				pass
			sockobj.connect((ipaddr, ls))
			sockobj.send(ident)
			data = sockobj.recv(1024)
			sockobj.close()
			if str(data):
				passlist.append("TCP/"+str(ls))
			else:
				pass
			if encodedata == "base85":
				ident = b64.b85decode(ident)
			if encodedata == "base64":
				data = b64.b64decode(ident)
			if encodedata == "base16":
				ident = b64.b16decode(ident)
			if encodedata == "base32":
				ident = b64.b32decode(ident)
			if encodedata == "rot13":
				ident = str(ident).decode('rot13')
			if encodedata == "xor":
				ident = ''.join(chr(ord(c)^ord(k)) for c,k in izip(ident, cycle(key)))
			__builtin__.state = "connected"
			print bf+"\t\tATTENTION " +be+bo+"[*] Connected to: "+be+str(ipaddr) +bo+" - " +be+str(ident).strip()
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log failed in tcpsock " + str(logfailed)
		except Exception as tcpconfail:
			__builtin__.state = str(tcpconfail).split("] ")[1]
			print bf+"\t\t[?] Connection attempt failed on port: TCP " + str(ls) + " - to IP Address: " + str(ipaddr) + " - " + str(tcpconfail)+be
			try:
				from log_enable import log_enabled
				log_enabled().logging()
			except Exception as logfailed:
				print "log2 failed in tcpsock " + str(logfailed)
			faillist.append("TCP/"+str(ls))

