#!/usr/bin/python3

from assets.properties import version, total_scripts, total_exploits, total_settings
from assets.colors import *

scripts_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Total] ' + str(total_scripts) + ' Scripts Available'
exploits_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Exploits | [Total] ' + str(total_exploits) + ' Listeners Available'
settings_banner = CYAN + '[Version] ' + version + ' | [Module] Settings | [Total] ' + str(total_settings) + ' Settings Available'

scanning_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning'
enumeration_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Enumeration'
exploitation_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation'
privilege_escalation_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Privilege Escalation'
brute_force_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force'
network_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network'
miscellaneous_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous'

netscan_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] NetScan'
portscan_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] PortScan'
subscan_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] SubScan'

rsgen_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] RSGEN'
machanger_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] MACHANGER'
pgen_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] PGEN'
update_banner = CYAN + '[Version] ' + version + ' | [Module] Settings | [Option] Update | [Script] UPDATE'
setup_banner = CYAN + '[Version] ' + version + ' | [Module] None | [Option] None | [Script] Setup'
arpspoof_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] ARPSPOOF'
packetsniffer_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] PACKETSNIFFER'
exif_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] EXIF'
crypt_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] CRYPT'
hashing_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] HASHING'
bruteftp_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTEFTP'
brutessh_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTESSH'
