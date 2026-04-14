#!/usr/bin/env python3
import subprocess
import argparse

def set_pytables():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--set", dest="setiptables", help="Set IP Tables.")
    parser.add_argument("-n", "--number", dest="number", help="iptables number to set.")
    parser.add_argument("-f", "--flush", dest="flush", help="Flush the iptables.")
    options = parser.parse_args()

    if options.setiptables and options.number:
        number = options.number
        print("\n[+] Set the iptables to: " + number + "\n")
        subprocess.call(["sudo", "iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", number, "--queue-bypass"])
        subprocess.call(["sudo", "iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", number, "--queue-bypass"])
        print("[+]Check if the iptables have been set")
        subprocess.call(["sudo", "iptables", "-L"])

    elif options.flush:
        subprocess.call(["sudo", "iptables", "--flush"])
        print("\nCheck if the iptables have been flushed (unset)\n")
        subprocess.call(["sudo", "iptables", "-L"])

print("[+] Hellow World!  This is set-pytables")
set_pytables()


