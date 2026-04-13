#!/usr/bin/env python3
import netfilterqueue
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw

new_line = "\n\n"
def set_load(packet, load):
    packet[Raw].load = load
    del packet[IP].len
    del packet[IP].chksum
    del packet[TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw) and scapy_packet.haslayer(TCP):
        if scapy_packet[TCP].dport == 80:
            print("[+] This is an HTTP Request: ")
            print(scapy_packet.show())
        elif scapy_packet[TCP].sport == 80:
            print("This is a *** HTTP Response ***: ")
            print(scapy_packet.show())
    packet.accept()
    return None

print("Hello World, this is Code Injector")
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()