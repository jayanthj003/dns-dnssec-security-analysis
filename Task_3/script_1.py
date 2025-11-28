from scapy.all import *

# Load all packets
pkts = rdpcap("step_1.pcap")

# Print number of packets (optional)
print(f"Loaded {len(pkts)} packets")

# Show the last packet (should contain RRSIG)
last_pkt = pkts[-1]
print("Sending last packet:")
last_pkt.show()

# Send the last packet
send(last_pkt)
