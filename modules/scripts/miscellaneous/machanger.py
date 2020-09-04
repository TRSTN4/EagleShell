#!/usr/bin/python3

from assets.banners import machanger_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, interface_prefix, new_mac_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .miscellaneous import Miscellaneous
import os
import subprocess
import netifaces
import re


class MaChanger:
    def __init__(self):
        self.configuration()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print(machanger_banner)
        print(author)

    def configuration(self):
        try:
            print('Interface:')
            self.interfaces()
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                self.interface_set = input(interface_prefix).lower()
                if self.interface_set == 'wlan0' or self.interface_set == 'wlan1' or self.interface_set == 'wlan2' or self.interface_set == 'wlan3' or self.interface_set == 'mon0' or self.interface_set == 'mon1' or self.interface_set == 'mon2' or self.interface_set == 'mon3' or self.interface_set == 'wlp5s0' or self.interface_set == 'wlp5s1' or self.interface_set == 'wlp5s2' or self.interface_set == 'wlp5s3' or self.interface_set == 'eth0' or self.interface_set == 'eth1' or self.interface_set == 'eth2' or self.interface_set == 'eth3':
                    self.set_mac()
                elif self.interface_set == 'z':
                    Miscellaneous()
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
            if i == 'wlan0' or i == 'wlan1' or i == 'wlan2' or i == 'wlan3' or i == 'mon0' or i == 'mon1' or i == 'mon2' or i == 'mon3' or i == 'wlp5s0' or i == 'wlp5s1' or i == 'wlp5s2' or i == 'wlp5s3' or i == 'eth0' or i == 'eth1' or i == 'eth2' or i == 'eth3':
                print('\n\t[+] Available Interface: ' + i)
            elif i != 'lo' or i != 'tun0' or i != 'tun1' or i != 'tun2' or i != 'tun3':
                print('\n\t[-] Unavailable Interface: ' + i)

    def set_mac(self):
        try:
            self.header()
            print('MAC Address:')
            print('\n\tExample 1: 00:11:22:33:44:55')
            print('\tExample 2: 12:22:33:44:55:66')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                self.mac_set = input(new_mac_prefix).lower()
                if self.mac_set == 'z':
                    Miscellaneous()
                elif self.mac_set == 'x':
                    Exit()
                else:
                    self.functions()
        except KeyboardInterrupt:
            Exit()

    def change_mac(self):
        os.system("ifconfig " + self.interface_set + " down" + " >/dev/null 2>&1")
        os.system("ifconfig " + self.interface_set + " hw " + " ether " + self.mac_set + " >/dev/null 2>&1")
        os.system("ifconfig " + self.interface_set + " up" + " >/dev/null 2>&1")

    def get_current_mac(self):
        try:
            ifconfig_result = subprocess.check_output(["ifconfig", self.interface_set])
            mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
            if mac_address_search_result:
                return mac_address_search_result.group(0)
            else:
                pass
        except subprocess.CalledProcessError:
            print('print')

    def functions(self):
        self.current_mac = self.get_current_mac()
        self.change_mac()
        if self.current_mac == self.mac_set:
            self.confirmed = GREEN + "MAC address was successfully changed." + WHITE
            self.result()
        else:
            self.confirmed = RED + "MAC address did not get changed." + WHITE
            self.result()

    def result(self):
        try:
            self.header()
            print('Output:')
            print('\n\tINTERFACE SET: ' + self.interface_set)
            print('\n\tMAC SET: ' + self.mac_set)
            print('\n\t---------------------------------------------')
            print('\n\tRESULT: ' + self.confirmed)
            print('\n\tCURRENT MAC: ' + self.current_mac)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    MaChanger()
                elif cmd == 'z':
                    Miscellaneous()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
