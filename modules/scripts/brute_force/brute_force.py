#!/usr/bin/python3

from assets.headers import brute_force_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix


class BruteForce:
    def __init__(self):
        try:
            brute_force_header()
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
