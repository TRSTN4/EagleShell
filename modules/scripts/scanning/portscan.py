#!/usr/bin/python3

from assets.banners import portscan_banner
from assets.colors import *
from assets.designs import logo, line, author
from assets.prefixes import eagleshell_prefix, invalid_input_prefix, rhost_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .scanning import Scanning
import os
import socket


class PortScan:
    def __init__(self):
        self.port_list = []
        self.configuration()
        self.scan_target()
        self.result()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print('\n' + line)
        print(portscan_banner)
        print(line + '\n')
        print(author)

    def configuration(self):
        try:
            self.header()
            print('RHOST:')
            print('\n\tExample: 192.168.1.128')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.rhost_set = input(rhost_prefix).lower()
            if self.rhost_set == 'z':
                Scanning()
            elif self.rhost_set == 'x':
                Exit()
        except KeyboardInterrupt:
            Exit()

    def scan_target(self):
        try:
            self.header()
            print('Scanning:\n')
            print('\tScanning target ' + self.rhost_set + '\n')
            try:
                for port in range(1, 65535):
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(1)
                    final_result = s.connect_ex((self.rhost_set, port))
                    if final_result == 0:
                        print('\tPort {} is open'.format(port))
                        self.port_list.append(format(port))
            except socket.gaierror:
                print('Hostname could not be resolved.')
                PortScan()
            except socket.error:
                print("Couldn't connect to server.")
                PortScan()
        except KeyboardInterrupt:
            self.result()

    def result(self):
        try:
            self.header()
            print('Output:\n')
            if len(self.port_list) < 1:
                print('\tRHOST: ' + RED + BOLD + self.rhost_set + WHITE)
            else:
                print('\tRHOST: ' + GREEN + BOLD + self.rhost_set + WHITE)
            if len(self.port_list) < 1:
                print('\n\tOPEN PORTS: ' + RED + BOLD + 'NONE' + WHITE)
            else:
                print('\n\tOPEN PORTS: ' + GREEN + BOLD + format(self.port_list).replace('[', '').replace(']', '').replace("'", '') + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    PortScan()
                elif cmd == 'z':
                    Scanning()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()