#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

import os
import re
import threading
import SocketServer
from contamination import contaminlog
import __builtin__


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
			contaminlog().jcom_keeper(self.client_address[0],str("tcp").upper(),self.client_address[1],self.data)
			contaminlog().jcom_write()

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	pass

class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.data = self.request[0].strip()
		socket = self.request[1]

		line = str(self.data)
		matchObj = re.match('(.*)On(.*)Port:(.*)By:(.*)From:(.*)On:(.*)', line)
		if matchObj:
			print bo + "Host:" + be+ " " +self.client_address[0] + bo+" - "+ be+ self.data
			socket.sendto(str(self.data[0:10000000]), self.client_address)
		else:
			contaminlog().jcom_read()
			contaminlog().jcom_keeper(self.client_address[0],str("tcp").upper(),self.client_address[1],self.data)
			contaminlog().jcom_write()

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
	pass

class bothserver():
	def __init__(self):
		pass

	def mybothserver(self):
		usocketserver = ThreadedUDPServer(('', int(serverport)), ThreadedUDPRequestHandler)
		usocketserver_thread = threading.Thread(target=usocketserver.serve_forever)
		usocketserver_thread.setDaemon(False)
		usocketserver_thread.start()
		os.popen("iptables -t nat -I PREROUTING -p udp --dport 1:65535 -j REDIRECT --to-ports "+str(serverport))
		os.popen("iptables -t nat -I OUTPUT -p udp -d 127.0.0.1 --dport 1:65535 -j REDIRECT --to-port "+str(serverport))
		tsocketserver = ThreadedTCPServer(('', int(serverport)), ThreadedTCPRequestHandler)
		tsocketserver_thread = threading.Thread(target=tsocketserver.serve_forever)
		tsocketserver_thread.setDaemon(False)
		tsocketserver_thread.start()
		os.popen("iptables -t nat -F")
		os.popen("iptables -t nat -I PREROUTING -p tcp --dport 1:65534 -j REDIRECT --to-ports "+str(serverport))
		os.popen("iptables -t nat -I OUTPUT -p tcp -d 127.0.0.1 --dport 1:65534 -j REDIRECT --to-port "+str(serverport))
		os.popen("iptables -t nat -I PREROUTING -p tcp --dport 65535 -j REDIRECT --to-ports 22")
		os.popen("iptables -t nat -I OUTPUT -p tcp -d 127.0.0.1 --dport 65535 -j REDIRECT --to-port 22")