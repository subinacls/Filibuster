# encoding: utf-8
#!/usr/bin/env python
import os
import re
import threading
import SocketServer
import __builtin__


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
			with open('Contaminated_log-'+str(date)+'.txt', 'a', buffering=0) as f:
				f.write(self.data)
				f.close()

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
		os.popen("iptables -t nat -I OUTPUT -p udp -d 127.0.0.1 --dport 1:6553 -j REDIRECT --to-port "+str(serverport))
