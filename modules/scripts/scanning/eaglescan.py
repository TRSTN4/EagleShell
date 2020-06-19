#!/usr/bin/python3

from assets.banners import eaglscan_banner
from assets.designs import *
from assets.properties import clear_screen

import sys
import os
import socket
import threading
from datetime import datetime

def eaglescan_main():

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
            print('RHOST:')
            print('')
            rhost_set = input('\u001b[33mRHOST \u001b[37m> ').lower()
            start()
        except KeyboardInterrupt:
            exit_shell()

    def start():
        print('')
        print("\tScanning target " + rhost_set)
        print("\tTime started: " + str(datetime.now()))
        print('')

        try:
            for port in range(1, 65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((rhost_set, port))
                if result == 0:
                    print("\tPort {} is open".format(port))
        except KeyboardInterrupt:
            exit_shell()

        except socket.gaierror:
            print("Hostname could not be resolved.")
            configuration()

        except socket.error:
            print("Couldn't connect to server.")
            configuration()

    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


eaglescan_main()
