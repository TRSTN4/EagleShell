#!/usr/bin/python3

from assets.banners import eaglscan_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from .scanning import Scanning
from assets.prefixes import eagleshell_prefix, invalid_input_prefix, rhost_prefix
from assets.colors import *
import socket
import os


class EagleScan:
    def __init__(self):
        self.port_list = []
        self.configuration()
        self.scanner()
        self.result()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print('')
        print(line)
        print(eaglscan_banner)
        print(line)
        print('')
        print(author)

    def configuration(self):
        try:
            self.header()
            print('Configuration:\n')
            print('\tSelect Target IP')
            print('\t----------------\n')
            print('\tZ): Back')
            print('\tX): Exit\n')
            self.rhost_set = input(rhost_prefix).lower()
            if self.rhost_set == 'z':
                Scanning()
            elif self.rhost_set == 'x':
                Exit()
        except KeyboardInterrupt:
            Exit()

    def scanner(self):
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
                EagleScan()
            except socket.error:
                print("Couldn't connect to server.")
                EagleScan()
        except KeyboardInterrupt:
            self.result()

    def result(self):
        try:
            self.header()
            print('Output:\n')
            print('\tRHOST: ' + self.rhost_set + '\n')
            print('\tOPEN PORTS: ' + '\u001b[32m' + format(self.port_list).replace('[', '').replace(']', '').replace("'", ''))
            print(WHITE + '\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    EagleScan()
                elif cmd == 'z':
                    Scanning()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
