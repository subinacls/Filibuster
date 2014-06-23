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
from bcolors import bcolors as b

class killswitch:

	def __init__(self):
		pass

	def killswitch(self, pid):
		#
		# determined this file needs to handle its own exceptions, no offloading
		#
		try:
			try: 
				time.sleep(0) # dirty hack to monitor for keybard interrupt
			except KeyboardInterrupt:
				os.popen("iptables -t nat -F")
			if str(diag).lower() in ["true","yes"]:
				print "Killer module killed pid: " + str(pid)
		except Exception as killerdied:
			print "exception caused in killswitch module: "+str(killerdied)
		print b.OKBLUE+"\t[!] User exited - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + b.ENDC
		killer = "kill -9 "+str(pid)
		os.popen(killer)
		sys.exit(0)
