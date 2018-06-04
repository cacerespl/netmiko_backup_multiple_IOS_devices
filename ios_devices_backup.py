#!/usr/bin/python

from netmiko import ConnectHandler
from datetime import datetime
import os

username = os.environ['USERNAME']   # environment variable
password = os.environ['PASSWORD']   # environment variable
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def backup(dictionary):
    """
    This function creates a backup of Cisco IOS devices and create a file in a directory defined.
    It will create one file for each device.
    The function accepts a dictionary of devices as argument
    
    """
    for i in dictionary:
        ip = dictionary[i]
        fname = '/home/user/ios_backups/'+date+'-'+i+'.txt'   # Path to save the file
        device = ConnectHandler(device_type='cisco_ios', ip = ip, username=username, password = password)
        file_test = open(fname, 'w')
        output = device.send_command('show run')
        file_test.write(output)
        file_test.close()

ios_devices = {'SW1': '172.18.9.233', 'SW2':'10.20.20.34', 'SW3':'192.168.45.200'}   # Example of Devices

backup(ios_devices)

