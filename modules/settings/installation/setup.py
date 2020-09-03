#!/usr/bin/python3

from assets.banners import setup_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import eagleshell_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
import os


class Setup:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print(setup_banner)
            print(author)
            print('Update:\n')
            print(WHITE + '\tAre you ready to setup EagleShell? ' + GREEN + 'Y' + WHITE + '/' + RED + 'N')
            print(WHITE + '\t--------------------------------------------\n')
            setup_select = input(eagleshell_prefix).lower()
            if setup_select == 'yes' or setup_select == 'y':
                print(GREEN + '\n[+] Installing EagleShell...')
                print(GREEN + "\n[+] Installing 'netifaces' Python Package.")
                os.system('pip install netifaces >/dev/null 2>&1')
                os.system('pip3 install netifaces >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'scapy' Python Package.")
                os.system('pip install scapy >/dev/null 2>&1')
                os.system('pip3 install scapy >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'requests' Python Package.")
                os.system('pip3 install requests >/dev/null 2>&1')
                os.system('pip3 install requests >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'Pillow' Python Package.")
                os.system('pip install Pillow >/dev/null 2>&1')
                os.system('pip3 install Pillow >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'cryptography' Python Package.")
                os.system('pip install cryptography >/dev/null 2>&1')
                os.system('pip3 install cryptography >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'colorama' Python Package.")
                os.system('pip install colorama >/dev/null 2>&1')
                os.system('pip3 install colorama >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'paramiko' Python Package.")
                os.system('pip install paramiko >/dev/null 2>&1')
                os.system('pip3 install paramiko >/dev/null 2>&1')
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
