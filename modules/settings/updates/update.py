#!/usr/bin/python3

# EagleShell Updater

# Imports all the needed packages
from assets.banners import update_banner
from assets.designs import *
from assets.properties import clear_screen
import os


# Main update function
def update_main():

    # Function that updates tool
    def update():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(update_banner)
            print(line)
            print('')
            print(author)
            print('Update:')
            print('')
            print('\tAre you inside the EagleShell Directory? \u001b[32mY\u001b[37m/\u001b[31mN')
            print('\t\u001b[37m--------------------------------------------')
            print('')
            update_select = input('\u001b[33mUPDATE \u001b[37m> ').lower()
            if update_select == 'yes' or update_select == 'y':
                print('\n\u001b[32m[+] Updating EagleShell...')
                os.system('git fetch >/dev/null 2>&1')
                os.system('git reset --hard origin/master >/dev/null 2>&1')
                os.system('git checkout master >/dev/null 2>&1')
                os.system('git pull >/dev/null 2>&1')
                print('\u001b[32m[+] Update Complete!')
                print('\u001b[0m')
                os.system('sleep 3')
                os.system(clear_screen)
            else:
                print('\n\u001b[31m[-] Please make sure to run this in the EagleShell directory.')
                print('\u001b[0m')
                os.system('sleep 3')
                os.system(clear_screen)
                exit()
        except KeyboardInterrupt:
            from assets.functions import exit_main
            exit_main()

    update()


update_main()
