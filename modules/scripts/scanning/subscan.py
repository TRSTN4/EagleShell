#!/usr/bin/python3

# Imports all needed variables and packages
from assets.banners import subscan_banner
from assets.designs import *
from assets.properties import clear_screen
import requests
import os

def subscan_main():

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
            website_set = input('\u001b[33mWEBSITE \u001b[37m> ').lower()
            wordlist()
        except KeyboardInterrupt:
            exit_shell()

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
            print('Configuration:')
            print('')
            print('\tExample: google.com')
            print('')
            while True:
                wordlist_set = input('\u001b[33mWEBSITE \u001b[37m> ').lower()
                if wordlist_set == '1':
                    os.system('cd wordlists/subdomains/')
                    subdomain_list = "subdomains-100.txt"
                elif wordlist_set == '2':
                elif wordlist_set == '3':
                elif wordlist_set == '4':
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue

            subsdomain_scan()
        except KeyboardInterrupt:
            exit_shell()

    def subsdomain_scan():
        # the domain to scan for subdomains
        domain = website_set

        # read all subdomains
        file = open(subdomain_list)
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
                print("[+] Discovered SubDomain: " + url)

    # The function where you exit
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


subscan_main()
