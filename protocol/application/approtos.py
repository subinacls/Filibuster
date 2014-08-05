#!/usr/bin/env python
# encoding: utf-8
#
# module author: subinacls
#




protolist = {
	"http": ["GET", "/this/should/never/be/real_anywhere/Filterbuster.html"],
    "ftp" : ["User: Filterbuster","Pass: Filterbuster"],
    "telnet" : []
}


"""
conn = httplib.HTTPConnection("127.0.0.1","888")
conn.request("GET","/this/should/never/be/real_anywhere/Filterbuster.html")
conn.close()
"""
""" FTP
from ftplib import FTP
ftp = FTP('ftp.debian.org')     # connect to host, default port
ftp.login()
"""
