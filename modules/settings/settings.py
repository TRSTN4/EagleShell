#!/usr/bin/python3

from assets.banners import settings_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Settings:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('\n' + line)
            print(settings_banner)
            print(line + '\n')
            print(author)
            print('Options:')
            print('\n\t1): Setup')
            print('\t2): Version')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                settings_select = input(eagleshell_prefix).lower()
                if settings_select == '1':
                    from modules.settings.updates.update import update_main
                    update_main()
                elif settings_select == '2':
                    pass
                elif settings_select == '3':
                    from assets.commands import eagleshell_version
                    eagleshell_version()
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
