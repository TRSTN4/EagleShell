#!/usr/bin/python3

from assets.banners import *
from assets.properties import *
from assets.designs import *
from assets.commands import *

import os

# dev branch

def menu():
    try:
        global menu_select
        os.system(clear_screen)
        print(logo)
        print(eagle)
        print('\u001b[37mVersion: ' + version)
        print(author)
        print('Modules:')
        print('')
        print('\t1): Eagle Payloads')
        print('\t2): Eagle Listeners')
        print('\t3): Eagle Scripts')
        print('\t4): Exit')
        print('')
        while True:
            menu_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if menu_select == '1':
                payloads()
            elif menu_select == '2':
                listeners()
            elif menu_select == '3':
                scripts()
            elif menu_select == '4':
                exit_shell()
            elif menu_select == 'help' or menu_select == '?':
                from assets.commands import help_list
                help_list()
            elif menu_select == 'exit' or menu_select == 'quit':
                exit_shell()
            elif menu_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def payloads():
    try:
        global payloads_select
        os.system(clear_screen)
        print(logo)
        print('')
        print(line)
        print(payloads_banner)
        print(line)
        print('')
        print(author)
        print('Options:')
        print('')
        print('\t1): Soon')
        print('\t2): Soon')
        print('\t3): Soon')
        print('\t4): Back')
        print('\t5): Exit')
        print('')
        while True:
            payloads_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if payloads_select == '1':
                pass
            elif payloads_select == '2':
                pass
            elif payloads_select == '3':
                pass
            elif payloads_select == '4':
                menu()
            elif payloads_select == '5':
                exit_shell()
            elif payloads_select == 'help' or payloads_select == '?':
                from assets.commands import help_list
                help_list()
            elif payloads_select == 'exit' or payloads_select == 'quit':
                exit_shell()
            elif payloads_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def listeners():
    try:
        global listeners_select
        os.system(clear_screen)
        print(logo)
        print('')
        print(line)
        print(listeners_banner)
        print(line)
        print('')
        print(author)
        print('Options:')
        print('')
        print('\t1): Soon')
        print('\t2): Soon')
        print('\t3): Soon')
        print('\t4): Back')
        print('\t5): Exit')
        print('')
        while True:
            listeners_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if listeners_select == '1':
                pass
            elif listeners_select == '2':
                pass
            elif listeners_select == '3':
                pass
            elif listeners_select == '4':
                menu()
            elif listeners_select == '5':
                exit_shell()
            elif listeners_select == 'help' or listeners_select == '?':
                from assets.commands import help_list
                help_list()
            elif listeners_select == 'exit' or listeners_select == 'quit':
                exit_shell()
            elif listeners_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def scripts():
    try:
        global scripts_select
        os.system(clear_screen)
        print(logo)
        print('')
        print(line)
        print(scripts_banner)
        print(line)
        print('')
        print(author)
        print('Options:')
        print('')
        print('\t1): Scanning')
        print('\t2): Enumeration')
        print('\t3): Privilege Escalation')
        print('\t4): Other')
        print('\t5): Back')
        print('\t6): Exit')
        print('')
        while True:
            scripts_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if scripts_select == '1':
                scanning()
            elif scripts_select == '2':
                enumeration()
            elif scripts_select == '3':
                privilege_escalation()
            elif scripts_select == '4':
                miscellaneous()
            elif scripts_select == '5':
                menu()
            elif scripts_select == '6':
                exit_shell()
            elif scripts_select == 'help' or scripts_select == '?':
                from assets.commands import help_list
                help_list()
            elif scripts_select == 'exit' or scripts_select == 'quit':
                exit_shell()
            elif scripts_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def scanning():
    try:
        os.system(clear_screen)
        print(logo)
        print('')
        print(line)
        print(scanning_banner)
        print(line)
        print('')
        print(author)
        print('Scripts:')
        print('')
        print('\t1): EAGLEYE - Eagle Network Scanner')
        print('\t2): EAGLESCAN - Eagle Port Scanner')
        print('\t3): Soon')
        print('\t4): Back')
        print('\t5): Exit')
        print('')
        while True:
            scanning_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if scanning_select == '1':
                from modules.scripts.scanning.eagleye import eagleye_main
                eagleye_main()
            elif scanning_select == '2':
                from modules.scripts.scanning.eaglescan import eaglescan_main
                eaglescan_main()
            elif scanning_select == '3':
                pass
            elif scanning_select == '4':
                scripts()
            elif scanning_select == '5':
                exit_shell()
            elif scanning_select == 'help' or scanning_select == '?':
                from assets.commands import help_list
                help_list()
            elif scanning_select == 'exit' or scanning_select == 'quit':
                exit_shell()
            elif scanning_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def enumeration():
    try:
        os.system(clear_screen)
        print(logo)
        print('')
        print(line)
        print(enumeration_banner)
        print(line)
        print('')
        print(author)
        print('Scripts:')
        print('')
        print('\t1): Soon')
        print('\t2): Soon')
        print('\t3): Soon')
        print('\t4): Back')
        print('\t5): Exit')
        print('')
        while True:
            enumeration_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if enumeration_select == '1':
                pass
            elif enumeration_select == '2':
                pass
            elif enumeration_select == '3':
                pass
            elif enumeration_select == '4':
                scripts()
            elif enumeration_select == '5':
                exit_shell()
            elif enumeration_select == 'help' or enumeration_select == '?':
                from assets.commands import help_list
                help_list()
            elif enumeration_select == 'exit' or enumeration_select == 'quit':
                exit_shell()
            elif enumeration_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def exploitation():
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
        print('\t1): RSGEN - Reverse Shell Generator')
        print('\t2): PGEN - Payload Generator')
        print('\t3): Soon')
        print('\t4): Back')
        print('\t5): Exit')
        print('')
        while True:
            exploitation_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if exploitation_select == '1':
                from modules.scripts.exploitation.rsgen import rsgen_main
                rsgen_main()
            elif exploitation_select == '2':
                from modules.scripts.exploitation.pgen import pgen_main
                pgen_main()
            elif exploitation_select == '3':
                pass
            elif exploitation_select == '4':
                scripts()
            elif exploitation_select == '5':
                exit_shell()
            elif exploitation_select == 'help' or exploitation_select == '?':
                from assets.commands import help_list
                help_list()
            elif exploitation_select == 'exit' or exploitation_select == 'quit':
                exit_shell()
            elif exploitation_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def privilege_escalation():
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
        print('\t4): Back')
        print('\t5): Exit')
        print('')
        while True:
            privilege_escalation_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if privilege_escalation_select == '1':
                pass
            elif privilege_escalation_select == '2':
                pass
            elif privilege_escalation_select == '3':
                pass
            elif privilege_escalation_select == '4':
                scripts()
            elif privilege_escalation_select == '5':
                exit_shell()
            elif privilege_escalation_select == 'help' or privilege_escalation_select == '?':
                from assets.commands import help_list
                help_list()
            elif privilege_escalation_select == 'exit' or privilege_escalation_select == 'quit':
                exit_shell()
            elif privilege_escalation_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def miscellaneous():
    try:
        os.system(clear_screen)
        print(logo)
        print('')
        print(line)
        print(miscellaneous_banner)
        print(line)
        print('')
        print(author)
        print('Scripts:')
        print('')
        print('\t1): MACHANGER - Change MAC from a Wireless Adapter')
        print('\t2): Soon')
        print('\t3): Soon')
        print('\t4): Back')
        print('\t5): Exit')
        print('')
        while True:
            miscellaneous_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if miscellaneous_select == '1':
                from modules.scripts.miscellaneous.machanger import machanger_main
                machanger_main()
            elif miscellaneous_select == '2':
                pass
            elif miscellaneous_select == '3':
                pass
            elif miscellaneous_select == '4':
                scripts()
            elif miscellaneous_select == '5':
                exit_shell()
            elif miscellaneous_select == 'help' or miscellaneous_select == '?':
                from assets.commands import help_list
                help_list()
            elif miscellaneous_select == 'exit' or miscellaneous_select == 'quit':
                exit_shell()
            elif miscellaneous_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()


def exit_shell():
    print('\u001b[31m[-] Exiting EagleShell')
    print('\u001b[0m')
    os.system(clear_screen)
    exit()


menu()
