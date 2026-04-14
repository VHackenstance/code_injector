#!/usr/bin/env python3
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw
import re

new_line = "\n\n"

# Ensure HTML Request does not compress(encode) the HTML file.  regex return ACCEPT ENCODING Field
# if it is in load [Accept-Encoding:.*?\\r\\n]. NB: There are different formats for the
# encoding request.  Removing field from load prevents the encoding.
# THIS WAS GOOD FOR DEBUGGING BUT REDUNDANT NOW NEEDS REFACTOR, GOOD FOR LEARNING.
def remove_encode_request(packet, set_ld):
    pattern = "Accept-Encoding:.*?\\r\\n"
    load = packet[Raw].load
    if pattern in load:
        print("\n[+] We found an Accept-Encoding request in the packet.")
        load = re.sub(pattern, "", load)
        new_packet = set_ld(packet, load)
        print("[+] We are returning a new packet.\n")
        return new_packet
    else:
        print("\n[+] There is no Accept-Encoding request to modify!")
        print("[+] We are returning the original packet.\n")
        return packet

def set_load(packet, load):
    packet[Raw].load = load
    del packet[IP].len
    del packet[IP].chksum
    del packet[TCP].chksum
    return packet

