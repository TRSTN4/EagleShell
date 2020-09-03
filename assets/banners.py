#!/usr/bin/python3

from assets.properties import version, total_scripts, total_exploits, total_settings
from assets.colors import *

line = YELLOW + '==================================================================================='

scripts_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Total] ' + str(total_scripts) + ' Scripts Available' + '\n' + line
exploits_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Exploits | [Total] ' + str(total_exploits) + ' Listeners Available' + '\n' + line
settings_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Settings | [Total] ' + str(total_settings) + ' Settings Available' + '\n' + line

scanning_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning' + '\n' + line
enumeration_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Enumeration' + '\n' + line
exploitation_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation' + '\n' + line
privilege_escalation_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Privilege Escalation' + '\n' + line
brute_force_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force' + '\n' + line
network_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network' + '\n' + line
miscellaneous_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous' + '\n' + line

netscan_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] NetScan' + '\n' + line
portscan_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] PortScan' + '\n' + line
subscan_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Scanning | [Script] SubScan' + '\n' + line

rsgen_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] RSGEN' + '\n' + line
machanger_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] MACHANGER' + '\n' + line
pgen_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Exploitation | [Script] PGEN' + '\n' + line
update_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Settings | [Option] Update | [Script] UPDATE' + '\n' + line
setup_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] None | [Option] None | [Script] Setup' + '\n' + line
arpspoof_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] ARPSPOOF' + '\n' + line
packetsniffer_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Network | [Script] PACKETSNIFFER' + '\n' + line
exif_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] EXIF' + '\n' + line
crypt_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] CRYPT' + '\n' + line
hashing_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Miscellaneous | [Script] HASHING' + '\n' + line
bruteftp_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTEFTP' + '\n' + line
brutessh_banner = YELLOW + '\n' + line + '[Version] ' + version + ' | [Module] Eagle Scripts | [Option] Brute Force | [Script] BRUTESSH' + '\n' + line
