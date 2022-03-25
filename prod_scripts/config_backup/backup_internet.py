# Import dependencies
from netmiko import ConnectHandler
import getpass

# Define variables
f = open ('my_devices.txt')
username = input("Input Username:\n")
password = getpass.getpass()

# Loop through my_devices.txt inventory and save running_config to file in backups directory
for hostname in f:
    hostname=hostname.strip()
    device = {
        'device_type': 'cisco_ios',
        'host':   hostname,
        'username': username,
        'password': password,
    }
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command('terminal length 0')
    output = net_connect.send_command('show run')
    print(output, file=open("backups/" + hostname + "_running_config.txt", 'w'))

