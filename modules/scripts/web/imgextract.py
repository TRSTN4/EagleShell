#!/usr/bin/python3

from assets.headers import imgextract_header
from assets.colors import *
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, url_prefix, path_prefix
from assets.shortcuts import Exit
from .web import Web
import os
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


class IMGExtract:
    def __init__(self):
        self.configuration()
        self.main()

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

    def main(self):
        imgs = self.get_all_images(self.url_set)
        for img in imgs:
            self.download(img, self.path_set)

    def get_all_images(self, url):
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

    def is_valid(self, url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def download(self, url, pathname):
        if not os.path.isdir(pathname):
            os.makedirs(pathname)
        response = requests.get(url, stream=True)

        file_size = int(response.headers.get("Content-Length", 0))

        filename = os.path.join(pathname, url.split("/")[-1])

        progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            for data in progress:
                f.write(data)
                progress.update(len(data))
