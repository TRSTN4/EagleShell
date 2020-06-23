#!/usr/bin/python3

# SubScan - Sub Domain Scanner Script

# Imports all needed variables and packages
from assets.banners import subscan_banner
from assets.designs import *
from assets.properties import clear_screen
from eagleshell import eagleshell_main
import requests
import os

# Main Function
def subscan_main():

    # Function that takes input
    def configuration():
        try:
            global website_set
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
            website_set = input('\u001b[33mWEBSITE \u001b[37m> ').lower()
            if website_set == 'z':
                eagleshell_main()
            elif website_set == 'x':
                exit_shell()
            wordlist()
        except KeyboardInterrupt:
            exit_shell()

    # Function that sets wordlist
    def wordlist():
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
                    output()
                elif wordlist_set == '2':
                    subdomain_list = "subdomains-500.txt"
                    output()
                elif wordlist_set == '3':
                    subdomain_list = "subdomains-1000.txt"
                    output()
                elif wordlist_set == '4':
                    subdomain_list = "subdomains-10000.txt"
                    output()
                if wordlist_set == 'z':
                    subscan_main()
                elif wordlist_set == 'x':
                    exit_shell()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    # Function that displays output
    def output():
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
            subsdomain_scan()
        except KeyboardInterrupt:
            exit_shell()

    # Function that scans subdomains
    def subsdomain_scan():
        try:
            global total_found
            total_found = 0

            # the domain to scan for subdomains
            domain = website_set

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
            result()

    # Function that displays result
    def result():
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
            print('\tWEBSITE: ' + website_set)
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
                    subscan_main()
                elif eagleshell_cmd == 'z':
                    eagleshell_main()
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


subscan_main()
