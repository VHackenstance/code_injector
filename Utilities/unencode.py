#!/usr/bin/env python3
from scapy.layers.dns import Raw
import re

# Stop HTML Request from encoding HTML file.  regex fine ACCEPT ENCODING Field
# in load [Accept-Encoding:.*?\\r\\n]. NB: There are different formats.
# Removing field from load prevents the encoding.
# GOOD FOR DEBUGGING BUT REDUNDANT NOW NEEDS REFACTOR. GOOD FOR LEARNING.
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

def content_length():
    print("\n[+] We are returning the length of the packet.\n")