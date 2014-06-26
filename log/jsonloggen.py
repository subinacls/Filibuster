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
import datetime
from exceptcatcher import jsonloghandler as jlh

__builtin__.jlogback = {}


class jsonlogger():

	global rawjson
	__builtin__rawjson = ""
	def __init__(self):
		pass # nothing to see here

	def json_read(self):
		try:
			with open(str(consultant)+'-'+str(location)+'-'+str(datetime.datetime.now()).split(" ")[0]+'.json', "r") as __builtin__.f: # open a file as named variable
				__builtin__.rawjson = json.loads(f.read()) # load json data to built in variable
		except Exception as jreadfail: # catch all
			__builtin__.rawjson = json.loads(json.dumps({})) #, indent=4))
			jlh().jlogreadfail(jreadfail)
			if jlogback != "": # really dirty hack to keep a log ...
				rawjson = json.loads(json.dumps(jlogback)) #, indent=4)) # modify to add tabs to logfile
			else:
				rawjson = json.loads(json.dumps({})) #, indent=4)) # modify to add tabs to logfile
				pass

	def json_write(self):
		try:
			with open(str(consultant)+'-'+str(location)+'-'+str(datetime.datetime.now()).split(" ")[0]+'.json', "w") as __builtin__.f: # open a file as named variable
				f.write(json.dumps(rawjson)) #, indent=4)) # dumps data to file with indent 4 spaces
				jlogback = dict(rawjson)
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
			if str(ldate).split(" ")[0] not in rawjson[consultant][location].keys():
				rawjson[consultant][location][str(ldate).split(" ")[0]] = {}
			if ipaddr not in rawjson[consultant][location][str(ldate).split(" ")[0]].keys():
				rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr] = {}
			if proto not in rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr].keys():
				rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto] = {}
			if state not in rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto].keys():
				rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto][state] = [] # set state as a list
			try: # check if value in both potential string and integer value are in the list
				if str(ls) not in rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto][state]:
					rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto][state].append(str(ls))
					rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto][state].sort(key=int)
			except Exception as baseportfail:
				if ls not in rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto][state]:
					rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto][state].append(ls)
					rawjson[consultant][location][str(ldate).split(" ")[0]][ipaddr][proto][state].sort(key=int)
			self.json_write()
			pass # keep on moving
		except Exception as jkeeperfail: # catch all
			jlh().jlogfail(jkeeperfail)
			pass # keep on keeping no