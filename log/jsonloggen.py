#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#

""" Useful information
This file preforms all the ini configuration settings
sets __builtin__ vars to be used throughout the application
"""

import json
import __builtin__
from exceptcatcher import jsonloghandler as jlh

class jsonlogger():

	def __init__(self):
		pass # nothing to see here

	def json_read(self):
		try:
			with open(str(consultant)+'-'+str(location)+'-'+str(ldate)+'.json', "r") as f: # open a file as named variable
				__builtin__.rawjson = json.loads(f.read()) # load json data to built in variable
		except Exception as jreadfail: # catch all
			__builtin__.rawjson = json.loads(json.dumps({})) #, indent=4))
			jlh().jlogreadfail(jreadfail)
			pass

	def json_write(self):
		try:
			with open(str(consultant)+'-'+str(location)+'-'+str(ldate)+'.json', "w") as f: # open a file as named variable
				f.write(json.dumps(rawjson)) #, indent=4)) # dumps data to file with indent 4 spaces
		except Exception as jwritefail: # catch all
			jlh().jlogwritefail(jwritefail)
			pass

	def jsonlog(self):
		self.json_read()
		try:
			if consultant not in rawjson.keys(): # check for variable in key values
				rawjson[consultant] = {} # if not in key values, make new key as a dict
			if location not in rawjson[consultant].keys(): # repeated
				rawjson[consultant][location] = {}
			if ldate not in rawjson[consultant][location].keys():
				rawjson[consultant][location][ldate] = {}
			if ipaddr not in rawjson[consultant][location][ldate].keys():
				rawjson[consultant][location][ldate][ipaddr] = {}
			if proto not in rawjson[consultant][location][ldate][ipaddr].keys():
				rawjson[consultant][location][ldate][ipaddr][proto] = {}
			if state not in rawjson[consultant][location][ldate][ipaddr][proto].keys():
				rawjson[consultant][location][ldate][ipaddr][proto][state] = [] # set state as a list
			try: # check if value in both potential string and integer value are in the list
				if str(ls) not in rawjson[consultant][location][ldate][ipaddr][proto][state]:
					rawjson[consultant][location][ldate][ipaddr][proto][state].append(str(ls))
					rawjson[consultant][location][ldate][ipaddr][proto][state].sort(key=int)
			except Exception as baseportfail:
				if ls not in rawjson[consultant][location][ldate][ipaddr][proto][state]:
					rawjson[consultant][location][ldate][ipaddr][proto][state].append(ls)
					rawjson[consultant][location][ldate][ipaddr][proto][state].sort(key=int)
			pass # keep on moving
		except Exception as jkeeperfail: # catch all
			jlh().jlogfail(jkeeperfail)
			pass # keep on keeping no