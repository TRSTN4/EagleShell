#!/usr/bin/python3

from assets.banners import linkextract_banner
from assets.colors import *
from assets.designs import logo, author
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, url_prefix
from assets.properties import clear_screen
from assets.shortcuts import Exit
from .web import Web
import os
import requests
from urllib.request import urlparse, urljoin
from bs4 import BeautifulSoup


class LinkExtract:
    def __init__(self):
        self.internal_urls = set()
        self.external_urls = set()
        self.total_urls_visited = 0
        self.configuration()
        self.result()

    def header(self):
        os.system(clear_screen)
        print(logo)
        print(linkextract_banner)
        print(author)

    def configuration(self):
        try:
            self.header()
            print('Configuration:')
            print('\n\tPaste Your URL')
            print('\tExample 1: http://mysite.com')
            print('\tExample 2: mysite.com')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.url_set = input(url_prefix)
            if self.url_set == 'z' or self.url_set == 'Z':
                Web()
            elif self.url_set == 'x' or self.url_set == 'X':
                Exit()
            if 'http://' in self.url_set or 'https://' in self.url_set:
                pass
            else:
                self.url_set = 'http://' + self.url_set
            self.header()
            print('Output:')
            print('\n\tControls')
            print('\t--------')
            print('\tStop: CTRL+C\n')
            self.crawl(self.url_set)
            self.result()
        except KeyboardInterrupt:
            Exit()

    def crawl(self, url, max_urls=50):
        try:
            self.total_urls_visited += 1
            links = self.get_all_website_links(url)
            for link in links:
                if self.total_urls_visited > max_urls:
                    break
                self.crawl(link, max_urls=max_urls)
        except requests.exceptions.ConnectionError:
            print(RED + "\n\t[-] URL does not exist." + WHITE)
            os.system('sleep 2')
            LinkExtract()

    def get_all_website_links(self, url):
        try:
            urls = set()
            domain_name = urlparse(url).netloc
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
            for a_tag in soup.findAll("a"):
                href = a_tag.attrs.get("href")
                if href == "" or href is None:
                    continue
                href = urljoin(url, href)
                parsed_href = urlparse(href)
                href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
                if not self.is_valid(href):
                    continue
                if href in self.internal_urls:
                    continue
                if domain_name not in href:
                    if href not in self.external_urls:
                        print(YELLOW + '\t[!] ' + MAGENTA + 'External Link Found ' + WHITE + '>> ' + BLUE + f"{href}" + WHITE)
                        self.external_urls.add(href)
                    continue
                print(YELLOW + '\t[+] ' + GREEN + 'Internal Link Found ' + WHITE + '>> ' + BLUE + f"{href}" + WHITE)
                urls.add(href)
                self.internal_urls.add(href)
            return urls
        except KeyboardInterrupt:
            self.result()

    def is_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def result(self):
        try:
            self.header()
            print('Result:')
            print(GREEN, "\n\tTotal Internal Links:", len(self.internal_urls), WHITE)
            print(MAGENTA, "\tTotal External Links:", len(self.external_urls), WHITE)
            print(BLUE, "\tTotal URLs:", len(self.external_urls) + len(self.internal_urls), WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    LinkExtract()
                elif cmd == 'z':
                    Web()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
