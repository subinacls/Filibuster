# encoding: utf-8
#!/usr/bin/env python
'''
this file is used to produce the XML log
'''

class xmllogfilegen:

	def __init__(self):
		pass

	def xmllog(self,proto, ipaddr, consultant, location, ldate, base_port, dft,state):
		xmloutput = """<consultant>
\t<name>"""+str(consultant)+"""</name>
</consultant>
<location>
\t<address>"""+str(location)+"""</address>
</location>
<date>
\t<current_date>"""+str(dft.strip())+"""</current_date>
</date>
<ipaddress>
\t<target_ip>"""+str(ipaddr)+"""</target_ip>
</ipaddress>
<target_port>
\t<service_port>"""+str(proto)+"""/"""+str(base_port)+"""</service_port>
</target_port>
<status>
\t<condition>"""+str(state)+"""</connection>
</status>
"""
		with open(str(consultant)+'-'+str(location)+'-'+str(ldate)+'.xml', 'a', buffering=0) as f:
			f.write(xmloutput)
			f.close()