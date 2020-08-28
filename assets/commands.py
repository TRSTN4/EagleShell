#!/usr/bin/python3

from assets.properties import version


class HelpCMD:
    def __init__(self):
        print('''
    Core Commands
    =============
    
        Command       Description
        -------       -----------
        ?             Help menu
        help          Help menu
        exit          Exit the console
        quit          Exit the console
        version       Show the framework and console library version numbers
    
    =============
    ''')


class VersionCMD:
    def __init__(self):
        print('Framework: ' + version)
        print('Console: ' + version)
