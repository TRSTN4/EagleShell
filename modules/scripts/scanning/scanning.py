#!/usr/bin/python3

from assets.headers import scanning_header
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
from assets.shortcuts import Exit


class Scanning:
    def __init__(self):
        try:
            scanning_header()
            print('Scripts:')
            print('\n\t1): NetScan - Network Scanner')
            print('\t2): PortScan - Port Scanner')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                scanning_select = input(eagleshell_prefix).lower()
                if scanning_select == '1':
                    from modules.scripts.scanning.netscan import NetScan
                    NetScan()
                elif scanning_select == '2':
                    from modules.scripts.scanning.portscan import PortScan
                    PortScan()
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
