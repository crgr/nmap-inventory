#!/usr/bin/env python

from urllib.request import urlopen
import xml.etree.ElementTree as ET
tree = ET.parse('arpscan.xml')
root = tree.getroot()
for hosts in root.findall('host'):
  mac = ''
  ip = ''
  vendor = ''
  for host in hosts.findall('address'):
    type = host.get('addrtype')
    if type == 'mac':
      mac = host.get('addr').lower()
      if 'vendor' in host.attrib:
        vendor = host.get('vendor')
      else:
        url = "https://macvendors.co/api/{}/pipe".format(mac)
        with urlopen(url) as res:
          vendor = res.read().decode('utf-8').split('|')[0]
    elif type == 'ipv4':
      ip = host.get('addr')
  print(mac, ip, vendor)