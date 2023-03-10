import netifaces
import ipaddress

#.AF_LINK = mac, key 18pip i
#.AF_INET = broadcast, netmask, ip
#.AF_INET6 = ipv6

interfacelist = ['lo0', 'gif0', 'stf0', 'ap1', 'en0', 'awdl0', 'llw0', 'en1', 'en2', 'en3', 'en4', 'bridge0', 'utun0', 'utun1', 'utun2', 'utun3', 'utun4', 'en5', 'utun5', 'utun6']
def get_interfaces():
	inter = netifaces.interfaces()
	print(inter)
	return inter

def get_mac(interface: str):
	try:
		mac = netifaces.ifaddresses(interface)[netifaces.AF_LINK]
		print("The mac address of "+interface+" is: "+str(mac))
		return mac
	except(KeyError):
		print("Does not have Mac Addr.")

def get_ips(interface: str):
	#look for key 'addr', this will be address in the 
	ip_dict = {}
	try:
		ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET]
		ipv4 = ipv4[0]['addr']
		print(ipv4)
		ip_dict.update({'V4':ipv4})
	except:
		print(interface+" does not have ipv4.")

	try:
		ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6]
		ipv6 = ipv6[0]['addr']
		print(ipv6)
		ip_dict.update({'V6':ipv6})
	except:
		print(interface+" does not have ipv6.")
	
	print(ip_dict)
	return ip_dict

def get_netmask(interface: str):
	#look for key 'addr', this will be address in the 
	nm_dict = {}
	try:
		ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET]
		ipv4 = ipv4[0]['netmask']
		print(ipv4)
		ip_dict.update({'V4':ipv4})
	except:
		print(interface+" does not have mask.")

	try:
		ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6]
		ipv6 = ipv6[0]['netmask']
		print(ipv6)
		ip_dict.update({'V6':ipv6})
	except:
		print(interface+" does not have mask.")
	
	print(nm_dict)
	return nm_dict

def get_network(interface: str):
	#look for key 'addr', this will be address in the 
	net_dict = {}
	try:
		ipv4 = netifaces.ifaddresses(interface)[netifaces.AF_INET]
		ipv4 = ipv4[0]['broadcast']
		print(ipv4)
		ip_dict.update({'V4':ipv4})
	except:
		print(interface+" does not have network.")

	try:
		ipv6 = netifaces.ifaddresses(interface)[netifaces.AF_INET6]
		ipv6 = ipv6[0]['broadcast']
		print(ipv6)
		ip_dict.update({'V6':ipv6})
	except:
		print(interface+" does not have network.")
	
	print(net_dict)
	return
interface = str(get_interfaces())
for i in interfacelist:

	get_network(i)



'''
What is the IP configuration for your computer (i.e. what is the output of the shell command used for this purpose)? 
['lo0', 'gif0', 'stf0', 'ap1', 'en0', 'awdl0', 'llw0', 'en1', 'en2', 'en3', 'en4', 'bridge0', 'utun0', 'utun1', 'utun2', 'utun3', 'utun4', 'en5', 'utun5', 'utun6']

What are the MAC addresses for these interfaces? Write a function that uses netifaces to return the MAC address for a given interface:
‘lo0’ has no MAC
‘gif0’ has no mac
‘stf0’ has no mac
‘ap1’ =’addr': '3e:22:fb:c5:fa:33'
‘en0’ = 'addr': '3c:22:fb:c5:fa:33'
‘awdl0’ = 'addr': '06:65:93:a9:f1:1b'
llw0 is: [{'addr': '06:65:93:a9:f1:1b'}]
en1 is: [{'addr': '82:ba:89:64:c0:01'}]
en2 is: [{'addr': '82:ba:89:64:c0:00'
en3 is: [{'addr': '82:ba:89:64:c0:05'}
en4 is: [{'addr': '82:ba:89:64:c0:04'}]
The mac address of bridge0 is: [{'addr': '82:ba:89:64:c0:01'}]
'utun0', 'utun1', 'utun2', 'utun3', 'utun4', 'en5', 'utun5', 'utun6' do not have mac addresses

What are the IPv4 and IPv6 addresses associated with these interfaces?

'lo0',
127.0.0.1
::1
{'V4': '127.0.0.1', 'V6': '::1'}
 'gif0',
n/a
 'stf0',
stf0
 'ap1',
n/a
 'en0', 
192.168.187.114
fe80::1c12:3dad:d5b7:bf7b%en0
{'V4': '192.168.187.114', 'V6': 'fe80::1c12:3dad:d5b7:bf7b%en0'}
'awdl0',
awdl0 does not have ipv4.
fe80::38b0:5cff:fe4a:400d%awdl0
{'V6': 'fe80::38b0:5cff:fe4a:400d%awdl0'}
 'llw0', 
llw0 does not have ipv4.
fe80::38b0:5cff:fe4a:400d%llw0
{'V6': 'fe80::38b0:5cff:fe4a:400d%llw0'}
'en1'
n/a
, 'en2'
n/a
, 'en3', 
n/a
'en4',
n/a
 'bridge0',
n/a
 'utun0',
utun0 does not have ipv4.
fe80::b5ec:d82:3ddb:3c55%utun0
{'V6': 'fe80::b5ec:d82:3ddb:3c55%utun0'}
 'utun1',
utun1 does not have ipv4.
fe80::e352:deac:9806:da2%utun1
{'V6': 'fe80::e352:deac:9806:da2%utun1'}
 'utun2',
utun2 does not have ipv4.
fe80::ce81:b1c:bd2c:69e%utun2
{'V6': 'fe80::ce81:b1c:bd2c:69e%utun2'}
 'utun3',
utun3 does not have ipv4.
fe80::28b:21d1:da7a:e7f8%utun3
{'V6': 'fe80::28b:21d1:da7a:e7f8%utun3'}
 'utun4'
, 'en5',
en5 does not have ipv4.
fe80::aede:48ff:fe00:1122%en5
{'V6': 'fe80::aede:48ff:fe00:1122%en5'}
 'utun5', 
'utun6'
What are the IPv4 and IPv6 netmasks of each of these IP subnets? Write a function that users netifaces to return both the IPv4Address Links to an external site. and IPv6Address Links to an external site. object representation of the netmasks for the given interface as a dictionary.
'lo0' =255.0.0.0
lo0 does not have mask.
ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
lo0 does not have mask.
255.0.0.0
lo0 does not have mask.
ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
lo0 does not have mask.
{}
gif0 does not have mask.
gif0 does not have mask.
{}
stf0 does not have mask.
stf0 does not have mask.
{}
ap1 does not have mask.
ap1 does not have mask.
{}
255.255.240.0
en0 does not have mask.
ffff:ffff:ffff:ffff::/64
en0 does not have mask.
{}
awdl0 does not have mask.
ffff:ffff:ffff:ffff::/64
awdl0 does not have mask.
{}
llw0 does not have mask.
ffff:ffff:ffff:ffff::/64
llw0 does not have mask.
{}
en1 does not have mask.
en1 does not have mask.
{}
en2 does not have mask.
en2 does not have mask.
{}
en3 does not have mask.
en3 does not have mask.
{}
en4 does not have mask.
en4 does not have mask.
{}
bridge0 does not have mask.
bridge0 does not have mask.
{}
utun0 does not have mask.
ffff:ffff:ffff:ffff::/64
utun0 does not have mask.
{}
utun1 does not have mask.
ffff:ffff:ffff:ffff::/64
utun1 does not have mask.
{}
utun2 does not have mask.
ffff:ffff:ffff:ffff::/64
utun2 does not have mask.
{}
utun3 does not have mask.
ffff:ffff:ffff:ffff::/64
utun3 does not have mask.
{}
utun4 does not have mask.
ffff:ffff:ffff:ffff::/64
utun4 does not have mask.
{}
en5 does not have mask.
ffff:ffff:ffff:ffff::/64
en5 does not have mask.
{}
utun5 does not have mask.
ffff:ffff:ffff:ffff::/64
utun5 does not have mask.
{}
utun6 does not have mask.
ffff:ffff:ffff:ffff::/64
utun6 does not have mask.
{}


What are the IPv4 and IPv6 networks associated with each of these addresses? 
lo0 does not have network.
lo0 does not have network.
{}
gif0 does not have network.
gif0 does not have network.
{}
stf0 does not have network.
stf0 does not have network.
{}
ap1 does not have network.
ap1 does not have network.
{}
192.168.191.255
en0 does not have network.
en0 does not have network.
{}
awdl0 does not have network.
awdl0 does not have network.
{}
llw0 does not have network.
llw0 does not have network.
{}
en1 does not have network.
en1 does not have network.
{}
en2 does not have network.
en2 does not have network.
{}
en3 does not have network.
en3 does not have network.
{}
en4 does not have network.
en4 does not have network.
{}
bridge0 does not have network.
bridge0 does not have network.
{}
utun0 does not have network.
utun0 does not have network.
{}
utun1 does not have network.
utun1 does not have network.
{}
utun2 does not have network.
utun2 does not have network.
{}
utun3 does not have network.
utun3 does not have network.
{}
utun4 does not have network.
utun4 does not have network.
{}
en5 does not have network.
en5 does not have network.
{}
utun5 does not have network.
utun5 does not have network.
{}
utun6 does not have network.
utun6 does not have network.
{}
'''