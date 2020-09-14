#!/usr/bin/python3

import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


class IMGExtract:
    def is_valid(url):
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)


def get_all_images(url):
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
        if is_valid(img_url):
            urls.append(img_url)
    return urls


def download(url, pathname):
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


def main(url, path):
    imgs = get_all_images(url)
    for img in imgs:
        download(img, path)



if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="This script downloads all images from a web page")
    parser.add_argument("url", help="The URL of the web page you want to download images")
    parser.add_argument("-p", "--path", help="The Directory you want to store your images, default is the domain of URL passed")

    args = parser.parse_args()
    url = args.url
    path = args.path

    if not path:
        path = urlparse(url).netloc

    main(url, path)
