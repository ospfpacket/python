# Import dependencies
from netmiko import ConnectHandler
import getpass
import csv

username = input("Username: ")
password = getpass.getpass()
csv_reader = csv.DictReader(open("singlefile_csv.csv"))                # Replace CSV file with CSV File to import

row_check = "NDH-SUP2-E414.4A-S46.choa.org"                 # Set row_check to the first device in the CSV File

# Connect to device name in row_check
ios_device = {
    'device_type': 'cisco_ios',
    'host': row_check,
    'username': username,
    'password': password,
    }
net_connect = ConnectHandler(**ios_device)

# Loop through rows in CSV file 
for row in csv_reader:
    if row_check is row['Switch']:
        config_commands = ["interface " + row['Interface'], "no description " + row['AP Name'], "no shutdown"]
        output = net_connect.send_config_set(config_commands)
        print (output)
    else:
        row_check = row['Switch']
        ios_device = {
            'device_type': 'cisco_ios',
            'host': row['Switch'],
            'username': username,
            'password': password,
            }
        net_connect = ConnectHandler(**ios_device)
        config_commands = ["interface " + row['Interface'], "no description " + row['AP Name'], "no shutdown"]
        output = net_connect.send_config_set(config_commands)
        print (output)