#!/usr/bin/python3

# EagleScan - Port Scanner

# Imports all the needed variables and packages
from assets.banners import eaglscan_banner
from assets.designs import *
from assets.properties import clear_screen
from assets.redirect import redirect_eagleshell_scanning
from assets.redirect import redirect_eagleshell_menu
import os
import socket
from datetime import datetime


# Main function
def eaglescan_main():

    # Function that takes user input
    def configuration():
        try:
            global rhost_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(eaglscan_banner)
            print(line)
            print('')
            print(author)
            print('Configuration:')
            print('')
            print('\tSelect Target IP')
            print('\t----------------')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            rhost_set = input('\u001b[33mRHOST \u001b[37m> ').lower()
            if rhost_set == 'z':
                redirect_eagleshell_scanning()
            elif rhost_set == 'x':
                exit_shell()
            display()
        except KeyboardInterrupt:
            exit_shell()

    # Function that displays port scanning progress
    def display():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(eaglscan_banner)
            print(line)
            print('')
            print(author)
            print('Scanning:')
            start()
            result()
        except KeyboardInterrupt:
            exit_shell()

    # Function that starts scanning the ports
    def start():
        global port_list
        port_list = []
        print('')
        print("\tScanning target " + rhost_set)
        print("\tTime started: " + str(datetime.now()))
        print('')

        try:
            for port in range(1, 65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                final_result = s.connect_ex((rhost_set, port))
                if final_result == 0:
                    print("\tPort {} is open".format(port))
                    port_list.append(format(port))

        except KeyboardInterrupt:
            exit_shell()

        except socket.gaierror:
            print("Hostname could not be resolved.")
            configuration()

        except socket.error:
            print("Couldn't connect to server.")
            configuration()

    # Function that displays result
    def result():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(eaglscan_banner)
            print(line)
            print('')
            print(author)
            print('Output:')
            print('')
            print('\tRHOST: ' + rhost_set)
            print('')
            print('\tOPEN PORTS: ' + '\u001b[32m' + format(port_list).replace('[', '').replace(']', '').replace("'", ''))
            print('\u001b[37m')
            print('\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit')
            print('')
            while True:
                eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if eagleshell_cmd == 'y':
                    eaglescan_main()
                elif eagleshell_cmd == 'z':
                    redirect_eagleshell_menu()
                elif eagleshell_cmd == 'x':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    # Function that exit
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


eaglescan_main()
