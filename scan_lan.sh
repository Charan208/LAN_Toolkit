#!/bin/bash
# scan_lan.sh

# Simple nmap scan to discover devices on the network
echo "Scanning the LAN..."
nmap -sn 192.168.1.0/24
