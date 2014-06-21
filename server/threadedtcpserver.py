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


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler): 
	def handle(self): 
		self.data = self.request.recv(1024).strip()
		line = str(self.data)
		matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', line)
		if matchObj:
			print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.data 
			self.request.send(self.data) 
		else:
			contaminlog().jcom_read()
			contaminlog().jcom_keeper()
			contaminlog().jcom_write()

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass
  
class tcpserver():
	def __init__(self):
		pass

	def mytcpserver(self):
		__builtin__.socketserver = ThreadedTCPServer(('', int(serverport)), ThreadedTCPRequestHandler)
		socketserver_thread = threading.Thread(target=socketserver.serve_forever)
		socketserver_thread.setDaemon(False)
		socketserver_thread.start()
		os.popen("iptables -t nat -F")
		os.popen("iptables -t nat -I PREROUTING -p tcp --dport 1:65534 -j REDIRECT --to-ports "+str(serverport)) 
		os.popen("iptables -t nat -I OUTPUT -p tcp -d 127.0.0.1 --dport 1:65534 -j REDIRECT --to-port "+str(serverport)) 
		os.popen("iptables -t nat -I PREROUTING -p tcp --dport 65535 -j REDIRECT --to-ports 22")
		os.popen("iptables -t nat -I OUTPUT -p tcp -d 127.0.0.1 --dport 65535 -j REDIRECT --to-port 22")