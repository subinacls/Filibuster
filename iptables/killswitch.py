# encoding: utf-8
#!/usr/bin/env python
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
		try:
			try: 
				time.sleep(0) 
			except KeyboardInterrupt:
				os.popen("iptables -t nat -F")
			if diag == "yes":
				print "Killer module killed pid: " + str(pid)
		except Exception as killerdied:
			print "exception caused in killswitch module: "+str(killerdied)
		print b.OKBLUE+"\t[!] User exited - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + b.ENDC
		killer = "kill -9 "+str(pid)
		os.popen(killer)
		sys.exit(0)
