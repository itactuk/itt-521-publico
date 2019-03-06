# import netmiko
from netmiko import ConnectHandler
# from getpass import getpass
from time import ctime
password = '20091665'
centos_vm = {
    'device_type': 'linux',
    'host': '192.168.77.23',
    'username': 'root',
    'password': password
}
net_connect = ConnectHandler(**centos_vm)
net_connect.find_prompt()

net_connect.send_command("mkdir hola" + str(ctime()).replace(" ","_s"))
output = net_connect.send_command("ip addr")

print(output)
