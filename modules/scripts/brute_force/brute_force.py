#!/usr/bin/python3

from assets.headers import brute_force_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
from assets.colors import *


class BruteForce:
    def __init__(self):
        try:
            brute_force_header()
            print('Scripts:')
            print('\n\t1): BruteSSH - Brute Force SSH ' + RED + '* NOT RECOMMENDED *' + RESET + WHITE)
            print('\t2): BruteFTP - Brute Force FTP ' + RED + '* NOT RECOMMENDED *' + RESET + WHITE)
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
