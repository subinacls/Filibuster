

import base64
import shutil
import time
import json
import __builtin__
from exceptcatcher import contamloghandler as clh

__builtin__.contback = {}
__builtin__.contjson = {}

class contaminlog():

	def __init__(self):
		pass # nothing to see here

	def jcom_read(self):
		try:
			with open('Contaminated_log-'+str(date)+'.json', 'r') as fr: # open a file as named variable
				__builtin__.contjson = json.loads(f.read()) # load json data to built in variable
				fr.close()
		except Exception as jreadfail: # catch all
			if contback != "": # really dirty hack to keep a log ...
				contjson = json.loads(json.dumps(contback)) #, indent=4)) # modify to add tabs to logfile
			else:
				contjson = json.loads(json.dumps({})) #, indent=4)) # modify to add tabs to logfile
			clh().jsonreadfail(jreadfail)
			pass

	def jcom_write(self):
		try:
			with open('Contaminated_log-'+str(date)+'.json', 'w') as fw: # open a file as named variable
				__builtin__.fw = fw
				fw.write(json.dumps(contjson))#, indent=4)) # dumps data to file with indent 4 spaces
				fw.close()
			if len(contjson) != 0:
				shutil.copyfile('Contaminated_log-'+str(date)+'.json', 'Contaminated_log-'+str(date)+'.back')
		except Exception as jwritefail: # catch all
			clh().jsonrwritefail(jwritefail)
			pass

	def jcom_keeper(self, ipaddr, proto, port, data):
		self.jcom_read()
		try:
			bdata = base64.b64encode(data)
			sdata = str(data).encode('hex')
			hdata = "\\x"+'\\x'.join(a+b for a,b in zip(sdata[::2], sdata[1::2]))
			if str(ipaddr) not in contjson.keys():
				contjson[str(ipaddr)] = {}
			if str(proto) not in contjson[str(ipaddr)].keys():
				contjson[str(ipaddr)][str(proto)] = {}

			if str(port) not in contjson[str(ipaddr)][str(proto)].keys():
				contjson[str(ipaddr)][str(proto)][str(port)] = {}

			if str(bdata) not in contjson[str(ipaddr)][str(proto)][str(port)].keys():
				contjson[str(ipaddr)][str(proto)][str(port)][str(bdata)] = {}

				contjson[str(ipaddr)][str(proto)][str(port)][str(bdata)]["raw"] = """+str(data)+"""
				contjson[str(ipaddr)][str(proto)][str(port)][str(bdata)]["hex"] = str(hdata)
				contjson[str(ipaddr)][str(proto)][str(port)][str(bdata)]["count"] = 1
			else:
				cjc = contjson[str(ipaddr)][str(proto)][str(port)][str(bdata)]["count"]
				cjc = int(cjc) + 1
				contjson[str(ipaddr)][str(proto)][str(port)][str(bdata)]["count"] = str(cjc)
		except Exception as jkeeperfail: # catch all
			clh().jsonrkeepfail(jkeeperfail)
			pass # keep on keeping no
		self.jcom_write()