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
from exceptcatcher import servarghandler as sah


class args(object):

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
			sah().srvarg2fail(sysarg2fail)
		try:
			if str(sys.argv[3]):
				__builtin__.serverport = sys.argv[3]
			else:
				pass
		except Exception as sysarg3fail:
			sah().srvarg3fail(sysarg3fail)
		try:
			if str(sys.argv[4]):
				__builtin__.atls = str(sys.argv[4])
			else:
				helper().tlshelp()
				sys.exit()
		except Exception as sysarg4fail:
			sah().srvarg4fail(sysarg4fail)