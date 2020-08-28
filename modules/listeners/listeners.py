#!/usr/bin/python3

from assets.banners import listeners_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Listeners:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(listeners_banner)
            print(line)
            print('')
            print(author)
            print('Options:')
            print('')
            print('\t1): Soon')
            print('\t2): Soon')
            print('\t3): Soon')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            while True:
                listeners_select = input(eagleshell_prefix).lower()
                if listeners_select == '1':
                    pass
                elif listeners_select == '2':
                    pass
                elif listeners_select == '3':
                    pass
                elif listeners_select == 'z':
                    from ..modules import Modules
                    Modules()
                elif listeners_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
