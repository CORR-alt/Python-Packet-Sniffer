from scapy.all import sniff, IP, TCP, UDP, DNS, DNSQR, PcapWriter

import csv
from pathlib import Path

CAPTURE_DIR = Path("captures")
CAPTURE_DIR.mkdir(exist_ok=True)

CSV_FILE = CAPTURE_DIR / "packet_capture.csv"

with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Source IP",
        "Destination IP",
        "Protocol",
        "Source Port",
        "Destination Port",
        "DNS Query"
    ])

PCAP_FILE = CAPTURE_DIR / "packet_capture.pcap"

pcap_writer = PcapWriter(str(PCAP_FILE), append=False, sync=True)

def process_packet(packet):
    if IP in packet:
        pcap_writer.write(packet)

        source = packet[IP].src
        destination = packet[IP].dst
        protocol_number = packet[IP].proto

        protocols = {
            1: "ICMP",
            6: "TCP",
            17: "UDP"
        }

        protocol = protocols.get(protocol_number, "Other")

        source_port = ""
        destination_port = ""
        domain = ""

        if TCP in packet:
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif UDP in packet:
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        if DNS in packet and packet[DNS].qr == 0 and DNSQR in packet:
            domain = packet[DNSQR].qname.decode(
                "utf-8", errors="replace"
            )

        print(f"Source: {source}")
        print(f"Destination: {destination}")
        print(f"Protocol: {protocol}")
        print(f"Source Port: {source_port}")
        print(f"Destination Port: {destination_port}")

        if domain:
            print(f"DNS Query: {domain}")

        print("-" * 40)

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                source,
                destination,
                protocol,
                source_port,
                destination_port,
                domain
            ])


print("Starting packet capture...")
try:
    sniff(
        iface=r"\Device\NPF_{086E19B4-9277-4B6C-B559-DECC3A40393F}",
        filter="ip",
        prn=process_packet,
        count=100,
        store=False
        )
finally:
    pcap_writer.close()

print("packet capture complete.")