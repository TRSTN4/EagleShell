#!/usr/bin/python3

# MaChanger MAC Changer Script

# Imports all the needed variables and packages
from assets.banners import machanger_banner
from assets.designs import *
from assets.properties import clear_screen
import os
import netifaces


# The main function
def machanger_main():

    # Function where it takes user input
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

    # Function that displays all available and unavailable interfaces
    def ips():
        x = netifaces.interfaces()

        for i in x:
            if i == 'wlan0' or i == 'wlan1' or i == 'wlan2' or i == 'wlan3' or i == 'mon0' or i == 'mon1' or i == 'mon2' or i == 'mon3' or i == 'wlp5s0' or i == 'wlp5s1' or i == 'wlp5s2' or i == 'wlp5s3':
                print('\n\t[+] Available Interface: ' + i)
            elif i != 'lo' or i != 'eth0' or i != 'eth1' or i != 'eth2' or i != 'eth3' or i != 'tun0' or i != 'tun1' or i != 'tun2' or i != 'tun3':
                print('\n\t[-] Unavailable Interface: ' + i)

    # Function that will change the mac address
    def change_mac():
        print("[+] Changing MAC address for " + interface_set + " to " + mac_set + ' >/dev/null 2>&1')
        os.system("ifconfig " + interface_set + " down" + ' >/dev/null 2>&1')
        os.system("ifconfig " + interface_set + " hw " + " ether " + mac_set + ' >/dev/null 2>&1')
        os.system("ifconfig " + interface_set + " up" + ' >/dev/null 2>&1')

    # Function that
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


machanger_main()
