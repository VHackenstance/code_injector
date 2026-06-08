#!/usr/bin/env python3
# Rebuild - Separate Script for testing with OWASP Juice Shop which I think is Https
# We are testing here locally against OWASP Juice Shop
# http://127.0.0.1:42000/#/
import netfilterqueue
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw
import re

# Take our modified load and set it to the actual load
def set_load(packet, load):
    packet[Raw].load = load
    # For scapy to recalculate IP and Chksum values for our updated load
    # You need to delete them
    del packet[IP].len
    del packet[IP].chksum
    del packet[TCP].chksum
    return packet

# Payload has: Accept-Encoding\r\nContent-Encoding: gzip\r\n
# The following Regex should also work here.
AcceptEncodingRegex = "Accept-Encoding:.*?\\r\\n"

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw):
        if scapy_packet.haslayer(TCP):
            # print("\n[+] Packet has layer TCP")
            # print(scapy_packet.show())
            if scapy_packet[TCP].dport == 443:
                print("[+] This is a HTTP Request on port 443:  ")
                if "Accept-Encoding" in scapy_packet[Raw].load:
                    print("[+] Accept Encoding in Payload:  ")
                    print(scapy_packet[Raw].load)
            elif scapy_packet[TCP].dport == 55114:
                print("[+] This is a HTTP Request on port 55114:  ")
            elif scapy_packet[TCP].dport == 42000:
                print("[+] This is a HTTP Request on port 42000: ")
                if "Accept-Encoding" in scapy_packet[Raw].load:
                    print("[+] Accept Encoding in Payload:  ")
                    print(scapy_packet[Raw].load)

            # TODO ************************
            #  Write a loop to cycle through ports
            #   How about autodect ports being used for HTTP traffic
            #   Do the same things as here for replace_download
            #    The actual idea would be to have scripts adaptable to any scenerio
            # END TODO ********************

                # Find string "Accept-Encoding" in the payload of HTTP Request Raw layer
                # replace with nothing, and save in modified_load
                # modified_load = re.sub(AcceptEncodingRegex, "", scapy_packet[Raw].load)
                # print(modified_load)
                # new_packet = set_load(scapy_packet, modified_load)
                # set the new packet with the updated payload to the actual packet
                # packet.set_payload(str(new_packet))
            # Remove elif for testing modify payload in HTTP request
            # elif scapy_packet[TCP].sport == 80:
                # print("[+] This is a HTTP Response: ")
                # print(scapy_packet.show())

    packet.accept()


if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(2, process_packet)
    queue.run()
