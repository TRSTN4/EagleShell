#!/usr/bin/python3

from assets.banners import privilege_escalation_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input
import os


class PrivilegeEscalation:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(privilege_escalation_banner)
            print(line)
            print('')
            print(author)
            print('Scripts:')
            print('')
            print('\t1): Soon')
            print('\t2): Soon')
            print('\t3): Soon')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            while True:
                privilege_escalation_select = input(eagleshell_prefix).lower()
                if privilege_escalation_select == '1':
                    pass
                elif privilege_escalation_select == '2':
                    pass
                elif privilege_escalation_select == '3':
                    pass
                elif privilege_escalation_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif privilege_escalation_select == 'x':
                    Exit()
                else:
                    print(invalid_input)
                    continue
        except KeyboardInterrupt:
            Exit()
