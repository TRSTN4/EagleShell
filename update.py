#!/usr/bin/python3

# EagleShell Updater

# Imports needed package
import os


# Main update function
def update_main():

    # Function that updates tool
    def update():
        try:
            print('\u001b[37mUpdate:')
            print('')
            print('\tAre you inside the EagleShell Directory? \u001b[32mY\u001b[37m/\u001b[31mN')
            print('\t\u001b[37m--------------------------------------------')
            print('')
            update_select = input('\u001b[33mEagleShell \u001b[37m> ').lower()
            if update_select == 'yes' or update_select == 'y':
                print('\u001b[32m[+] Updating EagleShell...')
                os.system('git fetch >/dev/null 2>&1')
                os.system('git reset --hard origin/master >/dev/null 2>&1')
                os.system('git checkout master >/dev/null 2>&1')
                os.system('git pull >/dev/null 2>&1')
                print('\u001b[32m[+] Update Complete!')
                print('\u001b[0m')
                exit()
            else:
                print('\u001b[31m[-] Please make sure to run this in the EagleShell directory.')
                print('\u001b[0m')
                exit()
        except KeyboardInterrupt:
            from assets.functions import exit_main
            exit_main()

    update()


update_main()
