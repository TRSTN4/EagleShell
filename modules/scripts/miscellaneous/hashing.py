#!/usr/bin/python3

# RSGen Reverse Shell Generator Script

# Imports all variables and packages
from assets.banners import hashing_banner
from assets.designs import *
from assets.properties import clear_screen
import hashlib
import os


def hashing_main():

    # Function that takes some user input
    def configuration():
        try:
            global hashing_set
            global hash_type_set
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(hashing_banner)
            print(line)
            print('')
            print(author)
            print('Configuration:')
            print('')
            print('\t1): Text Hashing')
            print('\t2): File Hashing')
            print('')
            while True:
                hashing_set = input('\u001b[33mHASHING \u001b[37m> ').lower()
                if hashing_set == '1':
                    hashing_text()
                elif hashing_set == '2':
                    hashing_files()
                else:
                    print('\u001b[31m[-] Invalid Input.')
                    continue
        except KeyboardInterrupt:
            exit_shell()

    #
    def hashing_text():

        #
        def set_text_hash_input():
            try:
                global hashing_text_set
                os.system(clear_screen)
                print(logo)
                print('')
                print(line)
                print(hashing_banner)
                print(line)
                print('')
                print(author)
                print('Input:')
                print('')
                print('\tPaste Your Text')
                print('\tExample: SomeRandomText123')
                print('')
                hashing_text_set = input('\u001b[33mTEXT \u001b[37m> ')
                hash_txt_process()
            except KeyboardInterrupt:
                exit_shell()

        #
        def hash_txt_process():
            try:
                # encode it to bytes using UTF-8 encoding
                global message
                message = hashing_text_set.encode()

                result_text_hashing()
            except KeyboardInterrupt:
                exit_shell()

        def result_text_hashing():
            try:
                os.system(clear_screen)
                print(logo)
                print('')
                print(line)
                print(hashing_banner)
                print(line)
                print('')
                print(author)
                print('Output:')
                print('')
                print('\tTEXT SET: ' + str(hashing_text_set))
                print('')
                # hash with MD5 (not recommended)
                print("\t\u001b[31mMD5:", hashlib.md5(message).hexdigest())
                # hash with SHA-2 (SHA-256 & SHA-512)
                print("\t\u001b[32mSHA-256:", hashlib.sha256(message).hexdigest())
                print("\t\u001b[33mSHA-512:", hashlib.sha512(message).hexdigest())
                # hash with SHA-3
                print("\t\u001b[34mSHA-3-256:", hashlib.sha3_256(message).hexdigest())
                print("\t\u001b[35mSHA-3-512:", hashlib.sha3_512(message).hexdigest())
                # hash with BLAKE2
                # 256-bit BLAKE2 (or BLAKE2s)
                print("\t\u001b[36mBLAKE2c:", hashlib.blake2s(message).hexdigest())
                # 512-bit BLAKE2 (or BLAKE2b)
                print("\t\u001b[36mBLAKE2b:", hashlib.blake2b(message).hexdigest())
                print('\u001b[37m')
                print('\t1): New')
                print('\t2): Exit')
                print('')
                while True:
                    eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                    if eagleshell_cmd == '1':
                        hashing_main()
                    elif eagleshell_cmd == '2':
                        exit_shell()
                    else:
                        print('\u001b[31m[-] Invalid Input.')
                        continue
            except KeyboardInterrupt:
                exit_shell()

        set_text_hash_input()

    #
    def hashing_files():

        #
        def set_file_hash_input():
            try:
                global hashing_file_path
                os.system(clear_screen)
                print(logo)
                print('')
                print(line)
                print(hashing_banner)
                print(line)
                print('')
                print(author)
                print('Input:')
                print('')
                print('\tInput File Path')
                print('\tExample: /tmp/images/car.jpeg')
                print('')
                hashing_file_path = input('\u001b[33mPATH \u001b[37m> ')
                file_hashing()
            except KeyboardInterrupt:
                exit_shell()
            except FileNotFoundError:
                print('\u001b[31m[-] Invalid Input.')
                os.system('sleep 2')
                set_file_hash_input()
            except IsADirectoryError:
                print('\u001b[31m[-] Invalid Input.')
                os.system('sleep 2')
                set_file_hash_input()

        def read_file(file):
            try:
                """Reads an entire file and returns file bytes."""
                BUFFER_SIZE = 16384 # 16 kilo bytes
                b = b""
                with open(file, "rb") as f:
                    while True:
                        # read 16K bytes from the file
                        bytes_read = f.read(BUFFER_SIZE)
                        if bytes_read:
                            # if there is bytes, append them
                            b += bytes_read
                        else:
                            # if not, nothing to do here, break out of the loop
                            break
                return b
            except KeyboardInterrupt:
                exit_shell()

        def file_hashing():
            try:
                global file_content
                # read some file
                file_content = read_file(hashing_file_path)
                result_file_hashing()
            except KeyboardInterrupt:
                exit_shell()

        def result_file_hashing():
            try:
                os.system(clear_screen)
                print(logo)
                print('')
                print(line)
                print(hashing_banner)
                print(line)
                print('')
                print(author)
                print('Output:')
                print('')
                print('\tFILE SET: ' + hashing_file_path)
                print('')
                # some chksums:
                # hash with MD5 (not recommended)
                print("\t\u001b[31mMD5:", hashlib.md5(file_content).hexdigest())
                # hash with SHA-2 (SHA-256 & SHA-512)
                print("\t\u001b[32mSHA-256:", hashlib.sha256(file_content).hexdigest())
                print("\t\u001b[33mSHA-512:", hashlib.sha512(file_content).hexdigest())
                # hash with SHA-3
                print("\t\u001b[34mSHA-3-256:", hashlib.sha3_256(file_content).hexdigest())
                print("\t\u001b[35mSHA-3-512:", hashlib.sha3_512(file_content).hexdigest())
                # hash with BLAKE2
                # 256-bit BLAKE2 (or BLAKE2s)
                print("\t\u001b[36mBLAKE2c:", hashlib.blake2s(file_content).hexdigest())
                # 512-bit BLAKE2 (or BLAKE2b)
                print("\t\u001b[36mBLAKE2b:", hashlib.blake2b(file_content).hexdigest())
                print('\u001b[37m')
                print('\t1): New')
                print('\t2): Exit')
                print('')
                while True:
                    eagleshell_cmd = input('\u001b[33mEagleShell \u001b[37m> ').lower()
                    if eagleshell_cmd == '1':
                        hashing_main()
                    elif eagleshell_cmd == '2':
                        exit_shell()
                    else:
                        print('\u001b[31m[-] Invalid Input.')
                        continue
            except KeyboardInterrupt:
                exit_shell()

        set_file_hash_input()

    # The function where you exit
    def exit_shell():
        from assets.functions import exit_main
        exit_main()

    configuration()


hashing_main()
