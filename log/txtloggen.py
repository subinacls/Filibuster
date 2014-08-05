#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

"""
This file generates the txt log
"""

import datetime


class txtlogfilegen(object):
	def __init__(self):
		pass

	def txtlog(self):
		with open(str(consultant) + '-' + str(location) + '-' + str(ldate) + '.txt', 'a', buffering=0) as txtlogwrite:
			txtlogwrite.write(
				"Location: " + str(consultant) + " State: " + str(state) + " IP: " + str(ipaddr) + " Proto: " +
				str(proto) + " Port: " + str(base_port) + " Consultant: " + str(location) + " Date: " +
				str(datetime.datetime.now()).strip("."))
			txtlogwrite.close()
