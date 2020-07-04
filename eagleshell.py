#!/usr/bin/python3

# EagleShell Main Script

# Imports all needed variables and packages
from assets.banners import *
from assets.properties import *
from assets.designs import *
from assets.commands import *
import os


# Function that shows menu
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
        # print('\t1): Eagle Payloads')
        # print('\t2): Eagle Listeners')
        print('\t1): Eagle Scripts')
        print('\t2): Settings')
        print('')
        print('\tX): Exit')
        print('')
        while True:
            menu_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            # if menu_select == '1':
            # payloads()
            # elif menu_select == '2':
            # listeners()
            if menu_select == '1':
                scripts()
            elif menu_select == '2':
                settings()
            elif menu_select == 'x':
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

# Function that displays all payloads categories
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
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            payloads_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if payloads_select == '1':
                pass
            elif payloads_select == '2':
                pass
            elif payloads_select == '3':
                pass
            elif payloads_select == 'z':
                menu()
            elif payloads_select == 'x':
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

# Function that displays all listeners categories
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
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            listeners_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if listeners_select == '1':
                pass
            elif listeners_select == '2':
                pass
            elif listeners_select == '3':
                pass
            elif listeners_select == 'z':
                menu()
            elif listeners_select == 'x':
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

# Function that displays all scripts categories
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
        # print('\t2): Enumeration')
        print('\t2): Exploitation')
        # print('\t4): Privilege Escalation')
        print('\t3): Brute Force')
        print('\t4): Network')
        print('\t5): Miscellaneous')
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            scripts_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if scripts_select == '1':
                scanning()
            # elif scripts_select == '2':
                # enumeration()
            elif scripts_select == '2':
                exploitation()
            # elif scripts_select == '4':
                # privilege_escalation()
            elif scripts_select == '3':
                brute_force()
            elif scripts_select == '4':
                network()
            elif scripts_select == '5':
                miscellaneous()
            elif scripts_select == 'z':
                menu()
            elif scripts_select == 'x':
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

# Function that displays all scanning scripts
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
        print('\t3): SUBSCAN - Sub Domain Scanner')
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
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
                from modules.scripts.scanning.subscan import subscan_main
                subscan_main()
            elif scanning_select == 'z':
                scripts()
            elif scanning_select == 'x':
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

# Function that displays all enumeration scripts
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
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            enumeration_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if enumeration_select == '1':
                pass
            elif enumeration_select == '2':
                pass
            elif enumeration_select == '3':
                pass
            elif enumeration_select == 'z':
                scripts()
            elif enumeration_select == 'x':
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

# Function that displays all exploitation scripts
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
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
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
            elif exploitation_select == 'z':
                scripts()
            elif exploitation_select == 'x':
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

# Function that displays all privilege escalation scripts
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
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            privilege_escalation_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if privilege_escalation_select == '1':
                pass
            elif privilege_escalation_select == '2':
                pass
            elif privilege_escalation_select == '3':
                pass
            elif privilege_escalation_select == 'z':
                scripts()
            elif privilege_escalation_select == 'x':
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

# Function that displays all brute force scripts
def brute_force():
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
        print('\t1): BruteSSH')
        print('\t2): BruteFTP')
        print('\t3): Soon')
        print('')

        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            privilege_escalation_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if privilege_escalation_select == '1':
                from modules.scripts.brute_force.brutessh import brutessh
                brutessh_main()
                pass
            elif privilege_escalation_select == '2':
                from modules.scripts.brute_force.bruteftp import bruteftp_main
                bruteftp_main()
            elif privilege_escalation_select == '3':
                pass
            elif privilege_escalation_select == 'z':
                scripts()
            elif privilege_escalation_select == 'x':
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

# Function that displays all miscellaneous scripts
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
        print('\t1): MACHANGER - Change MAC Address')
        print('\t2): SOON - EXIF - Image Metadata Extractor')
        print('\t3): SOON - CRYPT - Encrypter and Decrypter')
        print('\t4): HASHING - Text and File Hashing')
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            miscellaneous_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if miscellaneous_select == '1':
                from modules.scripts.miscellaneous.machanger import machanger_main
                machanger_main()
            elif miscellaneous_select == '2':
                from modules.scripts.miscellaneous.exif import exif_main
                exif_main()
            elif miscellaneous_select == '3':
                from modules.scripts.miscellaneous.crypt import crypt_main
                crypt_main()
            elif miscellaneous_select == '4':
                from modules.scripts.miscellaneous.hashing import hashing_main
                hashing_main()
            elif miscellaneous_select == 'z':
                scripts()
            elif miscellaneous_select == 'x':
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

def network():
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
        print('\t1): ARPSPOOF - ARP Spoofer')
        print('\t2): PACKETSNIFFER - Packet Sniffer')
        print('\t3): Soon')
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            network_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if network_select == '1':
                from modules.scripts.network.arpspoof import arpspoof_main
                arpspoof_main()
            elif network_select == '2':
                from modules.scripts.network.packetsniff import packetsniff_main
                packetsniff_main()
            elif network_select == '3':
                pass
            elif network_select == 'z':
                scripts()
            elif network_select == 'x':
                exit_shell()
            elif network_select == 'help' or network_select == '?':
                from assets.commands import help_list
                help_list()
            elif network_select == 'exit' or network_select == 'quit':
                exit_shell()
            elif network_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()

# Function that shows all settings
def settings():
    try:
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
        print('\t1): Update')
        print('\t2): Soon')
        print('\t3): Version')
        print('')
        print('\tZ): Back')
        print('\tX): Exit')
        print('')
        while True:
            settings_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if settings_select == '1':
                from modules.settings.updates.update import update_main
                update_main()
            elif settings_select == '2':
                pass
            elif settings_select == '3':
                from assets.commands import eagleshell_version
                eagleshell_version()
            elif settings_select == 'z':
                menu()
            elif settings_select == 'x':
                exit_shell()
            elif settings_select == 'help' or settings_select == '?':
                from assets.commands import help_list
                help_list()
            elif settings_select == 'exit' or settings_select == 'quit':
                exit_shell()
            elif settings_select == 'version':
                from assets.commands import eagleshell_version
                eagleshell_version()
            else:
                print('\u001b[31m[-] Invalid Input.')
                continue
    except KeyboardInterrupt:
        exit_shell()

# Function that exits
def exit_shell():
    from assets.functions import exit_main
    exit_main()

menu()
