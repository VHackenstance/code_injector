#!/usr/bin/env python3
# Rebuild
import netfilterqueue

def process_packet(packet):
    print("\n[+] Hello World, this is Code Injector!")

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()