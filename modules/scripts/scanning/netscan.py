#!/usr/bin/python3

from assets.banners import netscan_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import eagleshell_prefix, invalid_input_prefix, net_ip_prefix, net_range_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .scanning import Scanning
import os
import netifaces
import scapy.all as scapy


class NetScan:
    def __init__(self):
        self.configuration()
        self.scan_result = self.net_scanner()
        self.result(self.scan_result)

    def header(self):
        os.system(clear_screen)
        print(logo)
        print(netscan_banner)
        print(author)

    def configuration(self):
        try:
            self.header()
            print('Network:')
            self.netifaces()
            print('\n\t-------------------------\n')
            print('\tNetIP Example: 10.10.10.0')
            print('\tNetRange Example: 24\n')
            print('\tZ): Back')
            print('\tX): Exit\n')
            self.net_ip_set = input(net_ip_prefix).lower()
            if self.net_ip_set == 'z':
                Scanning()
            elif self.net_ip_set == 'x':
                Exit()
            self.net_range_set = input(net_range_prefix).lower()
            if self.net_range_set == 'z':
                Scanning()
            elif self.net_range_set == 'x':
                Exit()
        except KeyboardInterrupt:
            Exit()

    def netifaces(self):
        interfaces = netifaces.interfaces()
        for x in interfaces:
            if x != '':
                print('\n\tInterface: ' + x)
            try:
                ip = netifaces.ifaddresses(x)[netifaces.AF_INET][0]['addr']
                print('\tIP addr: {0} '.format(ip))
            except KeyError:
                continue

    def net_scanner(self):
        arp_request = scapy.ARP(pdst=self.net_ip_set + '/' + self.net_range_set)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        clients_list = []
        for element in answered_list:
            client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            clients_list.append(client_dict)
        return clients_list

    def result(self, results_list):
        try:
            self.header()
            print('Result:\n')
            print("\tIP\t\t\tMAC Address")
            print('\t-----------------------------------------')
            for client in results_list:
                if len(client["ip"]) < 8:
                    pass
                else:
                    print('\t' + GREEN + BOLD + client["ip"] + "\t\t" + client["mac"] + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    NetScan()
                elif cmd == 'z':
                    Scanning()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
