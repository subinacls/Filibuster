# encoding: utf-8
#!/usr/bin/env python
from module_error_handling import modreporter as mp
import sys

class prettyerror:

	def __init__(self):
		pass

	def printerror(self, file, section, exceptionname):

		if str(diag).lower() in ["true","yes"]:
			print bf+"\n\t\t[?] Application failure in the "+str(mp().mod_inspect())+" module" \
					 "\n\t\t[-] Exception error name: " + str(section) +"" \
			         "\n\t\t\t[-] Exception reported: "+str(exceptionname)+"\n"+be
		if suppress != True:
			print bf+"\n\t\t[?] Error generated in ./"+str(file)+".py module" \
					 "\n\t\t[-] Exception error name: " + str(section) + "" \
		             "\n\t\t\t[-] File location: "+str(mp().mod_inspect()) + \
		             "\n\t\t\t[-] Exception reported: "+str(exceptionname)+"\n"+be
		sys.exit()