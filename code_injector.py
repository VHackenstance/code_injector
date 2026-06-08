#!/usr/bin/env python3
# Rebuild
import netfilterqueue
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw

import re

AcceptEncodingRegex = "Accept-Encoding:.*?\\r\\n"

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw):
        if scapy_packet.haslayer(TCP):
            # print("\n[+] Packet has layer TCP")
            if scapy_packet[TCP].dport == 80:
                print("[+] This is a HTTP Request:  ")
                print("[+] This is our current load with Accept Encoding:  ")
                print(scapy_packet[Raw].load)
                # Find string Accept-Encoding in HTTPR Raw layer load
                # replace with nothing and as as modified_load
                modified_load = re.sub(AcceptEncodingRegex, "", scapy_packet[Raw].load)
                print("[+] Load minus the Accept Encoding:  ")
                print(modified_load)

            # elif scapy_packet[TCP].sport == 80:
                # print("[+] This is a HTTP Response: ")

    packet.accept()


if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
