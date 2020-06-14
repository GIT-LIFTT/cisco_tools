from netmiko import Netmiko
import time

# define hosts in the form of dictionarys as required by netmiko
NXOS9 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.8',
'username': 'admin',
'password': 'admin',
 }

NXOS10 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.6',
'username': 'admin',
'password': 'admin',
 }

NXOS11 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.5',
'username': 'admin',
'password': 'admin',
 }

NXOS12 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.3',
'username': 'admin',
'password': 'admin',
 }

NXOS13 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.4',
'username': 'admin',
'password': 'admin',
 }

NXOS14 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.7',
'username': 'admin',
'password': 'admin',
 }
# put the dictionarys into a list 
host_list = [NXOS9,NXOS10,NXOS11,NXOS12,NXOS13,NXOS14]

# for each dictionary within the list
for i in host_list:
 try:
    #try to conenct via ssh
    net_connect = Netmiko(**i)
    print("ssh conencted to "+i['host'])
 except:
    #if the connection fails print connect failed
    print ("ssh failed to "+i['host'])