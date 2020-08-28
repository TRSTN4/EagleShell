#!/usr/bin/python3

from assets.banners import subscan_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from .scanning import Scanning
import requests
import os


class SubScan:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(subscan_banner)
            print(line)
            print('')
            print(author)
            print('Configuration:')
            print('')
            print('\tExample: google.com')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            self.website_set = input('\u001b[33mWEBSITE \u001b[37m> ').lower()
            if self.website_set == 'z':
                Scanning()
            elif self.website_set == 'x':
                Exit()
            else:
                self.wordlist()
        except KeyboardInterrupt:
            Exit()

    def wordlist(self):
        try:
            global wordlist_set
            global subdomain_list
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(subscan_banner)
            print(line)
            print('')
            print(author)
            print('Wordlist:')
            print('')
            print('\t1): 100 Words')
            print('\t2): 500 Words')
            print('\t3): 1000 Words')
            print('\t4): 10000 Words')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            while True:
                wordlist_set = input('\u001b[33mWORDLIST \u001b[37m> ').lower()
                if wordlist_set == '1':
                    subdomain_list = "subdomains-100.txt"
                    self.output()
                elif wordlist_set == '2':
                    subdomain_list = "subdomains-500.txt"
                    self.output()
                elif wordlist_set == '3':
                    subdomain_list = "subdomains-1000.txt"
                    self.output()
                elif wordlist_set == '4':
                    subdomain_list = "subdomains-10000.txt"
                    self.output()
                if wordlist_set == 'z':
                    Scanning()
                elif wordlist_set == 'x':
                    Exit()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            Exit()

    # Function that displays output
    def output(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(subscan_banner)
            print(line)
            print('')
            print(author)
            print('Output:')
            print('')
            print('\tControls')
            print('\t--------')
            print('\tStop: CTRL+C')
            print('')
            self.subsdomain_scan()
        except KeyboardInterrupt:
            Exit()

    # Function that scans subdomains
    def subsdomain_scan(self):
        try:
            global total_found
            total_found = 0

            # the domain to scan for subdomains
            domain = self.website_set

            # read all subdomains
            file = open("/opt/EagleShell/wordlists/subdomains/" + subdomain_list)
            # read all content
            content = file.read()
            # split by new lines
            subdomains = content.splitlines()

            for subdomain in subdomains:
                # construct the url
                url = f"http://{subdomain}.{domain}"
                try:
                    # if this raises an ERROR, that means the subdomain does not exist
                    requests.get(url)
                except requests.ConnectionError:
                    # if the subdomain does not exist, just pass, print nothing
                    pass
                else:
                    print("\t\u001b[33;1m[+] \u001b[32;1mDiscovered SubDomain \u001b[37;1m>> \u001b[36;1m" + str(url))
                    total_found = total_found + 1
        except KeyboardInterrupt:
            self.result()

    # Function that displays result
    def result(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(subscan_banner)
            print(line)
            print('')
            print(author)
            print('Result:')
            print('')
            print('\tInput')
            print('\t-----')
            print('\tWEBSITE: ' + self.website_set)
            print('\tWORDLIST: ' + subdomain_list)
            print('')
            print('\tOutput')
            print('\t------')
            print('\tSUBDOMAINS FOUND: ' + str(total_found))
            print('')
            print('\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit')
            print('')
            while True:
                eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                if eagleshell_cmd == 'y':
                    SubScan()
                elif eagleshell_cmd == 'z':
                    Scanning()
                elif eagleshell_cmd == 'x':
                    Exit()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            Exit()
