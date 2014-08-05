#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#


""" Useful information
		gets logging type used if any and configures and starts socket for both TCP and UDP communication
		logs state and information about connection attempts
"""

import __builtin__
import socket
import datetime
from padme import padgen
from encoder import clientencoder


class bothsocks(object):

	def __init__(self):
		pass

	def connecttcpsocket(self):
		try:
			__builtin__.ldate = datetime.datetime.now()  # get current date/time
			__builtin__.proto = str("tcp").upper()  # sets protocol in uppercase for logging

			if str(paddata).lower() in ["true", "yes"]:  # used to make data more random, harder for signatures
				__builtin__.ident = bo + str(padgen().maxipad()) + be + "On " + str(proto) + bo + \
			                    str(padgen().maxipad()) + be + " - Port: " + str(lst) + bo + \
			                    str(padgen().maxipad()) + be + " - By: " + str(consultant) + bo + \
			                    str(padgen().maxipad()) + be + " - From: "  + str(location) + bo + \
			                    str(padgen().maxipad()) + be + " - Date: "  + str(ldate) + bo + \
				                str(padgen().maxipad()) + be
			else:  # if no padding use standard ident information to send
				__builtin__.ident = bo + "On " + be + str(proto) + bo + \
			                    " Port: " + be + str(lst) + bo + \
			                    " - By: " + be + str(consultant) + bo + \
			                    " - From: " + be + str(location) + bo + \
			                    " - Date: " + be + str(ldate) + be

			clientencoder().dataencode(ident)  # check encoding module and produce ident as desired by configuration

			sockobj = socket.socket()  # create the socket object

			if nappy > "1":  # is nappy is a fraction less than 1 -  float socket timeout
				sockobj.settimeout(float(nappy))
			else:
				pass

			#  connect, send, and close the socket

			sockobj.connect((ipaddr, lst))  # basic socket connection
			sockobj.send(ident)  # send ident string
			data2 = sockobj.recv(65535)  # catch anything sent back
			sockobj.close()  # close the socket

			if data2:  # if we recv any data back from server, append to passlist
				passlist.append(str(proto) + "/" + str(lst))
				clientencoder().datadecode(data2)  # check if encode and decode data for displaying
			else:
				pass

			__builtin__.state = "Established"  # set state for the connection

			if str(paddata).lower() in ["true","yes"]:  # if padding was used display generic information to client
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + bo + ": Padded data"
				# passlist.append("TCP/" + str(ls))
			else:
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + str(data)

			from log_enable import log_enabled
			log_enabled().logging()  # try to log data


		except Exception as tcpconfail:  # catch all errors generated - unexpected results
			__builtin__.state = str(tcpconfail).split("]")  # strip out the socket fail reason for display
			faillist.append(str(proto).upper() + "/" + str(lst))  # append to faillist
			print bf + "\t\t[?] Connection attempt failed on TCP port: " + str(lst) + " - to IP Address: " + \
			      str(ipaddr) + " - " + str(tcpconfail) + be

			from log_enable import log_enabled
			log_enabled().logging()  # try to log data

			pass  # nothing to see here - keep moving on ...

	def connectudpsocket(self):
		try:
			__builtin__.ldate = datetime.datetime.now()  # get current date/time
			__builtin__.proto = str("udp").upper()  # sets protocol in uppercase for logging

			if str(paddata).lower() in ["true", "yes"]:  # used to make data more random, harder for signatures
				__builtin__.ident = bo + str(padgen().maxipad()) + be + "On " + str(proto) + bo + \
			                    str(padgen().maxipad()) + be + " - Port: " + str(lsu) + bo + \
			                    str(padgen().maxipad()) + be + " - By: " + str(consultant) + bo + \
			                    str(padgen().maxipad()) + be + " - From: "  + str(location) + bo + \
			                    str(padgen().maxipad()) + be + " - Date: "  + str(ldate) + bo + \
				                str(padgen().maxipad()) + be
			else:  # if no padding use standard ident information to send
				__builtin__.ident = bo + "On " + be + str(proto) + bo + \
			                    " Port: " + be + str(lsu) + bo + \
			                    " - By: " + be + str(consultant) + bo + \
			                    " - From: " + be + str(location) + bo + \
			                    " - Date: " + be + str(ldate) + be

			clientencoder().dataencode(ident)  # check encoding module and produce ident as desired by configuration

			sockobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create the socket object

			if nappy > "1":  # is nappy is a fraction less than 1 -  float socket timeout
				sockobj.settimeout(float(nappy))
			else:
				pass

			sockobj.connect((ipaddr, lsu))  # basic socket connection
			sockobj.send(ident)  # send ident string
			data1 = sockobj.recvfrom(65535)  # catch anything sent back
			sockobj.close()  # close the socket

			if data1:  # if we recv any data back from server, append to passlist
				passlist.append(str(proto).upper() + "/" + str(lsu))
				clientencoder().datadecode(data1)  # check if encode and decode data for displaying
			else:
				pass

			__builtin__.state = "Established"

			if str(paddata).lower() in ["true","yes"]:  # if padding was used display generic information to client
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + bo + ": Padded data"
				# passlist.append("TCP/" + str(ls))
			else:
				print bf + "\t\tATTENTION " + be + bo + "[*] Connected to: " + be + str(ipaddr) + str(data)

			from log_enable import log_enabled
			log_enabled().logging()  # try to log data

		except Exception as udpconfail:  # catch all errors generated - unexpected results
			__builtin__.state = str(udpconfail).split("]")  # strip out the socket fail reason for display
			faillist.append(str(proto).upper() + "/" + str(lsu))  # append to faillist
			print bf + "\t\t[?] Connection attempt failed on UDP port: " + str(lsu) + " - to IP Address: " + \
			      str(ipaddr) + " - " + str(udpconfail) + be

			from log_enable import log_enabled
			log_enabled().logging()

			pass  # nothing to see here - keep moving on