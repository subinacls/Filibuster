#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#
'''
This file kills the app when user enters CTRL+C
'''

import os
import sys
import time
import __builtin__
from bcolors import bcolors as b

class killswitch:
	def __init__(self):
		pass

	def skillswitch(self):
		#
		# determined this file needs to handle its own exceptions, no offloading
		#
		try:
			try: 
				time.sleep(0) # dirty hack to monitor for keybard interrupt
			except KeyboardInterrupt:
				if str(__builtin__.sa1) in ["client","c"]:
					print b.OKBLUE+"\t[!] User exited - closed log file ...\n" + b.ENDC
					sys.exit(0)
				if str(_builtin__.sa1) in ["server","s"]:
					os.popen("iptables -t nat -F")
					if str(_builtin__.diag).lower() in ["true","yes"]:
						print "Killer module killed pid: " + str(pid)
					print b.OKBLUE+"\t[!] User exited - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + b.ENDC
					pid = os.getpid()
					killer = "kill -9 "+str(pid)
					os.popen(killer)
					sys.exit(0)
		except Exception as killerdied:
			print "exception caused in killswitch module: "+str(killerdied)
			sys.exit(0)

