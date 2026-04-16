#!/usr/bin/env python3
import subprocess
import argparse

def set_pytables():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--remote", dest="remote", help="Test against a remote Target.")
    parser.add_argument("-s", "--set", dest="setiptables", help="Set IP Tables.")
    parser.add_argument("-n", "--number", dest="number", help="iptables number to set.")
    parser.add_argument("-f", "--flush", dest="flush", help="Flush the iptables.")
    options = parser.parse_args()

    if options.setiptables and options.number:
        number = options.number
        print("[+] We have a request to set the iptables to: " + number)
        if options.remote:
            print("[+] We have a request to test to a remote target.")
            subprocess.call(
                ["sudo", "iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", number, "--queue-bypass"])
        else:
            print("[+] We have a request to test locally.")
            subprocess.call(["sudo", "iptables", "-I", "INPUT", "-j", "NFQUEUE", "--queue-num", number, "--queue-bypass"])
            subprocess.call(["sudo", "iptables", "-I", "OUTPUT", "-j", "NFQUEUE", "--queue-num", number, "--queue-bypass"])
        print("[+] Check the iptables have been set:\n")
        subprocess.call(["sudo", "iptables", "-L"])

    elif options.flush:
        subprocess.call(["sudo", "iptables", "--flush"])
        print("[+] Flush iptables.")
        print("[+] Check if the iptables have been flushed.\n")
        subprocess.call(["sudo", "iptables", "-L"])

print("\n[+] Hellow World!  This is set_iptables")
set_pytables()


