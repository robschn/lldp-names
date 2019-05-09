#!/usr/bin/env Python

#explain script
print('\nThis script will find the names of the LLDP enable devices on your switch.')

#ask for IP
userIP = input ('\nPlease enter the IP of the switch: ')

#ask for username
username = input ('\nUsername: ')

#connect to switch
while True:
	try:
		myDevice = {
		'host': userIP,
		'username': username,
		'password': password,
		'device_type': 'cisco_ios',
		}
		print ('Logging in now...')
		# Connects to "myDevice"
		net_connect = Netmiko(**myDevice)
		net_connect.enable()
		break
	except:
		print ('Login failed. Please try again.')
		continue

#issue sh lldp nei
data = net_connect.send_command('show lldp nei')

#split the LLDP output
data = f.read().split()

#create output file for the print
f = open('output.txt', 'w')

#print every 5th line and seperate but a new line, then output to file
print("\n".join(data[::5]), file=f)
