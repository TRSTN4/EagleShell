#!/usr/bin/python3

from assets.banners import miscellaneous_banner
from assets.properties import clear_screen
from assets.designs import logo, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Miscellaneous:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print(miscellaneous_banner)
            print(author)
            print('Scripts:')
            print('\t2): SOON - EXIF - Image Metadata Extractor')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                miscellaneous_select = input(eagleshell_prefix).lower()
                if miscellaneous_select == '1':
                    from modules.scripts.miscellaneous.exif import Exif
                    Exif()
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
