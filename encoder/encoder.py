#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

import base64 as b64
import __builtin__
from itertools import cycle, izip


class clientencoder(object):

	def __init__(self):
		pass

	def dataencode(self, ident):
		try:
			#print "Start of encoding routine" # diagnostics
			try:
				if encodedata == "base85":
					__builtin__.encident = b64.b85encode(ident)
				if encodedata == "base64":
					__builtin__.encident = b64.b64encode(ident)
				if encodedata == "base32":
					__builtin__.encident = b64.b32encode(ident)
				if encodedata == "base16":
					__builtin__.encident = b64.b16encode(ident)
				if encodedata == "rot13":
					__builtin__.encident = str(ident).encode('rot13')
				if encodedata == "xor":
					key = 'filterbuster'
					__builtin__.encident = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(ident, cycle(key)))
				if encodedata == "url":
					pass  # do url
				if encodedata == "lzma":
					pass  # do lzma
				if encodedata in ["gz", "gzip"]:
					pass  # do gzip
				if encodedata in ["binary", "bytestring"]:
					pass  # do gzip
				if encodedata in ["plain", "plaintext", "cleartext", "clear"]:
					pass  # do gzip
				#print "Stop of encoding routine" # diagnostics
			except Exception as failedtoencode:
				pass
		except Exception as e:
			print e

	def datadecode(self, data):
		try:
			#print "Start of decoding routine" # diagnostics
			if str(proto).lower() == "udp":
				try:
					if encodedata == "base85":
						__builtin__.decdata = b64.b85decode(data[0])
					if encodedata == "base64":
						__builtin__.decdata = b64.b64decode(data[0])
					if encodedata == "base16":
						__builtin__.decdata = b64.b16decode(data[0])
					if encodedata == "base32":
						__builtin__.decdata = b64.b32decode(data[0])
					if encodedata == "rot13":
						__builtin__.decdata = str(data[0]).decode('rot13')
					if encodedata == "xor":
						key = 'filterbuster'
						__builtin__.decdata = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(data[0], cycle(key)))
					#print "Stop of decoding routine" # diagnostics
				except Exception as failedtodecode:
					pass
			if str(proto).lower() == "tcp":
				try:
					if encodedata == "base85":
						__builtin__.decdata = b64.b85decode(data)
					if encodedata == "base64":
						__builtin__.decdata = b64.b64decode(data)
					if encodedata == "base16":
						__builtin__.decdata = b64.b16decode(data)
					if encodedata == "base32":
						__builtin__.decdata = b64.b32decode(data)
					if encodedata == "rot13":
						__builtin__.decdata = str(data).decode('rot13')
					if encodedata == "xor":
						key = 'filterbuster'
						__builtin__.decdata = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(data, cycle(key)))
					#print "Stop of decoding routine" # diagnostics
				except Exception as failedtodecode:
					pass
		except Exception as e:
			print e