#!/usr/bin/python3

# EagleShell Updater

# Imports needed packages
from assets.banners import setup_banner
from assets.designs import *
from assets.properties import clear_screen
import os


# Main update function
def setup_main():

    # Function that installs all required packages
    def setup():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(setup_banner)
            print(line)
            print('')
            print(author)
            print('Setup:')
            print('')
            print('\tReady to Setup EagleShell? \u001b[32mY\u001b[37m/\u001b[31mN')
            print('\t\u001b[37m------------------------------')
            print('')
            setup_select = input('\u001b[33mSETUP \u001b[37m> ').lower()
            if setup_select == 'yes' or setup_select == 'y':
                print('\n\u001b[32m[+] Installing EagleShell...')
                os.system('pip install netifaces >/dev/null 2>&1')
                os.system('pip3 install netifaces >/dev/null 2>&1')
                os.system('pip install scapy >/dev/null 2>&1')
                os.system('pip3 install scapy >/dev/null 2>&1')
                os.system('pip3 install requests >/dev/null 2>&1')
                os.system('pip3 install requests >/dev/null 2>&1')
                os.system('pip install Pillow >/dev/null 2>&1')
                os.system('pip3 install Pillow >/dev/null 2>&1')
                os.system('pip install cryptography >/dev/null 2>&1')
                os.system('pip3 install cryptography >/dev/null 2>&1')
                os.system('pip3 install colorama >/dev/null 2>&1')
                os.system('pip3 install paramiko >/dev/null 2>&1')
                print('\u001b[32m[+] Install Complete!')
                print('\u001b[0m')
                os.system('sleep 3')
                os.system(clear_screen)
                exit()
            else:
                print('\n\u001b[31m[-] Setup cancelled.')
                print('\u001b[0m')
                os.system('sleep 3')
                os.system(clear_screen)
                exit()
        except KeyboardInterrupt:
            exit_shell()

    # Function that exits
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    setup()


setup_main()
