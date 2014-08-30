#!/usr/bin/python2
# encoding: utf-8
#
# module author: subinacls
#


import os
import sys
import time
import verinfo
import __builtin__
from bcolors import bcolors
from exceptcatcher import sferrorhandler as sfh

__builtin__.va = __appname__
__builtin__.vv = __version__
__builtin__.vauth = __author__

bh = bcolors.HEADER
bf = bcolors.FAIL
be = bcolors.ENDC
bw = bcolors.WARNING
bo = bcolors.OKBLUE


class tcp_servers(object):

	def __init__(self):
		pass

	def tserver(self):
		try:
			from threadedtcpserver import ThreadedTCPRequestHandler, ThreadedTCPServer, tcpserver
			tcpserver().mytcpserver()
			try:
				while 1:
					time.sleep(0)
			except KeyboardInterrupt:
				sfh().kbicatcher()
		except Exception as tcpserverfail:
			sfh().sftcpfail(tcpserverfail)


class udp_servers(object):

	def __init__(self):
		pass

	def userver(self):
		try:
			from threadedudpserver import ThreadedUDPRequestHandler, ThreadedUDPServer, udpserver
			udpserver().myudpserver()
			try:
				while 1:
					time.sleep(0)
			except KeyboardInterrupt:
				sfh().kbicatcher()
		except Exception as udpserverfail:
			sfh().sfudpfail(udpserverfail)


class both_servers(object):

	def __init__(self):
		pass

	def bserver(self):
		try:

			from threadedbothserver import ThreadedTCPRequestHandler, ThreadedTCPServer, bothserver
			from threadedbothserver import ThreadedUDPRequestHandler, ThreadedUDPServer
			bothserver().mybothserver()
			try:
				while 1:
					time.sleep(0)
			except KeyboardInterrupt:
				sfh().kbicatcher()
		except Exception as bothserverfail:
			sfh().sfbothfail(bothserverfail)