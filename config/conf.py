# encoding: utf-8
#!/usr/bin/env python
#
# module author: subinacls
#

""" Useful information
This file preforms all the ini configuration settings
sets __builtin__ vars to be used throughout the application
"""

import verinfo
from bcolors import bcolors
import sys
import ConfigParser
import __builtin__
from diagforall import clientconfdiag
import datetime

global failconfig

#create a disctionary to store all configuration information
__builtin__.dict1 = {}

class confsecmap:

	global Config
	Config = ConfigParser.ConfigParser()
	Config
	try:
		read_config = Config.read(conffile)
		read_config
		Config.sections()
	except Exception as configreadfail:                                                   
		print("\nERROR CONFIGURATION READ CONDITION in conf.py: %s\n" % configreadfail)       
		sys.exit(0) # exit on failure to read configuration file

	def ConfigSectionMap(section):                                                        
		options = Config.options(section)                                                 
		for option in options:                                                            
			try:                                                                          
				dict1[option] = Config.get(section, option)                               
				if dict1[option] == -1:                                                   
					print("Option has no var to set: %s" % option)                        
			except Exception as optionfailure:                                            
				print("\nERROR CONDITION IN READ OPTIONS in conf.py: %s\n" % optionfailure)
				print ""
				sys.exit(0)
		return dict1

	ldate = datetime.datetime.now().date()
	try:
		try:
			try:
				if Config.get("SectionOne", "target") != "":
					__builtin__.diag = ConfigSectionMap("SectionOne")["diagnostics"]
			except Exception as diagconffail:
				__builtin__.diag = False
				pass
			try:
				if Config.get("SectionOne", "target") != "":
					__builtin__.ipaddr = ConfigSectionMap("SectionOne")["target"]
			except Exception as targetconffail:
				__builtin__.ipaddr = "127.0.0.1"
				pass
			try:
				if Config.get("SectionOne", "types") != "":
					__builtin__.scantype = ConfigSectionMap("SectionOne")["types"]
			except Exception as typesconffail:
				__builtin__.scantype = "connect"
				pass
			try:
				if Config.get("SectionOne", "spoof") != "":
					__builtin__.spoofipaddr = ConfigSectionMap("SectionOne")["spoof"]
			except Exception as spoofconffail:
				__builtin__.spoofipaddr = "no"
				pass
			try:
				if Config.get("SectionOne", "range") != "":
					__builtin__.portr = ConfigSectionMap("SectionOne")["range"]
			except Exception as rangeconffail:
				__builtin__.portr = "1000-2000"
				pass
			try:
				if Config.get("SectionOne", "protocol") != "":
					__builtin__.flipbit = ConfigSectionMap("SectionOne")["protocol"]
					__builtin__.fb = flipbit
					__builtin__.proto = flipbit
			except Exception as protoconffail:
				__builtin__.flipbit = "TCP"
				__builtin__.fb = flipbit
				__builtin__.proto = flipbit
				pass
			try:
				if Config.get("SectionOne", "consultant") != "":
					__builtin__.consultant = ConfigSectionMap("SectionOne")["consultant"]
			except Exception as conconffail:
				__builtin__.consultant = "yournamehere"
				pass
			try:
				if Config.get("SectionOne", "location") != "":
					__builtin__.location = ConfigSectionMap("SectionOne")["location"]
			except Exception as locconffail:
				__builtin__.location = "yourlocationhere"
				pass
			try:
				if Config.get("SectionOne", "random") != "":
					__builtin__.randomness = ConfigSectionMap("SectionOne")["random"]
			except Exception as randomconffail:
				__builtin__.randomness = "False"
				pass
			try:
				if Config.get("SectionTwo", "sleep") != "":
					__builtin__.sleepy = ConfigSectionMap("SectionTwo")["sleep"]
			except Exception as sleepconffail:
				__builtin__.sleepy = "1"
				pass
			try:
				if Config.get("SectionTwo", "nappy") != "":
					__builtin__.nappy = ConfigSectionMap("SectionTwo")["nappy"]
			except Exception as nappyconffail: 
				__builtin__.nappy = "5"
				pass
			try:
				if Config.get("SectionTwo", "dwell") != "":
					__builtin__.rester = ConfigSectionMap("SectionTwo")["dwell"]
			except Exception as restertypefail:
				__builtin__.rester = "1"
				pass
			try:
				if Config.get("SectionThree", "suppress") != "":
					__builtin__.suppress = ConfigSectionMap("SectionThree")["suppress"]
			except Exception as suppressconffail: 
				__builtin__.suppress = "False"
				pass
			try:
				if Config.get("SectionThree", "logging") != "":
					__builtin__.logging = ConfigSectionMap("SectionThree")["logging"]
			except Exception as loggingconffail: 
				__builtin__.logging = "False"
				pass
			try:
				if Config.get("SectionThree", "logtype") != "":
					__builtin__.logtype = ConfigSectionMap("SectionThree")["logtype"]
			except Exception as logtypefail: 
				__builtin__.logtype = ""
				pass
			try:
				if Config.get("SectionThree", "covert") != "":
					__builtin__.covert = ConfigSectionMap("SectionThree")["covert"]
			except Exception as convertconffail:
				__builtin__.covert = False
				pass
			__builtin__.dict1 = dict1
			clientconfdiag().diagconfig()
		except Exception as failconfig:
			if str(diag).lower() in ["true","yes"]:
				print "Configuration failed in conf.py, reason: " + str(failconfig)
			sys.exit(0)
	except Exception as confcatchall:
		if str(diag).lower() in ["true","yes"]:
			print confcatchall, "configuration failed, hit catch all"
		sys.exit(0)
