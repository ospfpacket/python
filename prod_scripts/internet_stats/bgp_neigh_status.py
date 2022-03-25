from netmiko import ConnectHandler
from getpass import getpass
from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

username = input("Username: ")
password = getpass()

rtr = open("devices.txt")

for device in rtr:
    device = {
        'device_type': 'cisco_ios',
        'host':   device,
        'username': username,
        'password': password,
    }

    try:
        net_connect = ConnectHandler(**device)
    except (AuthenticationException):
        print("Authentication failure: " + device['host'])
        continue
    except (NetmikoTimeoutException):
        print("Timeout to device: " + device['host'])
        continue
    except (EOFError):
        print("End of file while attempting device " + device['host'])
        continue
    except (SSHException):
        print("SSH Issue. Are you sure SSH is enabled? " + device['host'])
        continue
    except Exception as unknown_error:
        print("Some other error: " + device['host'])
        continue

    output = net_connect.send_command('show ip bgp summ | inc AS_Num')                      # Insert AS Numbers Here for parsing config (xxx|xxx|xxx)
    print(device['host'] + ": BGP Neighborships", file=open('bgp_neighbors.txt', 'a'))
    print(output, file=open('bgp_neighbors.txt', 'a'))
    print("_" * 60, file=open('bgp_neighbors.txt', 'a'))