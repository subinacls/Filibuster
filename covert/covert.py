#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

""" Useful information
This file is for covert tunnel testing
"""

import os
import time
from subprocess import Popen
from socket import *
import dns.resolver


""" handles the icmp tunnel testing """
class icmptunnel(object):

	def __init__(self):
		pass
		
	def ping(self, tunnelspass, tunnelsfail):
		try:
			devnull = open(os.devnull, 'a')
			p = []  # ip -> process
			targets = ['google.com']
			for n in targets:  # start ping processes
				p.append((n, Popen(['ping', '-c', '1', n], stdout=devnull)))
			while p:
				for i, (ip, proc) in enumerate(p[:]):
					if proc.poll() is not None:  # ping finished
						p.remove((ip, proc))  # this makes it O(n**2)
						if proc.returncode == 0:
							tunnelspass.append('icmp')
							#print('%s active' % ip)
						elif proc.returncode == 2:
							tunnelsfail.append('icmp')
							#print('%s no response' % ip)
					else:
						pass
						#print('%s error' % ip)
					time.sleep(.04)
				devnull.close()
		except Exception as icmptunnelfail:
			print icmptunnelfail, "icmp tunnel failed"

""" handles all the ntp time protocol tunnel testing """
class ntptunnel(object):

	def __init__(self):
		pass

	def ntp(self, tunnelspass, tunnelsfail):
		try:
			client = socket(SOCK_DGRAM)
			data = '\x1b' + 47 * '\0'
			client.sendto(data,('pool.ntp.org', 123))
			data, address = client.recvfrom(1024)
			time.sleep(1)
			if data:
				tunnelspass.append('ntp')
			else:
				tunnelsfail.append('ntp')
			client.close()
		except Exception as ntptunnelfail:
			print ntptunnelfail, "ntp tunnel failed"

""" handles all the dns protocol tunnel testing """
class dnstunnel(object):

	def __init__(self):
		pass

	def dnsres(self, tunnelspass, tunnelsfail):
		try:
			answers = dns.resolver.query('dnspython.org', 'A')
			if answers:
				tunnelspass.append('dns')
			else:
				tunnelsfail.append('dns')
		except Exception as dnstunnelfail:
			print dnstunnelfail, "dnstunnel failed"
