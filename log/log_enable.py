#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#
"""
This file is used to determined the logging functionality
"""

from exceptcatcher import logenablehandler as leh

if str(logtype).lower() == "xml":
	from xmlloggen import xmllogfilegen as xml
if str(logtype).lower() == "csv":
	from csvloggen import csvlogfilegen as csv
if str(logtype).lower() in ["txt", "text"]:
	from txtloggen import txtlogfilegen as txt
if str(logtype).lower() in ["dic", "dict", "dictionary", "json"]:
	from jsonloggen import jsonlogger as json


class log_enabled(object):

	def __init__(self):
		pass

	def logging(self):

		try:
			if str(logtype).lower() == "csv":
				csv().csvlog()
			if str(logtype).lower() == "xml":
				xml().xmllog()
			if str(logtype).lower() in ["txt", "text"]:
				txt().txtlog()
			if str(logtype).lower() in ["dictionary", "dic", "dict", "json"]:
				json().jsonlog()
			else:
				pass
		except Exception as notalog:
			leh().logimportfail(notalog)
