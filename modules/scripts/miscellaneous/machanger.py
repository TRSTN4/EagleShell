#!/usr/bin/python3

from assets.banners import machanger_banner
from assets.designs import *
from assets.properties import clear_screen

import os
import subprocess
import netifaces
import re


def machanger_main():

    def configuration():
        try:
            global interface_set
            global mac_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(machanger_banner)
            print(line)
            print('')
            print(author)
            print('Interface:')
            ips()
            print('')
            while True:
                interface_set = input('\u001b[33mINTERFACE \u001b[37m> ').lower()
                mac_set = input('\u001b[33mNEW MAC \u001b[37m> ').lower()
                change_mac()
        except KeyboardInterrupt:
            exit_shell()

    def ips():
        x = netifaces.interfaces()

        for i in x:
            if i == 'wlan0' or i == 'wlan1' or i == 'wlan2' or i == 'wlan3' or i == 'mon0' or i == 'mon1' or i == 'mon2' or i == 'mon3' or i == 'wlp5s0' or i == 'wlp5s1' or i == 'wlp5s2' or i == 'wlp5s3':
                print('\n\t[+] Available Interface: ' + i)
            elif i != 'lo' or i != 'eth0' or i != 'eth1' or i != 'eth2' or i != 'eth3' or i != 'tun0' or i != 'tun1' or i != 'tun2' or i != 'tun3':
                print('\n\t[-] Unavailable Interface: ' + i)

    def change_mac():
        print("[+] Changing MAC address for " + interface_set + " to " + mac_set)
        subprocess.call(["ifconfig", interface_set, "down"])
        subprocess.call(["ifconfig", interface_set, "hw", "ether", mac_set])
        subprocess.call(["ifconfig", interface_set, "up"])
        get_current_mac()

    def get_current_mac():
        ifconfig_result = subprocess.check_output(["ifconfig", interface_set])
        mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
        if mac_address_search_result:
            return mac_address_search_result.group(0)
        else:
            print("[-] Could not read MAC address.")

#    print("Current MAC = " + str(current_mac))

#    change_mac(options.interface, options.new_mac)

#    current_mac = get_current_mac(options.interface)
#    if current_mac == options.new_mac:
#        print("[+] MAC address was successfully changed to " + current_mac)
#    else:
#        print("[-] MAC address did not get changed.")

    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


machanger_main()
