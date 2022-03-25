from napalm import get_network_driver
import getpass

#hostname = input("Device: ")
username = input("Username: ")
password = getpass.getpass()

device_list = ['ip1',
               'ip2']

driver = get_network_driver('ios')

for hostname in device_list:
    hostname = hostname.strip()
    print ("Connecting to " + hostname)
    device = driver(hostname, username, password)
    device.open()
    device.load_merge_candidate(filename='ACL1.cfg')
    diffs = device.compare_config()
    if len(diffs) > 0:
        print(diffs)
        device.commit_config()
    else:
        device.discard_config()

    device.close()
