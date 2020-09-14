#!/usr/bin/python3

from assets.headers import update_header
from assets.colors import *
from assets.prefixes import eagleshell_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
import os


class Update:
    def __init__(self):
        try:
            update_header()
            print('Update:\n')
            print(WHITE + '\tAre you inside the EagleShell Directory? ' + GREEN + 'Y' + WHITE + '/' + RED + 'N')
            print(WHITE + '\t--------------------------------------------\n')
            update_select = input(eagleshell_prefix).lower()
            if update_select == 'yes' or update_select == 'y':
                print(GREEN + '\n[+] Updating EagleShell...')
                os.system('git fetch >/dev/null 2>&1')
                os.system('git reset --hard origin/master >/dev/null 2>&1')
                os.system('git checkout master >/dev/null 2>&1')
                os.system('git pull >/dev/null 2>&1')
                print(GREEN + '[+] Update Complete!' + RESET)
                os.system('sleep 3')
                os.system(clear_screen)
                from modules.settings.installation.setup import Setup
                Setup()
            else:
                print(RED + '\n[-] Please make sure to run this in the EagleShell directory.' + RESET)
                os.system('sleep 3')
                os.system(clear_screen)
                exit()
        except KeyboardInterrupt:
            Exit()


Update()
