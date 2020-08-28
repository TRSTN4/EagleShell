#!/usr/bin/python3

# Imports all the needed variables
from assets.properties import version
from assets.properties import total_scripts
from assets.colors import *

# Banner Variables
payloads_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Payloads | [Total] 0 Payloads Available'
listeners_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Listeners | [Total] 0 Listeners Available'
scripts_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Total] ' + total_scripts +' Scripts Available'
settings_banner = CYAN + '[Version] ' + version + ' | [Module] Settings | [Total] 0 Settings Available'
scanning_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning'
enumeration_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Enumeration'
network_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network'
privilege_escalation_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Privilege Escalation'
exploitation_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation'
brute_force_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force'
miscellaneous_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous'
rsgen_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] RSGEN'
machanger_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] MACHANGER'
eagleye_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] EAGLEYE'
eaglscan_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] EAGLESCAN'
pgen_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] PGEN'
update_banner = CYAN + '[Version] ' + version + ' | [Module] Settings | [Option] Update | [Script] UPDATE'
setup_banner = CYAN + '[Version] ' + version + ' | [Module] None | [Option] None | [Script] SETUP'
arpspoof_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] ARPSPOOF'
packetsniffer_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] PACKETSNIFFER'
subscan_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] SUBSCAN'
exif_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] EXIF'
crypt_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] CRYPT'
hashing_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] HASHING'
bruteftp_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTEFTP'
brutessh_banner = CYAN + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTESSH'
