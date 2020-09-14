#!/usr/bin/python3

from assets.headers import hashing_header
from assets.colors import *
from assets.prefixes import invalid_input_prefix, eagleshell_prefix, hashing_prefix, text_prefix, path_prefix
from assets.shortcuts import Exit
from modules.scripts.miscellaneous.miscellaneous import Miscellaneous
import os
import hashlib


class Hashing:
    def __init__(self):
        self.configuration()

    def configuration(self):
        try:
            hashing_header()
            print('Configuration:')
            print('\n\t1): Text Hashing')
            print('\t2): File Hashing')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            while True:
                hashing_set = input(hashing_prefix).lower()
                if hashing_set == '1':
                    self.text_hashing()
                elif hashing_set == '2':
                    self.file_hashing_input()
                elif hashing_set == 'z':
                    Miscellaneous()
                elif hashing_set == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()

    def text_hashing(self):
        try:
            hashing_header()
            print('Input:')
            print('\n\tType Your Text')
            print('\tExample: SomeRandomText123')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.hashing_text_set = input(text_prefix)
            if self.hashing_text_set == 'z' or self.hashing_text_set == 'Z':
                Miscellaneous()
            elif self.hashing_text_set == 'x' or self.hashing_text_set == 'X':
                Exit()
            else:
                self.message = self.hashing_text_set.encode()
                self.result_text()
        except KeyboardInterrupt:
            Exit()

    def result_text(self):
        try:
            hashing_header()
            print('Output:')
            print('\n\tText Input: ' + str(self.hashing_text_set) + '\n')
            print(RED + "\tMD5:", hashlib.md5(self.message).hexdigest())
            print(GREEN + "\tSHA-256:", hashlib.sha256(self.message).hexdigest())
            print(YELLOW + "\tSHA-512:", hashlib.sha512(self.message).hexdigest())
            print(BLUE + "\tSHA-3-256:", hashlib.sha3_256(self.message).hexdigest())
            print(MAGENTA + "\tSHA-3-512:", hashlib.sha3_512(self.message).hexdigest())
            print(CYAN + "\tBLAKE2c:", hashlib.blake2s(self.message).hexdigest())
            print(CYAN + "\tBLAKE2b:", hashlib.blake2b(self.message).hexdigest() + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    Hashing()
                elif cmd == 'z':
                    Miscellaneous()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()

    def file_hashing_input(self):
        try:
            hashing_header()
            print('Input:')
            print('\n\tFile Path')
            print('\tExample: /tmp/images/car.jpeg')
            print('\n\tZ): Back')
            print('\tX): Exit\n')
            self.hashing_file_path = input(path_prefix)
            if self.hashing_file_path == 'z' or self.hashing_file_path == 'Z':
                Miscellaneous()
            elif self.hashing_file_path == 'x' or self.hashing_file_path == 'X':
                Exit()
            else:
                self.hashing_file()
                self.result_file()
        except KeyboardInterrupt:
            Exit()
        except FileNotFoundError:
            print(invalid_input_prefix)
            os.system('sleep 1')
            self.file_hashing_input()
        except IsADirectoryError:
            print(invalid_input_prefix)
            os.system('sleep 1')
            self.file_hashing_input()

    def hashing_file(self):
        try:
            buff_size = 16384
            self.hashed_file = b""
            with open(self.hashing_file_path, "rb") as f:
                while True:
                    bytes_read = f.read(buff_size)
                    if bytes_read:
                        self.hashed_file += bytes_read
                    else:
                        break
        except KeyboardInterrupt:
            Exit()

    def result_file(self):
        try:
            hashing_header()
            print('Output:')
            print('\n\tFile Input: ' + self.hashing_file_path + '\n')
            print(RED + "\tMD5:", hashlib.md5(self.hashed_file).hexdigest())
            print(GREEN + "\tSHA-256:", hashlib.sha256(self.hashed_file).hexdigest())
            print(YELLOW + "\tSHA-512:", hashlib.sha512(self.hashed_file).hexdigest())
            print(BLUE + "\tSHA-3-256:", hashlib.sha3_256(self.hashed_file).hexdigest())
            print(MAGENTA + "\tSHA-3-512:", hashlib.sha3_512(self.hashed_file).hexdigest())
            print(CYAN + "\tBLAKE2c:", hashlib.blake2s(self.hashed_file).hexdigest())
            print(CYAN + "\tBLAKE2b:", hashlib.blake2b(self.hashed_file).hexdigest() + WHITE)
            print('\n\tY): New')
            print('\tZ): Menu')
            print('\tX): Exit\n')
            while True:
                cmd = input(eagleshell_prefix).lower()
                if cmd == 'y':
                    Hashing()
                elif cmd == 'z':
                    Miscellaneous()
                elif cmd == 'x':
                    Exit()
                else:
                    print(invalid_input_prefix)
                    continue
        except KeyboardInterrupt:
            Exit()
