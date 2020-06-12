from netmiko import Netmiko
import time


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

comamnds = ["show running-config"]
comamnds2 = ["show hostname"]


host_list = [NXOS9,NXOS10,NXOS11,NXOS12,NXOS13,NXOS14]
for i in host_list:
    net_connect = Netmiko(**i)
    print()
    print(net_connect.find_prompt())
    hostname = net_connect.send_command("show hostname")
    net_connect.send_command('terminal length 0')
    hostname = hostname.strip()
    print(hostname)
    #print(output)

    output = net_connect.send_config_set(comamnds)
    time.sleep(2)
    f = open(hostname+'.txt','w')
    f.write(output)
    f.close()
