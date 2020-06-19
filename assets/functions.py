#!/usr/bin/python3

# Imports all needed variables and packages
from assets.properties import clear_screen
import os


# Functions that are used a lot.
def exit_main():
    print('\n\u001b[31m[-] Exiting EagleShell')
    print('\u001b[0m')
    os.system(clear_screen)
    exit()
