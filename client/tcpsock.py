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
import __builtin__
import base64 as b64

class tcpsocks():

	def __init__(self):
		pass

	def connectsocket(self):
		try:
			__builtin__.proto = str("tcp").upper()
			__builtin__.ident = bo+"On "+be+str(proto)+bo+" Port: "+be+str(ls)+bo+" - By: "+be+str(consultant)+bo+" - From: "+be+str(location)+bo+" - On: "+be +str(ldate)
			if encodedata in ["base85","b85"]:
				ident = b64.b85encode(ident)
			if encodedata in ["base64", "b64"]:
				ident = b64.b64encode(ident)
			if encodedata in ["base32", "b32"]:
				ident = b64.b32encode(ident)
			if encodedata in ["base16", "b16"]:
				ident = b64.b16encode(ident)
			if encodedata in ["rot13", "rot", "r13"]:
				ident = str(ident).encode('rot13')
			if encodedata in ["xor", "OR"]:
				#xor routing taken from https://dustri.org/
				# Stupid XOR demo
				from itertools import cycle, izip
				key = 'filterbuster'
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
				if encodedata == "base85":
					ident = b64.b85decode(data)
				if encodedata == "base64":
					ident = b64.b64decode(data)
				if encodedata == "base16":
					ident = b64.b16decode(data)
				if encodedata == "base32":
					ident = b64.b32decode(data)
				if encodedata == "rot13":
					ident = str(data).decode('rot13')
				if encodedata == "xor":
					ident = ''.join(chr(ord(c)^ord(k)) for c,k in izip(data, cycle(key)))
				__builtin__.state = "Established"
				print bf+"\t\tATTENTION " +be+bo+"[*] Connected to: "+be+str(ipaddr) +bo+" - " +be+str(ident).strip()
			else:
				pass
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

