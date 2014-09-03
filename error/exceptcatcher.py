#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#


import os
import json
import __builtin__
import binascii
import verinfo
from bcolors import bcolors
from helper import helper
import sys
import time
import datetime

__builtin__.va = __appname__
__builtin__.vv = __version__
__builtin__.vauth = __author__

bh = bcolors.HEADER
bf = bcolors.FAIL
be = bcolors.ENDC
bw = bcolors.WARNING
bo = bcolors.OKBLUE


class skerrorhandler(object):

	def __init__(self):
		pass

	def allserverfail(self, reporterror):
		print "\t[?] " + va + " v." + vv + " - CRASH in server_kicker.py during import of both server: " + \
		      bf + str(reporterror) + "\n" + be
		sys.exit(0)


class sferrorhandler(object):

	def __init__(self):
		pass

	def kbicatcher(self):
		pid = os.getpid()
		os.popen("iptables -t nat -F")
		print bo + "\t[!] User initialized exit - flushed IPTABLES and killed server pid " + \
		      bf + str(pid) + " ...\n" + be
		killer = "kill -9 " + str(pid)
		os.popen(killer)
		sys.exit(0)

	def sfbothfail(self, reporterror):
		print bo + "\t[?] " + va + " v." + vv + " - CRASH in server_func.py during import of both servers: " + \
		      bf + str(reporterror) + "\n" + be
		sys.exit(0)

	def sftcpfail(self, reporterror):
		print bo + "\t[?] " + va + " v." + vv + " - CRASHED during import of tcp server: " + \
		      bf + str(reporterror) + "\n" + be
		sys.exit(0)

	def sfudpfail(self, reporterror):
		print bo + "\t[?] " + va + " v." + vv + " - CRASHED during import of udp servers: " + \
		      bf + str(reporterror) + "\n" + be
		sys.exit(0)

class logenablehandler(object):

	def __init__(self):
		pass

	def logimportfail(self, reporterror):
		print bo+"\t[?] " + va + " v." + vv + " - " + str(logtype).upper() + " CRASHED due to: " + \
		      bf + str(reporterror) + "\n" + be
		sys.exit(0)


class contamloghandler(object):

	def __init__(self):
		pass

	def jsonreadfail(self, reporterror):
		if str(diag).lower() in ["true", "yes", "1"]:
			print bo + "\t[?] Reading saved JSON contamination data from file: Contaminated_log-" + \
			      str(datetime.datetime.now()).split(".")[0] + ".json\n" + be

	def jsonrwritefail(self, reporterror):
		if str(diag).lower() in ["true", "yes", "1"]:
			print bo + "\t[?] Writting JSON contamination data to file: Contaminated_log-" + \
			      str(datetime.datetime.now()).split(".")[0] + ".json\n" + be

	def jsonrkeepfail(self, reporterror):
		if str(diag).lower() in ["true", "yes", "1"]:
			print bo + "\t[?] Processsing received traffic which does not meet criteria " + \
			      str(reporterror) + "\n" + be


class servarghandler(object):

	def __init__(self):
		pass

	def srvarg2fail(self, reporterror):
		print bo + "\n\n\t[?] Please choose: 'TCP or UDP' for the protocol\n" + be
		helper().shelp()
		sys.exit(0)

	def srvarg3fail(self, reporterror):
		print bo + "\n\n\t[?] Please choose: 'Port Number' for the server to bind to\n" + be
		helper().shelp()
		sys.exit(0)

	def srvarg4fail(self, reporterror):
		print bo + "\n\n\t[?] Please choose: 'Yes' or 'No' for the use of TLS\n" + be
		helper().tlshelp()
		sys.exit(0)


class jsonloghandler(object):

	def __init__(self):
		pass

	def jlogreadfail(self, reporterror):
		#print bo+"\t[?] Read access violation in jsonloggen.py: " + str(reporterror) + "\n" + be
		pass

	def jlogwritefail(self, reporterror):
		#print bo+"\t[?] Write access violation in jsonloggen.py: " + str(reporterror) + "\n" + be
		pass

	def jlogfail(self, reporterror):
		#print bo+"\t[?] Keeper access violation in jsonloggen.py: " + str(reporterror) + "\n" + be
		pass

class checkall(object):

	def __init__(self):
		pass

	def findosrel(self):
		with open('/etc/os-release') as eor:
			eorl = eor.readlines()
		isaal = str(eorl[0].split('=')[1].strip().lower())
		if isaal[1] == "\x61" and isaal[2] =="\x72" and isaal[3] == "\x63" and isaal[4] == "\x68" \
		and isaal[5] == isaal[1] and isaal[6:7] == "\x73"  and isaal[8] == isaal[1]  \
		and isaal[9] == "\x75"  and isaal[10] == "\x6c" and isaal[11] == "\x74":
			pass
		else:
			print binascii.unhexlify('596f752073686f756c642073746f7020706c6179696e6720776974682074686520636c6f6e6573210a09557365204172636841737361756c742c2069742773206f726967696e616c')
