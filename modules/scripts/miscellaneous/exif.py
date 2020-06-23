#!/usr/bin/python3

# Exif Extract Image Metadata Script

# Imports all variables and packages
from assets.banners import exif_banner
from assets.banners import exif_banner
from assets.designs import *
from assets.properties import clear_screen
import os
from PIL import Image
from PIL.ExifTags import TAGS


def exif_main():

    def configuration():
        try:
            global image_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(exif_banner)
            print(line)
            print('')
            print(author)
            print('Configuration:')
            print('')
            print('\tINFO:')
            print('\t-----')
            print('\tSupported Extensions:')
            print('\t".jpg", ".jpeg"')
            print('')
            print('\tInput:')
            print('\t------')
            print('\tInput Path To Image Location')
            print('\tExample: /tmp/images/puppy.jpg')
            print('')
            image_set = input('\u001b[33mIMAGE \u001b[37m> ').lower()
            extractor()
        except KeyboardInterrupt:
            exit_shell()


    def extractor():
        # path to the image
        imagename = image_set

        # read the image data using PIL
        image = Image.open(imagename)

        # extract EXIF data
        exifdata = image.getexif()

        # iterating over all EXIF data fields
        for tag_id in exifdata:
            # get the tag name, instead of human unreadable tag id
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            # decode bytes
            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:25}: {data}")

    # The function where you exit
    def exit_shell():
        from assets.functions import exit_main
        exit_main()
