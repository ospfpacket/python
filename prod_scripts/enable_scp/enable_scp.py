from netmiko import ConnectHandler
import getpass

username = input("Username: ")
password = getpass.getpass()
device_list = open("devices_file.txt")
scp_check = ["scp server"]

for devices in device_list:
    devices = devices.strip()
    print ("Connecting to device " + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'host': ip_address_of_device,
        'username': username,
        'password': password,
        'fast_cli': False
    }

    net_connect = ConnectHandler(**ios_device)
    for scp_server in scp_check:
        print ('Checking for SCP Server readiness')
        output_version = net_connect.send_command("show run | inc scp server")
        int_version = 0
        int_version = output_version.find(scp_server)
        if int_version > 0:
            break
        else:
           print ("Did not find " + scp_server)
           scp_server = "Not Present"
    
    if scp_server == 'scp server':
        print ("Device is ready for SCP")
    elif scp_server == "Not Present":
        print ("Running SCP command")
        output = net_connect.send_config_set("ip scp server enable")
        print(output)
        print ("Device is now SCP ready")
        print ("Saving Configuration to Start")
        output = net_connect.save_config()
        