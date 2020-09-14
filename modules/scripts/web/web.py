#!/usr/bin/python3

from assets.headers import web_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix


class Web:
    def __init__(self):
        try:
            web_header()
            print('Scripts:')
            print('\n\t1): LinkExtract -  Extract All Website Links')
            print('\t2): IMGExtract -  Extract All Website Images')
            print('\t3): SubScan - Sub Domain Scanner')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                web_select = input(eagleshell_prefix).lower()
                if web_select == '1':
                    from modules.scripts.web.linkextract import LinkExtract
                    LinkExtract()
                if web_select == '2':
                    from modules.scripts.web.imgextract import IMGExtract
                    IMGExtract()
                elif web_select == '3':
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
