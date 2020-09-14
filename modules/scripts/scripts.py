#!/usr/bin/python3

from assets.headers import scripts_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix


class Scripts:
    def __init__(self):
        try:
            scripts_header()
            print('Options:')
            print('\n\t1): Scanning')
            print('\t2): Enumeration')
            print('\t3): Exploitation')
            print('\t4): Privilege Escalation')
            print('\t5): Brute Force')
            print('\t6): Network')
            print('\t7): Web')
            print('\t8): Miscellaneous')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                scripts_select = input(eagleshell_prefix).lower()
                if scripts_select == '1':
                    from .scanning.scanning import Scanning
                    Scanning()
                elif scripts_select == '2':
                    from .enumeration.enumeration import Enumeration
                    Enumeration()
                elif scripts_select == '3':
                    from .exploitation.exploitation import Exploitation
                    Exploitation()
                elif scripts_select == '4':
                    from .privilege_escalation.privilege_escalation import PrivilegeEscalation
                    PrivilegeEscalation()
                elif scripts_select == '5':
                    from .brute_force.brute_force import BruteForce
                    BruteForce()
                elif scripts_select == '6':
                    from .network.network import Network
                    Network()
                elif scripts_select == '7':
                    from .web.web import Web
                    Web()
                elif scripts_select == '8':
                    from .miscellaneous.miscellaneous import Miscellaneous
                    Miscellaneous()
                elif scripts_select == '9':
                    from .miscellaneous.miscellaneous import Miscellaneous
                    Miscellaneous()
                elif scripts_select == 'z':
                    from ..modules import Modules
                    Modules()
                elif scripts_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
