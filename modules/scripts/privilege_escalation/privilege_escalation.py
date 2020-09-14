#!/usr/bin/python3

from assets.headers import privilege_escalation_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix


class PrivilegeEscalation:
    def __init__(self):
        try:
            privilege_escalation_header()
            print('Scripts:')
            print('\n\t1): SOON')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                privilege_escalation_select = input(eagleshell_prefix).lower()
                if privilege_escalation_select == '1':
                    pass
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
