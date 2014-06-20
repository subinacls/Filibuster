# encoding: utf-8
#!/usr/bin/env python

"""
file takes argv 1 var and passes it to a if statement which evaluates the supplied function to determine the flow of
the application from there on, it will be a server or a client. This can also be created into a seperate application
specific to the functionality desired for smaller payload to deploy.
"""

import sys


""" import modules after directory structure appended to system $PATH """

from bcolors import bcolors as b
from pcolors import *
from helper import *
from diagforall import diagserverheader
from killswitch import *

""" set some color variable shortcuts """
bh = b.HEADER
bf = b.FAIL
be = b.ENDC
bw = b.WARNING
bo = b.OKBLUE

""" import server args class to handle commandline arguments """

class initserver():

	def __init__(self):
		pass

	def serverrun(self):
		diagserverheader().serverheader()
		print bh+ va +" Server Initialized: ~ " + "ver.: "+ vv +  " - " + vauth +"\n\n"+ be
		ap = str(servproto)
		""" check system arguments for protocol to use """
		"""
		This section handles the protocol and encryption staging for the server portion of the application
		"""
		""" handling TCP protocol staging for server """
		if str(ap).lower() in ["tcp","t"]:
			""" check if protocol is tcp """
			try:
				""" check if tls is being used or not """
				if str(atls).lower() in ["yes","y"]:
					from server_func import tls_servers
					""" import tcp server functionality module """
					tcp_servers().tlsserver(ap)
					""" TLS/TCP server port from user supplied argument """
				else:
					from server_func import tcp_servers
					""" import tcp server functionality module """
					tcp_servers().tserver()
					""" set TCP server port from user supplied argument """
			except Exception as tcpserverfuncfail:
				print "\t[?] " +va+" v."+vv+" - CRASHED during import of tcp servers: " + bf + \
				      str(tcpserverfuncfail) + "\n" +be
				sys.exit(0)
		""" handling UDP protocol staging for server """
		if str(ap).lower() in ["udp","u"]:
			""" check if protocol is udp """
			try:
				""" check if tls is being used or not """
				if str(atls).lower() in ["yes","y"]:
					from server_func import tls_servers
					""" import udp server functionality module """
					udp_servers().dtlsserver(ap)
					""" TLS/TCP server port from user supplied argument """
				else:
					from server_func import udp_servers
					""" import udp server functionality module """
					udp_servers().userver()
					""" set udp server port from user supplied argument """
			except Exception as udpserverfuncfail:
				print "\t[?] " +va+" v."+vv+" - CRASHED during import of tcp servers: " + bf + \
				      str(udpserverfuncfail) + "\n" +be
				sys.exit(0)