#!/usr/bin/python3

# EagleEye Network Scanner Script

# Imports all needed variables and packages
from assets.banners import eagleye_banner
from assets.designs import *
from assets.properties import clear_screen
import os
import scapy.all as scapy
import netifaces


# Main function
def eagleye_main():

    # Function that takes user input
    def configuration():
        try:
            global network_ip_set
            global network_range_set
            global scan_result
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(eagleye_banner)
            print(line)
            print('')
            print(author)
            print('Network:')
            ips()
            print('')
            print('\tNetwork IP Example: 10.10.10.0')
            print('\tNetwork Range Example: 24')
            print('')
            while True:
                network_ip_set = input('\u001b[33mNETWORK IP \u001b[37m> ').lower()
                network_range_set = input('\u001b[33mNETWORK RANGE \u001b[37m> ').lower()
                scan_result = scan()
                print_result(scan_result)
        except KeyboardInterrupt:
            exit_shell()

    # Function that displays all interfaces and ips
    def ips():
        x = netifaces.interfaces()

        for i in x:
            if i != '':
                print('\n\tInterface: ' + i)

            try:
                ip = netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']

                print('\tIP addr: {0} '.format(ip))
            except KeyError:
                continue

    # Function that
    def scan():
        arp_request = scapy.ARP(pdst=network_ip_set + '/' + network_range_set)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        clients_list = []
        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(client_dict)
        return (clients_list)

    # Function that displays result
    def print_result(results_list):
        try:
            global network_ip_set
            global network_range_set
            global scan_result
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(eagleye_banner)
            print(line)
            print('')
            print(author)
            print('Result:')
            print('')
            print("\tIP\t\t\tMAC Address")
            print('\t-----------------------------------------')

            for client in results_list:
                if len(client["ip"]) < 8:
                    print('\t' + client["ip"] + "\t\t\t" + client["mac"])
                else:
                    print('\t' + client["ip"] + "\t\t" + client["mac"])
            print('')
            print('\t1): New')
            print('\t2): Exit')
            print('')
            while True:
                eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if eagleshell_cmd == '1':
                    eagleye_main()
                elif eagleshell_cmd == '2':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    # Function that exit
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


eagleye_main()
