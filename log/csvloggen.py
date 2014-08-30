#!/usr/bin/python2
# encoding: utf-8
#
# module author: subinacls
#

"""
This file is used for csv logging
"""

import csv
import datetime


class csvlogfilegen(object):
	def __init__(self):
		pass

	def csvlog(self):
		with open(str(consultant) + '-' + str(location) + '-' + str(datetime.datetime.now()).split(" ")[0] + \
				          '.csv', 'a', buffering=0) as f:
			writer = csv.writer(f)
			writer.writerow((str(state), str(ipaddr), str(proto) + "/" + str(ls), str(location), str(consultant),
		                 str(datetime.datetime.now()).strip(".")))
			f.close()
