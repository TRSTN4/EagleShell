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
            print('\n\t1): LinkExtract')
            print('\n\t2): SubScan')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                web_select = input(eagleshell_prefix).lower()
                if web_select == '1':
                    from modules.scripts.web.linkextract import LinkExtract
                    LinkExtract()
                elif web_select == '2':
                    from modules.scripts.web.subscan import SubScan
                    SubScan()
                elif web_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif web_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
