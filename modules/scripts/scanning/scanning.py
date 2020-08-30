#!/usr/bin/python3

from assets.banners import scanning_banner
from assets.designs import logo, line, author
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
import os


class Scanning:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('\n' + line)
            print(scanning_banner)
            print(line + '\n')
            print(author)
            print('Scripts:')
            print('\n\t1): EAGLEYE - Network Scanner')
            print('\t2): EAGLESCAN - Port Scanner')
            print('\t3): SUBSCAN - Sub Domain Scanner')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                scanning_select = input(eagleshell_prefix).lower()
                if scanning_select == '1':
                    from modules.scripts.scanning.eagleye import NetScan
                    NetScan()
                elif scanning_select == '2':
                    from modules.scripts.scanning.eaglescan import PortScan
                    PortScan()
                elif scanning_select == '3':
                    from modules.scripts.scanning.subscan import SubScan
                    SubScan()
                elif scanning_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif scanning_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
