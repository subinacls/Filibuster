#!/usr/bin/env python
# encoding: utf-8
"""
module author: subinacls

DLP testing module

"""

import random
import csv

name= []
with open('./dlp/datawarehouse/amm_name.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        name.append(row)


print " ".join(map(str,random.choice(name)))

city= []
with open('./dlp/datawarehouse/cityst.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        city.append(row)


print " ".join(map(str,random.choice(city)))

bday= []
with open('./dlp/datawarehouse/bday.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        bday.append(row)


print " ".join(map(str,random.choice(bday)))
bloodtype= []
with open('./dlp/datawarehouse/bloodtype.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        bloodtype.append(row)


print " ".join(map(str,random.choice(bloodtype)))
car= []
with open('./dlp/datawarehouse/car.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        car.append(row)


print " ".join(map(str,random.choice(car)))
guid= []
with open('./dlp/datawarehouse/guid.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        guid.append(row)


print " ".join(map(str,random.choice(guid)))
latlong= []
with open('./dlp/datawarehouse/latlong.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        latlong.append(row)


print " ".join(map(str,random.choice(latlong)))
maiden= []
with open('./dlp/datawarehouse/maiden.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        maiden.append(row)


print " ".join(map(str,random.choice(maiden)))
pci= []
with open('./dlp/datawarehouse/pci.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        pci.append(row)


print " ".join(map(str,random.choice(pci)))
ssn= []
with open('./dlp/datawarehouse/ssn.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        ssn.append(row)


print " ".join(map(str,random.choice(ssn)))
stname= []
with open('./dlp/datawarehouse/streetnames.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        stname.append(row)


print " ".join(map(str,random.choice(stname)))
unamepass= []
with open('./dlp/datawarehouse/unamepass.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        unamepass.append(row)


print " ".join(map(str,random.choice(unamepass)))
upstrack= []
with open('./dlp/datawarehouse/upstrack.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        upstrack.append(row)


print " ".join(map(str,random.choice(upstrack)))
website= []
with open('./dlp/datawarehouse/website.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        website.append(row)


print " ".join(map(str,random.choice(website)))
weightheight= []
with open('./dlp/datawarehouse/weightheight.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        weightheight.append(row)


print " ".join(map(str,random.choice(weightheight)))
stpre = []
with open('./dlp/datawarehouse/stprefix.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        stpre.append(row)


print " ".join(map(str,random.choice(stpre)))

n = random.choice(name)
print "\n\n\n" + \
      "".join(map(str,n)[0])+"."+"".join(map(str,n)[2]) + "@" + \
      "".join(map(str,random.choice(website))) + "\n" + \
      " ".join(map(str,n)) + "\n" + \
      " ".join(map(str,random.choice(stname))) + "\n" + \
      " ".join(map(str,random.choice(city))) + "\n" + \
      " ".join(map(str,random.choice(bday))) + "\n" + \
      " ".join(map(str,random.choice(weightheight))) + "\n" + \
      " ".join(map(str,random.choice(upstrack))) + "\n" + \
      " ".join(map(str,random.choice(website))) + "\n" + \
      " ".join(map(str,random.choice(unamepass))) + "\n" + \
      " ".join(map(str,random.choice(maiden))) + "\n" + \
      " ".join(map(str,random.choice(pci))) + "\n" + \
	  " ".join(map(str,random.choice(ssn))) + "\n\n\n"