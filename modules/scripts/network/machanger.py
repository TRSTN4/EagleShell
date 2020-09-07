#!/usr/bin/python3

from assets.banners import machanger_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, interface_prefix, new_mac_prefix, unavailable_interface_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .network import Network
import os
import subprocess
import netifaces
import re


class MAChanger:
    def __init__(self):
        self.allowed_interface_list = ['wlan0', 'wlan1', 'wlan2', 'wlan3', 'mon0', 'mon1', 'mon2', 'mon3', 'wlp5s0', 'wlp5s1', 'wlp5s2', 'wlp5s3', 'eth0', 'eth1', 'eth2', 'eth3']
        self.disallowed_interface_list = ['lo', 'tun0', 'tun1', 'tun2', 'tun3', 'mon1', 'mon2', 'mon3', 'wlp5s0', 'wlp5s1', 'wlp5s2', 'wlp5s3', 'eth0', 'eth1', 'eth2', 'eth3']
        self.configuration()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print(machanger_banner)
        print(author)

    def configuration(self):
        try:
            self.header()
            print('Configuration:')
            self.interfaces()
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                self.interface_set = input(interface_prefix)
                if self.interface_set in self.allowed_interface_list:
                    self.set_mac()
                elif self.interface_set == 'z':
                    Network()
                elif self.interface_set == 'x':
                    Exit()
                else:
                    print(unavailable_interface_prefix)
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
                    Network()
                elif self.mac_set == 'x':
                    Exit()
                else:
                    self.run_tasks()
        except KeyboardInterrupt:
            Exit()

    def run_tasks(self):
        self.change_mac()
        self.current_mac = self.get_current_mac()
        if self.current_mac == self.mac_set:
            self.confirmed = 'MAC address was successfully changed.'
            self.succ_fail = True
            self.result()
        else:
            self.confirmed = 'MAC address did not get changed.'
            self.succ_fail = False
            self.result()

    def get_current_mac(self):
        try:
            ifconfig_result = subprocess.check_output(["ifconfig", self.interface_set])
            mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
            if mac_address_search_result:
                return mac_address_search_result.group(0)
            else:
                pass
        except subprocess.CalledProcessError:
            print(RED + '[-] Failed.. Please Try Again.' + WHITE)
            os.system('sleep 1')
            Exit()

    def change_mac(self):
        os.system("ifconfig " + self.interface_set + " down" + " >/dev/null 2>&1")
        os.system("ifconfig " + self.interface_set + " hw " + " ether " + self.mac_set + " >/dev/null 2>&1")
        os.system("ifconfig " + self.interface_set + " up" + " >/dev/null 2>&1")

    def result(self):
        try:
            self.header()
            if self.succ_fail == True:
                color = GREEN
            else:
                color = RED
            print('Result:')
            print('\n\tINTERFACE SET: ' + color + self.interface_set + WHITE)
            print('\n\tMAC SET: ' + color + self.mac_set + WHITE)
            print('\n\t---------------------------------------------')
            print('\n\tRESULT: ' + color + self.confirmed + WHITE)
            print('\n\tCURRENT MAC: ' + color + self.current_mac + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    MAChanger()
                elif cmd == 'z':
                    Network()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
