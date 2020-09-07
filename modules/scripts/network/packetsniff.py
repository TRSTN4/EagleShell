#!/usr/bin/python3

from assets.banners import packetsniffer_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, interface_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .network import Network
import os
import netifaces
import scapy.all as scapy
from scapy.layers import http


class PacketSniff:
    def __init__(self):
        self.allowed_interface_list = ['wlan0', 'wlan1', 'wlan2', 'wlan3', 'mon0', 'mon1', 'mon2', 'mon3', 'wlp5s0', 'wlp5s1', 'wlp5s2', 'wlp5s3', 'eth0', 'eth1', 'eth2', 'eth3']
        self.disallowed_interface_list = ['lo', 'tun0', 'tun1', 'tun2', 'tun3', 'mon1', 'mon2', 'mon3', 'wlp5s0', 'wlp5s1', 'wlp5s2', 'wlp5s3', 'eth0', 'eth1', 'eth2', 'eth3']
        self.total_credentials = 0
        self.total_requests = 0
        self.configuration()
        self.sniff()
        self.result()

    def header(self):
            os.system(clear_screen)
            print(logo)
            print(packetsniffer_banner)
            print(author)

    def configuration(self):
        try:
            self.header()
            print('Configuration:')
            self.interfaces()
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                self.interface_set = input(interface_prefix).lower()
                if self.interface_set in self.allowed_interface_list:
                    break
                elif self.interface_set == 'z':
                    Network()
                elif self.interface_set == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()

    def interfaces(self):
        x = netifaces.interfaces()
        for i in x:
            if i in self.allowed_interface_list:
                print(GREEN + '\n\t[+] Available Interface: ' + i + WHITE)
            elif self.disallowed_interface_list != i:
                print(RED + '\n\t[-] Unavailable Interface: ' + i + WHITE)

    def sniff(self):
        try:
            self.header()
            print('Output:')
            print('\n\tControls')
            print('\t--------')
            print('\tStop: CTRL+C\n')
            scapy.sniff(iface=self.interface_set, store=False, prn=self.process_sniffed_packet)
        except KeyboardInterrupt:
            self.result()

    def process_sniffed_packet(self, packet):
        try:
            if packet.haslayer(http.HTTPRequest):
                url = self.get_url(packet)
                print(YELLOW + '\t[+] ' + GREEN + 'HTTP Request ' + WHITE + '>> ' + BLUE + url.decode() + WHITE)
                self.total_requests = self.total_requests + 1
                login_info = self.get_login_info(packet)
                if login_info:
                    print(YELLOW + '\t[!] ' + MAGENTA + 'Possible Credentials Found ' + WHITE + '>> ' + BLUE + login_info + WHITE)
                self.total_credentials = self.total_credentials + 1
        except KeyboardInterrupt:
            self.result()

    def get_url(self, packet):
        try:
            return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        except KeyboardInterrupt:
            self.result()

    def get_login_info(self, packet):
        try:
            if packet.haslayer(scapy.Raw):
                load = str(packet[scapy.Raw].load)
                keywords = ["username", "user", "login", "password", "pass"]
                for keywords in keywords:
                    if keywords in load:
                        return load
        except KeyboardInterrupt:
            self.result()

    def result(self):
        try:
            self.header()
            print('Result:')
            print('\n\tInput')
            print('\t-----')
            print('\tINTERFACE: ' + GREEN + self.interface_set + WHITE)
            print('\n\tOutput')
            print('\t------')
            print('\tTOTAL REQUESTS: ' + GREEN + str(self.total_requests) + WHITE)
            print('\tTOTAL CREDENTIALS: ' + GREEN + str(self.total_credentials) + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    PacketSniff()
                elif cmd == 'z':
                    Network()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
