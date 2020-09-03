#!/usr/bin/python3

from assets.properties import version, total_scripts, total_exploits, total_settings
from assets.colors import *

scripts_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Total] ' + str(total_scripts) + ' Scripts Available'
exploits_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Exploits | [Total] ' + str(total_exploits) + ' Listeners Available'
settings_banner = YELLOW + '[Version] ' + version + ' | [Module] Settings | [Total] ' + str(total_settings) + ' Settings Available'

scanning_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning'
enumeration_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Enumeration'
exploitation_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation'
privilege_escalation_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Privilege Escalation'
brute_force_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force'
network_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network'
miscellaneous_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous'

netscan_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] NetScan'
portscan_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] PortScan'
subscan_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] SubScan'

rsgen_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] RSGEN'
machanger_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] MACHANGER'
pgen_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] PGEN'
update_banner = YELLOW + '[Version] ' + version + ' | [Module] Settings | [Option] Update | [Script] UPDATE'
setup_banner = YELLOW + '[Version] ' + version + ' | [Module] None | [Option] None | [Script] Setup'
arpspoof_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] ARPSPOOF'
packetsniffer_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] PACKETSNIFFER'
exif_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] EXIF'
crypt_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] CRYPT'
hashing_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] HASHING'
bruteftp_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTEFTP'
brutessh_banner = YELLOW + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTESSH'
