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
                os.system('pip install netifaces')
                os.system('pip install scapy')
                print('\u001b[32m[+] Install Complete!')
                print('\u001b[0m')
                exit()
            else:
                print('\n\u001b[31m[-] Setup cancelled.')
                print('\u001b[0m')
                exit()
        except KeyboardInterrupt:
            exit_shell()

    # Function that exits
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    setup()


setup_main()
