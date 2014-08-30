#!/usr/bin/python2
# encoding: utf-8
#
# module author: subinacls
#

"""
this file is used to produce the XML log
"""

import datetime


class xmllogfilegen(object):

	def __init__(self):
		pass

	def xmllog(self):
		xmloutput = """<consultant>
\t<name>""" + str(consultant) + """</name>
</consultant>
<location>
\t<address>""" + str(location) + """</address>
</location>
<date>
\t<current_date>""" + str(datetime.datetime.now()).strip(".") + """</current_date>
</date>
<ipaddress>
\t<target_ip>""" + str(ipaddr) + """</target_ip>
</ipaddress>
<target_port>
\t<service_port>""" + str(proto) + """/""" + str(base_port) + """</service_port>
</target_port>
<status>
\t<condition>""" + str(state) + """</connection>
</status>
"""
		with open(str(consultant) + '-' + str(location) + '-' + str(datetime.datetime.now()).split(" ")[0] +
				          '.xml', 'a', buffering=0) as f:
			f.write(xmloutput)
			f.close()