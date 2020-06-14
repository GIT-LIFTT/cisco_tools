from netmiko import Netmiko
import time

# define hosts in the form of dictionarys as required by netmiko
FW01 = {
'device_type': 'cisco_asa',
'host': '200.100.100.8',
'username': 'cisco',
'password': 'cisco',
 }

IOSL2_1 = {
'device_type': 'cisco_ios',
'host': '200.100.100.1',
'username': 'admin',
'password': 'admin',
 }

IOSL2_2 = {
'device_type': 'cisco_ios',
'host': '200.100.100.7',
'username': 'admin',
'password': 'admin',
 }

FW01 = {
'device_type': 'cisco_asa',
'host': '200.100.100.8',
'username': 'cisco',
'password': 'cisco',
 }

NXOS05 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.6',
'username': 'admin',
'password': 'admin',
 }

NXOS06 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.5',
'username': 'admin',
'password': 'admin',
 }

NXOS07 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.3',
'username': 'admin',
'password': 'admin',
 }

NXOS08 = {
'device_type': 'cisco_nxos',
'host': '200.100.100.4',
'username': 'admin',
'password': 'admin',
 }

CORE_ISP = {
'device_type': 'cisco_ios',
'host': '200.100.100.4',
'username': 'admin',
'password': 'admin',
 }

FW02 = {
'device_type': 'cisco_asa',
'host': '200.100.100.9',
'username': 'cisco',
'password': 'cisco',
 }
# put the dictionarys into a list
host_list = [FW01,FW02,NXOS05,NXOS06,NXOS07,NXOS08,CORE_ISP,IOSL2_1,IOSL2_2]

# for each dictionary within the list
for i in host_list:
 try:
    #try to conenct via ssh
    net_connect = Netmiko(**i)
    print("ssh conencted to "+i['host'])
 except:
    #if the connection fails print connect failed
    print ("ssh failed to "+i['host'])