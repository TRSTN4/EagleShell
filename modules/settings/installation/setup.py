#!/usr/bin/python3

from assets.headers import setup_header
from assets.colors import *
from assets.prefixes import eagleshell_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
import os


class Setup:
    def __init__(self):
        try:
            setup_header()
            print('Update:\n')
            print(WHITE + '\tAre you ready to setup EagleShell? ' + GREEN + 'Y' + WHITE + '/' + RED + 'N')
            print(WHITE + '\t--------------------------------------------\n')
            setup_select = input(eagleshell_prefix).lower()
            if setup_select == 'yes' or setup_select == 'y':
                print(GREEN + '\n[+] Installing EagleShell...')
                packages = ['os', 'queue', 'ftplib', 'threading', 'paramiko', 'socket', 'time', 'cryptography',
                            'hashlib', 'netifaces', 'pyperclip', 'PIL', 'scapy', 'sys', 'netfilterqueue', 'subprocess',
                            're', 'requests', 'tqdm', 'beautifulsoup4', 'urllib']
                for package in packages:
                    print(GREEN + "\n[+] Installing '" + package + "' Python Package.")
                    os.system('pip install ' + package + ' >/dev/null 2>&1')
                    os.system('pip3 install ' + package + ' >/dev/null 2>&1')
                print(GREEN + '\n[+] Install Complete!' + RESET)
                os.system('sleep 3')
                os.system(clear_screen)
                exit()
            else:
                print(RED + '\n[-] Setup cancelled.' + RESET)
                os.system('sleep 3')
                os.system(clear_screen)
                exit()
        except KeyboardInterrupt:
            Exit()


Setup()
