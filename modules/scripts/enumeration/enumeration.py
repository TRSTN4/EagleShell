#!/usr/bin/python3

from assets.headers import enumeration_header
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input_prefix


class Enumeration:
    def __init__(self):
        try:
            enumeration_header()
            print('Scripts:')
            print('\n\t1): Soon - EagleEnum - Linux PE Enumeration Script')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                enumeration_select = input(eagleshell_prefix).lower()
                if enumeration_select == '1':
                    pass
                elif enumeration_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif enumeration_select == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
