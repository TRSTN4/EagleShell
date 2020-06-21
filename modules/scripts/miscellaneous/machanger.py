#!/usr/bin/python3

# Imports all the needed variables and packages
from assets.banners import machanger_banner
from assets.designs import *
from assets.properties import clear_screen
import subprocess
import netifaces
import os
import re


# Main function
def machanger_main():

    # Function that takes interface input
    def interface():
        try:
            global interface_set
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
                if interface_set == 'wlan0' or interface_set == 'wlan1' or interface_set == 'wlan2' or interface_set == 'wlan3' or interface_set == 'mon0' or interface_set == 'mon1' or interface_set == 'mon2' or interface_set == 'mon3' or interface_set == 'wlp5s0' or interface_set == 'wlp5s1' or interface_set == 'wlp5s2' or interface_set == 'wlp5s3' or interface_set == 'eth0' or interface_set == 'eth1' or interface_set == 'eth2' or interface_set == 'eth3':
                    mac()
                else:
                    print('\u001b[31m[-] Invalid Interface.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    # Function that takes mac input
    def mac():
        try:
            global mac_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(machanger_banner)
            print(line)
            print('')
            print(author)
            print('MAC Address:')
            print('')
            print('\tExample 1: 00:11:22:33:44:55')
            print('\tExample 2: 12:22:33:44:55:66')
            print('')
            while True:
                mac_set = input('\u001b[33mNEW MAC \u001b[37m> ').lower()
                print('')
                functions()
        except KeyboardInterrupt:
            exit_shell()

    # Function that shows all available and unavailable interfaces
    def ips():
        x = netifaces.interfaces()

        for i in x:
            if i == 'wlan0' or i == 'wlan1' or i == 'wlan2' or i == 'wlan3' or i == 'mon0' or i == 'mon1' or i == 'mon2' or i == 'mon3' or i == 'wlp5s0' or i == 'wlp5s1' or i == 'wlp5s2' or i == 'wlp5s3' or i == 'eth0' or i == 'eth1' or i == 'eth2' or i == 'eth3':
                print('\n\t[+] Available Interface: ' + i)
            elif i != 'lo' or i != 'tun0' or i != 'tun1' or i != 'tun2' or i != 'tun3':
                print('\n\t[-] Unavailable Interface: ' + i)

    # Function that changes MAC address
    def change_mac():
        os.system("ifconfig " + interface_set + " down" + " >/dev/null 2>&1")
        os.system("ifconfig " + interface_set + " hw " + " ether " + mac_set + " >/dev/null 2>&1")
        os.system("ifconfig " + interface_set + " up" + " >/dev/null 2>&1")

    # function that checks MAC address
    def get_current_mac():
        try:
            ifconfig_result = subprocess.check_output(["ifconfig", interface_set])
            mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
            if mac_address_search_result:
                return mac_address_search_result.group(0)
            else:
                pass
        except subprocess.CalledProcessError:
            print('print')

    # Function that executes other functions
    def functions():
        global worked_or_not
        global current_mac
        global color
        current_mac = get_current_mac()

        change_mac()

        current_mac = get_current_mac()
        if current_mac == mac_set:
            worked_or_not = "\u001b[32;1mMAC address was successfully changed."
            color = '\u001b[32;1m'
            result()
        else:
            worked_or_not = "\u001b[31mMAC address did not get changed."
            color = '\u001b[31m'
            result()

    # Function that displays result
    def result():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(machanger_banner)
            print(line)
            print('')
            print(author)
            print('Output:')
            print('')
            print('\tINTERFACE SET: ' + interface_set)
            print('')
            print('\tMAC SET: ' + mac_set)
            print('')
            print('\t---------------------------------------------')
            print('')
            print('\tRESULT: ' + worked_or_not + color + '\u001b[37m')
            print('')
            print('\tCURRENT MAC: ' + color + current_mac + color + '\u001b[37m')
            print('')
            print('\t1): New')
            print('\t2): Exit')
            print('')
            while True:
                eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if eagleshell_cmd == '1':
                    machanger_main()
                elif eagleshell_cmd == '2':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    # Function that exits
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    interface()


machanger_main()
