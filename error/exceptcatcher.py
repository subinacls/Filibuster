__author__ = 'root'

import os
import __builtin__
import verinfo
from bcolors import bcolors as b
import sys

__builtin__.va = __appname__
__builtin__.vv = __version__
__builtin__.vauth = __author__

bh = bcolors.HEADER
bf = bcolors.FAIL
be = bcolors.ENDC
bw = bcolors.WARNING
bo = bcolors.OKBLUE

class skerrorhandler():

	def __init__(self):
		pass

	def bothserverfail(self,reporterror):
		print "\t[?] " +va+" v."+vv+" - CRASH in server_kicker.py during import of tcp servers: " + bf + str(reporterror) + "\n" +be
		sys.exit(0)

	def udpserverfail(self,reporterror):
		print "\t[?] " +va+" v."+vv+" - CRASH in server_kicker.py during import of tcp servers: " + bf + str(reporterror) + "\n" +be
		sys.exit(0)

	def tcpserverfail(self,reporterror):
		print "\t[?] " +va+" v."+vv+" - CRASH in server_kicker.py  during import of tcp servers: " + bf + str(reporterror) + "\n" +be
		sys.exit(0)

class sferrorhandler():

	def __init__(self):
		pass

	def kbicatcher(self):
		pid = os.getpid()
		os.popen("iptables -t nat -F")
		print bo+"\t[!] User initialized exit - flushed IPTABLES and killed server pid "+str(pid)+" ...\n" + be
		killer = "kill -9 "+str(pid)
		os.popen(killer)
		sys.exit(0)

	def sfbothfail(self,reporterror):
		print "\t[?] " +va+" v."+vv+" - CRASH in server_func.py during import of both servers: " + bf + \
				str(reporterror) + "\n" +be
		sys.exit(0)









