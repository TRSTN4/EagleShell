#!/usr/bin/python3

from assets.banners import network_banner
from assets.properties import clear_screen
from assets.designs import logo, line, author
from assets.shortcuts import Exit
from assets.prefixes import eagleshell_prefix, invalid_input
import os


class Network:
    def __init__(self):
        try:
            os.system(clear_screen)
            print(logo)
            print('')
            print(line)
            print(network_banner)
            print(line)
            print('')
            print(author)
            print('Scripts:')
            print('')
            print('\t1): ARPSPOOF - ARP Spoofer')
            print('\t2): PACKETSNIFFER - Packet Sniffer')
            print('\t3): Soon')
            print('')
            print('\tZ): Back')
            print('\tX): Exit')
            print('')
            while True:
                network_select = input(eagleshell_prefix).lower()
                if network_select == '1':
                    from modules.scripts.network.arpspoof import arpspoof_main
                    arpspoof_main()
                elif network_select == '2':
                    from modules.scripts.network.packetsniff import packetsniff_main
                    packetsniff_main()
                elif network_select == '3':
                    pass
                elif network_select == 'z':
                    from ..scripts import Scripts
                    Scripts()
                elif network_select == 'x':
                    Exit()
                else:
                    print(invalid_input)
                    continue
        except KeyboardInterrupt:
            Exit()
