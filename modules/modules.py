#!/usr/bin/python3

from assets.headers import modules_header
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
from assets.shortcuts import Exit


class Modules:
    def __init__(self):
        try:
            modules_header()
            print('Modules:\n')
            print('\t1): Eagle Scripts')
            print('\t2): Settings')
            print('\n\tX): Exit\n')
            while True:
                menu_select = input(eagleshell_prefix).lower()
                if menu_select == '1':
                    from modules.scripts.scripts import Scripts
                    Scripts()
                elif menu_select == '2':
                    from modules.settings.settings import Settings
                    Settings()
                elif menu_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
