#!/usr/bin/python3

from assets.properties import clear_screen

import os


def exit_main():
    print('\n\u001b[31m[-] Exiting EagleShell')
    print('\u001b[0m')
    os.system(clear_screen)
    exit()
