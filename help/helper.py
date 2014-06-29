#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#
"""
Help information handled in this file
"""
import sys
import verinfo
from bcolors import bcolors as b

vb = __credits__
va = __appname__
vv = __version__
vauth = __author__
bh = b.HEADER
be = b.ENDC


class helper(object):
	""" display basic help information to use when there is NO supplied arguments on the commandline """

	def helpall(self):
		print bh + """

    ~ """ + va + ": " + vv + " - " + vauth + """
    [*] ----------------------------------------------------------------------------
    [*] Egress Filter verification and Covert Channel testing suite
    [*]
    [*] For further help try the following arguments:
      [!] Usage: python """ + sys.argv[0] + """ <mode>
	      [-] Server: python """ + sys.argv[0] + """ server
	      [-] Client: python """ + sys.argv[0] + """ client

	""" + be

	# help for server portion of the appliation
	def shelp(self):
		print bh + """

    ~ """ + va + ": " + vv + " - " + vauth + """
    [*] ----------------------------------------------------------------------------
    [*] Egress Filter verification and Covert Channel testing suite
    [*] Use this for a server listening on the internet.
    [*] For further help try the following arguments:
      [!] Usage: python """ + sys.argv[0] + """ <mode> <protocol> <server_port> <tls enabled>
	      [-] Example: python """ + sys.argv[0] + """ server tcp 10000 no
	      [-] Example: python """ + sys.argv[0] + """ server udp 10000 no
	      [-] Example: python """ + sys.argv[0] + """ server both 10000 no

    """ + be

	# help for server TLS support
	def tlshelp(self):
		print bh + """

    ~ """ + va + ": " + vv + " - " + vauth + """
    [*] ----------------------------------------------------------------------------
    [*] Egress Filter verification and Covert Channel testing suite
    [*] Use this for a TLS server listening on the internet.
    [*] For further help try the following arguments:
      [!] Usage: python """ + sys.argv[0] + """ <mode> <protocol> <server_port> <tls enabled>
	      [-] Example: python """ + sys.argv[0] + """ server tcp 10000 yes

    """ + be

	def chelp(self):
		print bh + """
    
    ~ """ + va + ": " + vv + " - " + vauth + """
    [*] ----------------------------------------------------------------------------
    [*] Egress Filter verification and Covert Channel testing suite
    [*] Client portion of this application to be used with listening server
    [*] For further help try the following arguments::
      [!] Usage: python """ + sys.argv[0] + """ <mode> <config> <tls>
	      [-] Example: python """ + sys.argv[0] + """ client ./efb.conf no
    """ + be

	def thelp(self):
		print bh + """
    
    ~ """ + va + ": " + vv + " - " + vauth + """
    [*] ----------------------------------------------------------------------------
    [*] Finds open ports inside a network or something...
    [*] Client portion of this application to be used with TLS listening server
    [*] For further help try the following arguments:
      [!] Usage: python """ + sys.argv[0] + """ <mode> <config> <tls>
	      [-] Example: python """ + sys.argv[0] + """ client ./efb.conf yes
    """ + be

	def confh(self):
		print bh + """
    # This is an example configuration file, modify as needed!
    # SectionOne is for main processes and settings

    [SectionOne]
    target: 127.0.0.1
    range: 1-65535       
    random: True
    protocol: TCP
    consultant: YOURNAME
    location: YOURLOCATION

    # SectionTwo is for sleep settings; the sleep var takes one of the following: 'random' or 'static'

    [SectionTwo]
    sleep: static
    nappy: 0   
    dwell: 0.01

    # SectionThree is for suppressing connection error messages and logging of output
     
    [SectionThree]
    suppress: no
    logging: yes
    logtype: xml
    """ + be