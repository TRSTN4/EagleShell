#!/usr/bin/python3

from assets.banners import web_banner
from assets.properties import clear_screen
from assets.designs import logo, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Web:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print(web_banner)
            print(author)
            print('Scripts:')
            print('\n\t1): SOON')
            print('\t2): SOON')
            print('\t3): SOON')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                miscellaneous_select = input(eagleshell_prefix).lower()
                if miscellaneous_select == '1':
                    pass
                elif miscellaneous_select == '2':
                    pass
                elif miscellaneous_select == '3':
                    pass
                elif miscellaneous_select == '4':
                    pass
                elif miscellaneous_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif miscellaneous_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
