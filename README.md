# Python Network Packet Sniffer

## Project Overview

A Python-based network packet sniffer developed using Scapy to capture, inspect and export network traffic.

This project demonstrates practical network traffic analysis, Python programming and packet inspection techniques relevant to cybersecurity and Security Operations Centre (SOC) analysis.

## Project Objectives

- Capture live IPv4 network traffic.
- Identify source and destination IP addresses.
- Distinguish between TCP, UDP and ICMP traffic.
- Extract TCP and UDP port numbers.
- Identify DNS queries.
- Export packet metadata to CSV.
- Export captured packets to PCAP for analysis in Wireshark.

## Technologies Used

- Python 3
- Scapy
- Npcap
- Wireshark
- Visual Studio Code
- Git and GitHub

## Implementation

The packet sniffer uses Scapy to capture IPv4 packets from a selected network interface.

Captured packets are processed to extract IP addresses, protocol information, transport-layer ports and DNS query names where available.

Packet metadata is saved in CSV format, while captured packets are also exported in PCAP format for further inspection.

## Testing and Validation

The application was tested on a Windows 11 laptop using its Wi-Fi interface.

Testing confirmed that:

- Live network packets were successfully captured.
- TCP and UDP protocols were correctly identified.
- Source and destination port numbers were extracted.
- DNS queries were detected.
- CSV files contained captured packet metadata.
- PCAP files could be opened and analysed using Wireshark.

## Security Considerations

Packet capture should only be performed on networks and devices where monitoring is authorised.

Raw packet captures and exported network data are excluded from the public Git repository using `.gitignore` to reduce the risk of exposing sensitive information.

## Future Improvements

- Add command-line arguments for interface selection.
- Support configurable capture filters.
- Add timestamps to exported records.
- Improve error handling and logging.
- Introduce basic network anomaly detection.

## Disclaimer

This project was developed for educational purposes and authorised network analysis only.

### Project Evidence

## 1. Live Packet Capture

The Python application successfully captures live IPv4 network traffic and identifies source IP addresses, destination IP addresses and protocol numbers.



## 2. DNS Query Detection

The packet sniffer extracts DNS query names, allowing DNS requests to be examined during network analysis.


## 3. CSV Packet Export

Captured packet metadata is exported to CSV, allowing further analysis using spreadsheets or Python.

Project Evidence

1. Live Packet Capture

The Python application successfully captures live IPv4 network traffic and identifies source IP addresses, destination IP addresses and protocol numbers.



2. DNS Query Detection

The packet sniffer extracts DNS query names, allowing DNS requests to be examined during network analysis.



3. CSV Packet Export

Captured packet metadata is exported to CSV, allowing further analysis using spreadsheets or Python.



4. Wireshark PCAP Verification

The exported PCAP file was successfully opened in Wireshark, confirming that captured packets can be examined using industry-standard network analysis tools.

## 4. Wireshark PCAP Verification

The exported PCAP file was successfully opened in Wireshark, confirming that captured packets can be examined using industry-standard network analysis tools.