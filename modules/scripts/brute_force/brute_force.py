#!/usr/bin/python3

from assets.banners import brute_force_banner
from assets.properties import clear_screen
from assets.designs import logo, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class BruteForce:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print(brute_force_banner)
            print(author)
            print('Scripts:')
            print('\n\t1): SOON - BruteSSH')
            print('\t2): SOON - BruteFTP')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                privilege_escalation_select = input(eagleshell_prefix).lower()
                if privilege_escalation_select == '1':
                    from modules.scripts.brute_force.brutessh import BruteSSH
                    BruteSSH()
                elif privilege_escalation_select == '2':
                    from modules.scripts.brute_force.bruteftp import BruteFTP
                    BruteFTP()
                elif privilege_escalation_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif privilege_escalation_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
