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
global failconfig
import sys
import ConfigParser
import __builtin__
from diagforall import clientconfdiag
import datetime

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
			if Config.get("SectionOne", "target") != "":
				__builtin__.ipaddr = ConfigSectionMap("SectionOne")["target"]
			if Config.get("SectionOne", "target") == "":
				__builtin__.ipaddr = "127.0.0.1"
			if Config.get("SectionOne", "types") != "":
				__builtin__.scantype = ConfigSectionMap("SectionOne")["types"]
			if Config.get("SectionOne", "types") == "":
				__builtin__.scantype = "connect"
			if Config.get("SectionOne", "spoof") != "":
				__builtin__.spoofipaddr = ConfigSectionMap("SectionOne")["spoof"]
			if Config.get("SectionOne", "spoof") == "":
				__builtin__.spoofipaddr = "no"
			if Config.get("SectionOne", "range") != "":
				__builtin__.portr = ConfigSectionMap("SectionOne")["range"]
			if Config.get("SectionOne", "range") == "":
				__builtin__.portr = "1000-2000"
			if Config.get("SectionOne", "protocol") != "":
				__builtin__.flipbit = ConfigSectionMap("SectionOne")["protocol"]
				__builtin__.fb = flipbit
				__builtin__.proto = flipbit
			if Config.get("SectionOne", "protocol") == "":
				__builtin__.flipbit = "TCP"
				__builtin__.fb = flipbit
				__builtin__.proto = flipbit
			if Config.get("SectionOne", "consultant") != "":
				__builtin__.consultant = ConfigSectionMap("SectionOne")["consultant"]
			if Config.get("SectionOne", "consultant") == "":
				__builtin__.consultant = "yournamehere"
			if Config.get("SectionOne", "location") != "":
				__builtin__.location = ConfigSectionMap("SectionOne")["location"]
			if Config.get("SectionOne", "location") == "":
				__builtin__.location = "yourlocationhere"
			if Config.get("SectionOne", "random") != "":
				__builtin__.randomness = ConfigSectionMap("SectionOne")["random"]
			if Config.get("SectionOne", "random") == "":
				__builtin__.randomness = "False"
			if Config.get("SectionTwo", "sleep") != "":
				__builtin__.sleepy = ConfigSectionMap("SectionTwo")["sleep"]
			if Config.get("SectionTwo", "sleep") == "":
				__builtin__.sleepy = "1"
			if Config.get("SectionTwo", "nappy") != "":
				__builtin__.nappy = ConfigSectionMap("SectionTwo")["nappy"]
			if Config.get("SectionTwo", "nappy") == "":
				__builtin__.nappy = "5"
			if Config.get("SectionTwo", "dwell") != "":
				__builtin__.rester = ConfigSectionMap("SectionTwo")["dwell"]
			if Config.get("SectionTwo", "dwell") == "":
				__builtin__.rester = "1"
			if Config.get("SectionThree", "suppress") != "":
				__builtin__.suppress = ConfigSectionMap("SectionThree")["suppress"]
			if Config.get("SectionThree", "suppress") == "":
				__builtin__.suppress = "False"
			if Config.get("SectionThree", "logging") != "":
				__builtin__.logging = ConfigSectionMap("SectionThree")["logging"]
			if Config.get("SectionThree", "logging") == "":
				__builtin__.logging = "False"
			if Config.get("SectionThree", "logtype") != "":
				__builtin__.logtype = ConfigSectionMap("SectionThree")["logtype"]
			if Config.get("SectionThree", "logtype") == "":
				__builtin__.logtype = ""
			if Config.get("SectionThree", "covert") != "":
				__builtin__.covert = ConfigSectionMap("SectionThree")["covert"]
			if Config.get("SectionThree", "covert") == "":
				__builtin__.covert = False
			__builtin__.dict1 = dict1
			if diag == "yes":
				clientconfdiag().diagconfig()
		except Exception as failconfig:
			if diag == "yes":
				print "Configuration failed in conf.py, reason: " + str(failconfig)
			sys.exit(0)
	except Exception as confcatchall:
		if diag == "yes":
			print confcatchall
		sys.exit(0)