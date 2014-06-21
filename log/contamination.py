__author__ = 'root'



import json
import __builtin__

class contaminlog():

	def __init__(self):
		pass # nothing to see here

	def jcom_read(self):
		try:
			with open('Contaminated_log-'+str(date)+'.json', 'r', buffering=0) as f: # open a file as named variable
				__builtin__.contjson = json.loads(f.read()) # load json data to built in variable
		except Exception as jreadfail: # catch all
			#print jreadfail, 'Can not read file: Contaminated_log-'+str(date)+'.json'
			__builtin__.contjson = json.loads(json.dumps({})) #, indent=4))
			pass

	def jcom_write(self):
		try:
			with open('Contaminated_log-'+str(date)+'.json', 'w', buffering=0) as f: # open a file as named variable
				f.write(json.dumps(contjson)) #, indent=4)) # dumps data to file with indent 4 spaces
		except Exception as jwritefail: # catch all
			print jwritefail, "something failed in writing the file: Contaminated_log-"+str(date)+".json"
			pass

	def jcom_keeper(self,ipaddr,proto,port,data):
		try:
			if str(ipaddr) not in contjson.keys():
				contjson[ipaddr] = {}
			if str(proto) not in contjson[ipaddr].keys():
				contjson[ipaddr][proto] = {}
			if str(port) not in contjson[ipaddr][proto].keys():
				contjson[ipaddr][proto][port] = {}
			if str(data) not in contjson[ipaddr][proto][port].keys():
				contjson[ipaddr][proto][port][data] = []
				contjson[ipaddr][proto][port][data].append(1)
			else:
				cjc = contjson[ipaddr][proto][port][data][0]
				cjc = int(cjc) + 1
				contjson[ipaddr][proto][port][data][0] = str(cjc)
			pass # keep on moving
		except Exception as jkeeperfail: # catch all
			print jkeeperfail, "something happened in contamination().keeper() ..."
			pass # keep on keeping no