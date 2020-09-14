#!/usr/bin/python3

from assets.headers import settings_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix


class Settings:
    def __init__(self):
        try:
            settings_header()
            print('Options:')
            print('\n\t1): Update')
            print('\t2): Version')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                settings_select = input(eagleshell_prefix).lower()
                if settings_select == '1':
                    from modules.settings.installation.update import Update
                    Update()
                elif settings_select == '2':
                    from modules.settings.other.version import Version
                    Version()
                elif settings_select == 'z':
                    from ..modules import Modules
                    Modules()
                elif settings_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
