#!/usr/bin/python3

from assets.headers import cryptography_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix


class Cryptography:
    def __init__(self):
        try:
            cryptography_header()
            print('Scripts:')
            print('\n\t1): Hashing - Text and File Hashing')
            print('\t2): SOON - Crypt - Encrypter and Decrypter')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                web_select = input(eagleshell_prefix).lower()
                if web_select == '1':
                    from modules.scripts.cryptography.hashing import Hashing
                    Hashing()
                elif web_select == '2':
                    pass
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
