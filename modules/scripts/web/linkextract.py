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

internal_urls = set()
external_urls = set()
total_urls_visited = 0


class LinkExtract:
    def __init__(self):
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
            print('\tExample: http://mysite.com')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.url_set = input(url_prefix)
            if self.url_set == 'z' or self.url_set == 'Z':
                Web()
            elif self.url_set == 'x' or self.url_set == 'X':
                Exit()
            self.crawl(self.url_set)
            self.result()
        except KeyboardInterrupt:
            Exit()

    def crawl(self, url, max_urls=50):
        self.total_urls_visited += 1
        links = self.get_all_website_links(url)
        for link in links:
            if self.total_urls_visited > max_urls:
                break
            self.crawl(link, max_urls=max_urls)

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
                if href in internal_urls:
                    continue
                if domain_name not in href:
                    if href not in external_urls:
                        print(MAGENTA + f"[!] External link: {href}" + WHITE)
                        external_urls.add(href)
                    continue
                print(GREEN + f"[*] Internal link: {href}" + WHITE)
                urls.add(href)
                internal_urls.add(href)
            return urls
        except KeyboardInterrupt:
            Exit()

    def is_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def result(self):
        try:
            self.header()
            print('Result:')
            print("\n[+] Total Internal links:", len(internal_urls))
            print("[+] Total External links:", len(external_urls))
            print("[+] Total URLs:", len(external_urls) + len(internal_urls))
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
