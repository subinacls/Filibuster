# encoding: utf-8
#!/usr/bin/env python
"""
server arguments checking
"""
import sys
import __builtin__

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
			from helper import helper
			print sysarg2fail
			helper().shelp()
			sys.exit()
		try:
			if str(sys.argv[3]):
				__builtin__.serverport = sys.argv[3]
			else:
				pass
		except Exception as sysarg3fail:
			from helper import shelp
			print sysarg3fail
			helper().shelp()
			sys.exit(0)
		try:
			if str(sys.argv[4]):
				__builtin__.atls = sys.argv[4]
			else:
				from helper import tlshelp
				helper().tlshelp()
				sys.exit()
		except Exception as sysarg4fail:
			print "\tPlease choose: 'Yes' or 'No' for the use of TLS", str(e) + "\n\n"
			from helper import tlshelp
			print sysarg4fail
			helper().tlshelp()
			sys.exit()