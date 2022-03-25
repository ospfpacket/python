from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException

    try:
        ###Command to Run for Exception Checking###
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