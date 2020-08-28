#!/usr/bin/python3

from assets.banners import scanning_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input
import os


class Scanning:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(scanning_banner)
            print(line)
            print('')
            print(author)
            print('Scripts:')
            print('')
            print('\t1): EAGLEYE - Network Scanner')
            print('\t2): EAGLESCAN - Port Scanner')
            print('\t3): SUBSCAN - Sub Domain Scanner')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            while True:
                scanning_select = input(eagleshell_prefix).lower()
                if scanning_select == '1':
                    from modules.scripts.scanning.eagleye import eagleye_main
                    eagleye_main()
                elif scanning_select == '2':
                    from modules.scripts.scanning.eaglescan import eaglescan_main
                    eaglescan_main()
                elif scanning_select == '3':
                    from modules.scripts.scanning.subscan import subscan_main
                    subscan_main()
                elif scanning_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif scanning_select == 'x':
                    Exit()
                else:
                    print(invalid_input)
                    continue
        except KeyboardInterrupt:
            Exit()
