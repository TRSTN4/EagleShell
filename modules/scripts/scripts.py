#!/usr/bin/python3

from assets.banners import scripts_banner
from assets.properties import clear_screen
from assets.designs import logo, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix
import os


class Scripts:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print(scripts_banner)
            print(author)
            print('Options:')
            print('\n\t1): Scanning')
            print('\t2): Enumeration')
            print('\t3): Exploitation')
            print('\t4): Privilege Escalation')
            print('\t5): Brute Force')
            print('\t6): Network')
            print('\t7): Miscellaneous')
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
