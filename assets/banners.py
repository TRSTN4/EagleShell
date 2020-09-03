#!/usr/bin/python3

from assets.properties import version, total_scripts, total_exploits, total_settings
from assets.colors import *

scripts_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Total] ' + str(total_scripts) + ' Scripts Available\n'
exploits_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Exploits | [Total] ' + str(total_exploits) + ' Listeners Available\n'
settings_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Settings | [Total] ' + str(total_settings) + ' Settings Available\n'

scanning_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning\n'
enumeration_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Enumeration\n'
exploitation_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation\n'
privilege_escalation_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Privilege Escalation\n'
brute_force_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force\n'
network_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network\n'
miscellaneous_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous\n'

netscan_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] NetScan\n'
portscan_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] PortScan\n'
subscan_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] SubScan\n'

rsgen_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] RSGEN\n'
machanger_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] MACHANGER\n'
pgen_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] PGEN\n'
arpspoof_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] ARPSPOOF\n'
packetsniffer_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] PACKETSNIFFER\n'
exif_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] EXIF\n'
crypt_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] CRYPT\n'
hashing_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] HASHING\n'
bruteftp_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTEFTP\n'
brutessh_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTESSH\n'

update_banner = YELLOW + '\n[Version] ' + version + ' | [Module] Settings | [Option] Update | [Script] Update\n'
setup_banner = YELLOW + '\n[Version] ' + version + ' | [Module] None | [Option] None | [Script] Setup\n'
