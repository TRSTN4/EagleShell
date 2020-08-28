#!/usr/bin/python3

from assets.banners import miscellaneous_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Miscellaneous:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(miscellaneous_banner)
            print(line)
            print('')
            print(author)
            print('Scripts:')
            print('')
            print('\t1): MACHANGER - Change MAC Address')
            print('\t2): SOON - EXIF - Image Metadata Extractor')
            print('\t3): SOON - CRYPT - Encrypter and Decrypter')
            print('\t4): HASHING - Text and File Hashing')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            while True:
                miscellaneous_select = input(eagleshell_prefix).lower()
                if miscellaneous_select == '1':
                    from modules.scripts.miscellaneous.machanger import machanger_main
                    machanger_main()
                elif miscellaneous_select == '2':
                    from modules.scripts.miscellaneous.exif import exif_main
                    exif_main()
                elif miscellaneous_select == '3':
                    from modules.scripts.miscellaneous.crypt import crypt_main
                    crypt_main()
                elif miscellaneous_select == '4':
                    from modules.scripts.miscellaneous.hashing import hashing_main
                    hashing_main()
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
