# Import dependencies
from netmiko import ConnectHandler
import getpass

# Define variables (input for 3 fields used in device dict)
hostname = input("Input Device Hostname:\n")
username = input("Input Username:\n")
password = getpass.getpass()
device = {
    'device_type': 'cisco_ios',
    'host':   hostname,
    'username': username,
    'password': password,
}

# Run net_connect, push commands, and write to file in backups directory
net_connect = ConnectHandler(**device)
output = net_connect.send_command('terminal length 0')
output = net_connect.send_command('show run')
print(output, file=open("backups/" + hostname + "_running_config.txt", 'w'))