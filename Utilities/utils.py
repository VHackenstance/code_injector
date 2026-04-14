#!/usr/bin/env python3
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw

new_line = "\n\n"

def set_load(packet, load):
    packet[Raw].load = load
    del packet[IP].len
    del packet[IP].chksum
    del packet[TCP].chksum
    return packet

