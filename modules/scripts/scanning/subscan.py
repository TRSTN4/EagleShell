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
            subsdomain_scan()
        except KeyboardInterrupt:
            exit_shell()

    def subsdomain_scan():
        # the domain to scan for subdomains
        domain = website_set

        # read all subdomains
        file = open("subdomains.txt")
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
