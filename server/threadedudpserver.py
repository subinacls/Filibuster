#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

import os
import re
import threading
import SocketServer
import __builtin__
from contamination import contaminlog

class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request[0].strip()
		socket = self.request[1]
		try:
			self.line = str(b64.b64decode(self.data))
			matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
		except Exception as notbase64:
			pass
		try:
			self.line = str(self.data)
			matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
		except Exception as notbase64:
			pass
		if matchObj:
			print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.data
			socket.sendto(str(self.data[0:10000000]), self.client_address)
		else:
			contaminlog().jcom_keeper(self.client_address[0], str("udp").upper(), self.client_address[1], self.data)

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
	pass

class udpserver():
	def __init__(self):
		pass

	def myudpserver(self):
		socketserver = ThreadedUDPServer(('', int(serverport)), ThreadedUDPRequestHandler)
		socketserver_thread = threading.Thread(target=socketserver.serve_forever)
		socketserver_thread.setDaemon(False)
		socketserver_thread.start()
		os.popen("iptables -t nat -I PREROUTING -p udp --dport 1:65535 -j REDIRECT --to-ports "+str(serverport))
		os.popen("iptables -t nat -I OUTPUT -p udp -d 127.0.0.1 --dport 1:65535 -j REDIRECT --to-port "+str(serverport))
