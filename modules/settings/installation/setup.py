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
                print(GREEN + "\n[+] Installing 'os' Python Package.")
                os.system('pip install os >/dev/null 2>&1')
                os.system('pip3 install os >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'queue' Python Package.")
                os.system('pip install queue >/dev/null 2>&1')
                os.system('pip3 install queue >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'ftplib' Python Package.")
                os.system('pip3 install ftplib >/dev/null 2>&1')
                os.system('pip3 install ftplib >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'threading' Python Package.")
                os.system('pip install threading >/dev/null 2>&1')
                os.system('pip3 install threading >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'paramiko' Python Package.")
                os.system('pip install paramiko >/dev/null 2>&1')
                os.system('pip3 install paramiko >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'socket' Python Package.")
                os.system('pip install socket >/dev/null 2>&1')
                os.system('pip3 install socket >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'time' Python Package.")
                os.system('pip install time >/dev/null 2>&1')
                os.system('pip3 install time >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'cryptography' Python Package.")
                os.system('pip install cryptography >/dev/null 2>&1')
                os.system('pip3 install cryptography >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'hashlib' Python Package.")
                os.system('pip install hashlib >/dev/null 2>&1')
                os.system('pip3 install hashlib >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'netifaces' Python Package.")
                os.system('pip3 install netifaces >/dev/null 2>&1')
                os.system('pip3 install netifaces >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'pyperclip' Python Package.")
                os.system('pip install pyperclip >/dev/null 2>&1')
                os.system('pip3 install pyperclip >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'PIL' Python Package.")
                os.system('pip install PIL >/dev/null 2>&1')
                os.system('pip3 install PIL >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'socket' Python Package.")
                os.system('pip install socket >/dev/null 2>&1')
                os.system('pip3 install socket >/dev/null 2>&1')
                print(GREEN + "\n[+] Installing 'time' Python Package.")
                os.system('pip install time >/dev/null 2>&1')
                os.system('pip3 install time >/dev/null 2>&1')
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
