#!/usr/bin/python3

from assets.banners import payloads_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Payloads:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(payloads_banner)
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
                payloads_select = input(eagleshell_prefix).lower()
                if payloads_select == '1':
                    pass
                elif payloads_select == '2':
                    pass
                elif payloads_select == '3':
                    pass
                elif payloads_select == 'z':
                    from ..modules import Modules
                    Modules()
                elif payloads_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
