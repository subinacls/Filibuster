#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

import os
import re
import threading
import SocketServer
import socket
import __builtin__
import base64 as b64
from contamination import contaminlog


"""
This is the TCP Threaded server portiong of the application
Some processing of the data is done here which is then reflected back to the client
Any future encoding/hashing/encryption function should be added to their respective file
and then patched into the threadedtcprequesthandler """


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler): 
	def handle(self): 
		self.data = self.request.recv(65535).strip()
		if self.data:
			try:
				from itertools import cycle, izip
				key = 'filterbuster'
				self.line = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(self.data, cycle(key)))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = ": Filterbuster - " + self.line
					self.data = ''.join(chr(ord(c) ^ ord(k)) for c, k in izip(self.data, cycle(key)))
					self.request.send(self.data)
			except Exception as notxor:
				pass
			try:
				self.line = str(self.data).decode('rot13')
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = str(" : Filterbuster = "+str(self.line)).encode('rot13')
					self.request.send(self.data)
			except Exception as notro13:
				pass
			try:
				self.line = str(b64.b85decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be+ " " +self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b85encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase85:
				pass
			try:
				self.line = str(b64.b64decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " +self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b64encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase64:
				pass
			try:
				self.line = str(b64.b32decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b85encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase64:
				pass
			try:
				self.line = str(b64.b16decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b85encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase16:
				pass
			try:
				self.line = self.data
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.request.send(" : Filterbuster - " + self.data)
			except Exception as notplaintxt:
				pass

			try:
				self.line = str(b64.b16decode(self.data))
				matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)Date:(.*)', self.line)
				if matchObj:
					print bf + "\t\tATTENTION " + bo + "[*] Connection from:" + be + " " + self.client_address[0] + \
					      bo + " - " + be + self.line
					self.data = b64.b85encode(" : Filterbuster - " + str(self.line))
					self.request.send(self.data)
			except Exception as notbase16:
				pass

		else:
			contaminlog().jcom_keeper(self.client_address[0], str("tcp").upper(), self.client_address[1], self.data)


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