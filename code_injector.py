#!/usr/bin/env python3
# Rebuild
# We are testing here online against either of OWASP Juice Shop, or Vulnweb
# http://juice-shop.herokuapp.com/#/  or http://testasp.vulnweb.com/
# Let me state clearly, both these sites as designated af freely hackable sites.
import netfilterqueue
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw
import re

AcceptEncodingRegex = "Accept-Encoding:.*?\\r\\n"

# Take our modified load and set it to the packet load
def set_load(packet, load):
    packet[Raw].load = load
    # For scapy to recalculate IP and Chksum for updated load, delete them
    del packet[IP].len
    del packet[IP].chksum
    del packet[TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw):
        if scapy_packet.haslayer(TCP):
            # print("\n[+] Packet has layer TCP")
            if scapy_packet[TCP].dport == 80:
                print("[+] This is a HTTP Request:  ")
                # Find string "Accept-Encoding" in the payload of HTTP Request Raw layer
                # replace with nothing, and save in modified_load
                modified_load = re.sub(AcceptEncodingRegex, "", scapy_packet[Raw].load)
                new_packet = set_load(scapy_packet, modified_load)
                # set the new packet with the updated payload to the actual packet
                packet.set_payload(str(new_packet))
            # After testing the above, we should get nothing but clean HTML page markup
            # in the payload.
            elif scapy_packet[TCP].sport == 80:
                print("[+] This is a HTTP Response: ")
                print(scapy_packet.show())

    packet.accept()


if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(2, process_packet)
    queue.run()
