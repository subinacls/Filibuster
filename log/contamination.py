__author__ = 'root'


import base64
import json
import __builtin__

class contaminlog():

	def __init__(self):
		pass # nothing to see here

	def jcom_read(self):
		try:
			with open('Contaminated_log-'+str(date)+'.json', 'r') as f: # open a file as named variable
				__builtin__.contjson = json.loads(f.read()) # load json data to built in variable
				f.close()
		except Exception as jreadfail: # catch all
			#print jreadfail, 'Can not read file: Contaminated_log-'+str(date)+'.json'
			__builtin__.contjson = json.loads(json.dumps({})) #, indent=4))
			pass

	def jcom_write(self):
		try:
			with open('Contaminated_log-'+str(date)+'.json', 'w') as f: # open a file as named variable
				f.write(json.dumps(contjson, indent=4)) # dumps data to file with indent 4 spaces
		except Exception as jwritefail: # catch all
			print jwritefail, "something failed in writing the file: Contaminated_log-"+str(date)+".json"
			pass

	def jcom_keeper(self, ipaddr, proto, port, data):
		self.jcom_read()
		time.sleep(0.01)
		try:
			data = base64.b64encode(data)
		except Exception as e1:
			print e1
		try:
			if str(ipaddr) not in contjson.keys():
				contjson[str(ipaddr)] = {}
		except Exception as e2: # catch all
			print e2
		try:
			if str(proto) not in contjson[str(ipaddr)].keys():
				contjson[str(ipaddr)][str(proto)] = {}
		except Exception as e3:
			print e3
		try:
			if str(port) not in contjson[str(ipaddr)][str([proto)].keys():
				contjson[str(ipaddr)][str(proto)][str(port)] = {}
		except Exception as e4:
			print e4
		try:
			if str(data) not in contjson[str(ipaddr)][str(proto)][str(port)].keys():
				try:
					contjson[str(ipaddr)][str(proto)][str(str(port)][str(data)] = []
				except Exception as e:
					print e, "test1"
				try:
					contjson[str(ipaddr)][str(proto)][str(port)][str(data)].append(str(1))
				except Exception as e:
					print e, "test2"
			else:
				try:
					cjc = contjson[str(ipaddr)][str(proto)][str(port)][str(data)][0]
				except Exception as e:
					print e, "test3"
				try:
					cjc = int(cjc) + 1
				except Exception as e:
					print e, "test4"
				try:
					contjson[str(ipaddr)][str(proto)][str(port)][str(data)][0] = str(cjc)
				except Exception as e:
					print e, "test5"
			pass # keep on moving
		except Exception as jkeeperfail: # catch all
			print jkeeperfail, "the portnumber form the client "
			#pass # keep on keeping no
		self.jcom_write()