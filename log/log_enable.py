#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#
'''
This file is used to determined the logging functionality
'''

import __builtin__

if str(logtype).lower() == "xml":
	from xmlloggen import xmllogfilegen as xml
if str(logtype).lower() == "csv":
	from csvloggen import csvlogfilegen as csv
if str(logtype).lower() in ["txt","text"]:
	from txtloggen import txtlogfilegen as txt
if str(logtype).lower() in ["dic","dict","dictionary","json"]:
	from jsonloggen import jsonlogger as jsonmod

class log_enabled():

	def __init__(self):
		pass

	def logging(self):

		try:
			if str(logtype).lower() == "csv":
				csv().csvlog()
			else:
				pass
		except Exception as notacsv:
			print "CSV failed in " + proto + ": " + str(notacsv)
		try:
			if str(logtype).lower() == "xml":
				xml().xmllog()
			else:
				pass	
		except Exception as notanxml:
			print "XML failed in " + proto + ": " + str(notanxml)
		try:
			if str(logtype).lower() in ["txt", "text"]:
				txt().txtlog()
			else:
				pass
		except Exception as notatxt:
			print "TXT failed in " + proto + ": " + str(notatxt)
		try:
			if str(logtype).lower() in ["dictionary", "dic", "dict", "json"]:
				try:
					jsonmod().json_read(str(consultant)+'-'+str(location)+'-'+str(ldate)+'.json')
					jsonmod().json_keeper()
					jsonmod().json_write(str(consultant)+'-'+str(location)+'-'+str(ldate)+'.json')
				except Exception as jsonlogfail:
					print "json failed"  +str(jsonlogfail)
			else:
				pass
		except Exception as notadict:
			print "JSON failed in " + proto + ": " + str(notadict)

	def contaminationlog(self):

