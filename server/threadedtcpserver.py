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
import base64 as b64
from contamination import contaminlog


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler): 
	def handle(self): 
		self.data = self.request.recv(1024).strip()
		if self.data:
			try:
				#xor routing taken from https://dustri.org/
				# Stupid XOR demo
				from itertools import cycle, izip
				key = 's3cr3t'
				self.line = ''.join(chr(ord(c)^ord(k)) for c,k in izip(self.data, cycle(key)))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
				if matchObj:
					print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.line
					self.request.send(self.data)
			except Exception as notbase16:
				pass
			try:
				self.line = str(self.data).decode('rot13')
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
				if matchObj:
					print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.line
					self.request.send(self.data)
			except Exception as notbase16:
				pass
			try:
				self.line = str(b64.b85decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
				if matchObj:
					print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.line
					self.request.send(self.data)
			except Exception as notbase16:
				pass
			try:
				self.line = str(b64.b64decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
				if matchObj:
					print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.line
					self.request.send(self.data)
			except Exception as notbase64:
				pass
			try:
				self.line = str(b64.b32decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
				if matchObj:
					print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.line
					self.request.send(self.data)
			except Exception as notbase64:
				pass
			try:
				self.line = str(b64.b16decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
				if matchObj:
					print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.line
					self.request.send(self.data)
			except Exception as notbase16:
				pass
			try:
				self.line = self.data
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', self.line)
				if matchObj:
					print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.data
					self.request.send(self.data)
			except Exception as notplaintxt:
				pass
		else:
			contaminlog().jcom_keeper(self.client_address[0],str("tcp").upper(),self.client_address[1],self.data)

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