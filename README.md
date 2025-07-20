# Basic Network Sniffer 📡

A lightweight network packet analyzer built with Python and Scapy that allows you to inspect network traffic in real-time.

## Features ✨

- 🖥️ Live packet capture and analysis
- 🔍 Filter packets using BPF syntax (tcp, udp, port ranges, etc.)
- 🌐 Supports IP, TCP, UDP protocols
- 📡 Displays packet headers and payloads
- 📊 Simple CLI interface

## Prerequisites

- Python 3.6+
- Scapy (`pip install scapy`)
- Root/admin privileges (for packet capture)

## Example Output

[+] Starting packet capture with filter: tcp
Ether / IP / TCP 192.168.1.10:54236 > 142.250.190.46:443 PA / Raw
Source IP: 192.168.1.10
Destination IP: 142.250.190.46  
Source Port: 54236
Destination Port: 443
Payload: b'\x17\x03\x03...'
