# encoding: utf-8
#!/usr/bin/env python
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

""" handles the icmp tunnel testing """
class icmptunnel:

	def __init__(self):
		pass
		
	def ping(self, tunnelspass, tunnelsfail):
		try:
			devnull = open(os.devnull, 'a')
			p = [] # ip -> process
			targets = ['google.com']
			for n in targets: # start ping processes
				p.append((n, Popen(['ping', '-c', '3', n], stdout=devnull)))
			while p:
				for i, (ip, proc) in enumerate(p[:]):
					if proc.poll() is not None: # ping finished
						p.remove((ip, proc)) # this makes it O(n**2)
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
class ntptunnel:

	def __init__(self):
		pass

	def ntp(self,tunnelspass, tunnelsfail):
		try:
			client = socket( AF_INET, SOCK_DGRAM )
			data = '\x1b' + 47 * '\0'
			client.sendto( data, ( 'pool.ntp.org', 123 ))
			data, address = client.recvfrom( 1024 )
			time.sleep(1)
			if data:
				tunnelspass.append('ntp')
			else:
				tunnelsfail.append('ntp')
			client.close()
		except Exception as ntptunnelfail:
			print ntptunnelfail, "ntp tunnel failed"

""" handles all the dns protocol tunnel testing """
class dnstunnel:

	def __init__(self):
		pass

	def dns(self, tunnelspass, tunnelsfail):
		try:
			answers = dns.resolver.query('dnspython.org', 'A')
			if answers:
				tunnelspass.append('dns')
			else:
				tunnelsfail.append('dns')
		except Exception as dnstunnelfail:
			print dnstunnelfail, "dnstunnel failed"

""" set basic list for gathering for covert tunnel testing """
tunnelspass = []
tunnelsfail = []
print(bh + "\n\t[-] Starting Covert tunnel testing process now ..." + be)
""" initalize tunnel testing """

""" actual covert testing calls to the previous set classes """
icmptunnel().ping(tunnelspass, tunnelsfail)
ntptunnel().ntp(tunnelspass, tunnelsfail)
dnstunnel().dns(tunnelspass, tunnelsfail)
print bh + "\n\t[-] Finished Cover tunnel testing process ..." + be

""" print findings for covert testing """
if tunnelspass:
	print(bh + "\n\t[-] List of passed Covert tunnels ...\n" + be)
	for tp in tunnelspass:
		""" adult toilet jokes, he said tp """
		printfunction().pfunc("\t\t[!] Cover tunnel: ",str(tp))

if tunnelsfail:
	print(bh + "\n\t[-] List of failed Covert tunnels ...\n" + be)
	for tf in tunnelsfail:
		printfunction().pfunc("\t\t[!] Cover tunnel: ",str(tf))

diagclientheader().clientheader()
if str(diag).lower() in ["true","yes"]:
	print(bh+"\n\t[-] Entering the Client portion of application\n"+be)
	printfunction().pfunc("\t\t[!] System Argument position 1 is set to: ",sa1)
else:
	pass