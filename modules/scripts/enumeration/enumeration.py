#!/usr/bin/python3

from assets.banners import enumeration_banner
from assets.properties import clear_screen
from assets.designs import logo, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Enumeration:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print(enumeration_banner)
            print(author)
            print('Scripts:')
            print('\n\t1): Soon')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                enumeration_select = input(eagleshell_prefix).lower()
                if enumeration_select == '1':
                    pass
                elif enumeration_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif enumeration_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
