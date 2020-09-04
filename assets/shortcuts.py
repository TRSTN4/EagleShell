#!/usr/bin/python3

from assets.properties import clear_screen
from assets.colors import *
import os


class Exit:
    def __init__(self):
        print(RED + '\n[-] Exiting EagleShell')
        print(RESET)
        os.system('sleep 1')
        os.system(clear_screen)
        exit()
