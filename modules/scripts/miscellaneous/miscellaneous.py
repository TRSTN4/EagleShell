#!/usr/bin/python3

from assets.headers import miscellaneous_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix


class Miscellaneous:
    def __init__(self):
        try:
            miscellaneous_header()
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
