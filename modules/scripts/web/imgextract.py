#!/usr/bin/python3

from assets.headers import imgextract_header
from assets.colors import *
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, url_prefix, path_prefix, unable_to_connect_prefix
from assets.shortcuts import Exit
from .web import Web
import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


class IMGExtract:
    def __init__(self):
        self.total_downloads = 0
        self.configuration()
        imgs = self.get_all_images(self.url_set)
        for img in imgs:
            self.download(img, self.path_set)
            self.total_downloads = self.total_downloads + 1
        self.result()

    def configuration(self):
        try:
            imgextract_header()
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
            imgextract_header()
            print('Configuration:')
            print('\n\tChoose Storage Path')
            print('\tExample: /opt/img/')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.path_set = input(path_prefix)
            if self.path_set == 'z' or self.path_set == 'Z':
                Web()
            elif self.path_set == 'x' or self.path_set == 'X':
                Exit()
        except KeyboardInterrupt:
            Exit()

    def get_all_images(self, url):
        try:
            imgextract_header()
            print('Output:')
            print('\n\tControls')
            print('\t--------')
            print('\tStop: CTRL+C\n')
            soup = bs(requests.get(url).content, "html.parser")
            urls = []
            for img in tqdm(soup.find_all("img"), "Extracting images"):
                img_url = img.attrs.get("src")
                if not img_url:
                    continue
                img_url = urljoin(url, img_url)
                try:
                    pos = img_url.index("?")
                    img_url = img_url[:pos]
                except ValueError:
                    pass
                if self.is_valid(img_url):
                    urls.append(img_url)
            return urls
        except requests.exceptions.ConnectionError:
            print(unable_to_connect_prefix)
            os.system('sleep 1.5')
            IMGExtract()
        except KeyboardInterrupt:
            self.result()

    def is_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def download(self, url, pathname):
        try:
            if not os.path.isdir(pathname):
                os.makedirs(pathname)
            response = requests.get(url, stream=True)
            file_size = int(response.headers.get("Content-Length", 0))
            filename = os.path.join(pathname, url.split("/")[-1])
            progress = tqdm(response.iter_content(1024), f"[+] Downloading: {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
            with open(filename, "wb") as f:
                for data in progress:
                    f.write(data)
                    progress.update(len(data))
        except KeyboardInterrupt:
            self.result()

    def result(self):
        try:
            imgextract_header()
            print('Result:')
            print(WHITE + "\n\tTotal Images Downloaded: " + GREEN + str(self.total_downloads) + WHITE)
            print(WHITE + "\n\tURL Set: " + GREEN + str(self.url_set) + WHITE)
            print(WHITE + "\tPATH Set: " + GREEN + str(self.path_set) + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    IMGExtract()
                elif cmd == 'z':
                    Web()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
