#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#
"""
server arguments checking
"""
import sys
import __builtin__
from helper import helper

class args():

	def __init__(self):
		pass

	def getservargs(self):
		try:
			if str(sys.argv[2]):
				__builtin__.servproto = sys.argv[2]

			else:
				helper().shelp()
				sys.exit()
		except Exception as sysarg2fail:
			print "\tPlease choose: 'TCP or UDP' for the protocol", str(sysarg2fail) + "\n\n"
			helper().shelp()
			sys.exit()
		try:
			if str(sys.argv[3]):
				__builtin__.serverport = sys.argv[3]
			else:
				pass
		except Exception as sysarg3fail:
			print "\tPlease choose: 'Port Number' for the server to bind to", str(sysarg3fail) + "\n\n"
			helper().shelp()
			sys.exit(0)
		try:
			if str(sys.argv[4]):
				__builtin__.atls = str(sys.argv[4])
			else:
				helper().tlshelp()
				sys.exit()
		except Exception as sysarg4fail:
			print "\tPlease choose: 'Yes' or 'No' for the use of TLS", str(sysarg4fail) + "\n\n"
			helper().tlshelp()
			sys.exit()