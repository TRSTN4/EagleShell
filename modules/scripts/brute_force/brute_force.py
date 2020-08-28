#!/usr/bin/python3

from assets.banners import brute_force_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input
import os


class BruteForce:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(brute_force_banner)
            print(line)
            print('')
            print(author)
            print('Scripts:')
            print('')
            print('\t1): BruteSSH')
            print('\t2): BruteFTP')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            while True:
                privilege_escalation_select = input(eagleshell_prefix).lower()
                if privilege_escalation_select == '1':
                    from modules.scripts.brute_force.brutessh import brutessh_main
                    brutessh_main()
                    pass
                elif privilege_escalation_select == '2':
                    from modules.scripts.brute_force.bruteftp import bruteftp_main
                    bruteftp_main()
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
