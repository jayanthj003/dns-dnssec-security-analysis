# DNSSEC Assignment 

This repository contains the DNSSEC assignment , including simulations and mitigation of DNS amplification attacks, DNSSEC signature replay attacks, and DNSSEC Keytrap attacks. The work was completed using Docker containers and various DNSSEC tools.

---

## Overview
This project explores DNS security mechanisms using DNSSEC. It involves:

1. Simulating DNS amplification attacks and mitigating them.
2. Generating DNSSEC keys (KSK and ZSK) and signing zones.
3. Demonstrating DNSSEC signature replay attacks and their mitigations.
4. Simulating DNSSEC Keytrap attacks to study CPU overhead and performance impact.

---
## ✨ Features

- **DNS Amplification Attack Simulation**: Crafted spoofed DNS queries using Scapy with amplification factor analysis
- **DNSSEC Implementation**: Complete DNSSEC infrastructure with cryptographic zone signing and trust chain establishment
- **Signature Replay Attack**: Demonstrated DNSSEC vulnerability through replaying captured RRSIG records
- **KeyTrap Attack**: CPU exhaustion analysis with automated monitoring and visualization
- **Rate Limiting Mitigation**: Implemented response rate limiting on BIND DNS servers
- **Traffic Analysis**: Comprehensive packet-level forensics using Wireshark and tcpdump
- **Automated Monitoring**: CPU utilization logging and CSV-based analysis pipelines

## 🏗️ Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Attacker  │─────▶│  DNS Server  │◀─────│    User     │
│ Container   │      │ (10.9.0.53)  │      │ (10.9.0.5)  │
└─────────────┘      └──────────────┘      └─────────────┘
                            │
                            │ DNSSEC Chain
                            ▼
                   ┌────────────────┐
                   │  Root Server   │
                   │      ↓         │
                   │  TLD Server    │
                   │      ↓         │
                   │ Auth Server    │
                   └────────────────┘
```

---
## 📥 Installation

1. Clone the Repository

2. Install Docker (if not already installed)

3. Setup Lab Environment

4. Verify Installation

---
## Tasks

### Task 1: DNS Amplification Attack Simulation and Mitigation
Steps:
1. Set up Docker containers for attacker, user, and server.
2. Run a standard `dig` command from the attacker terminal.
3. Send spoofed DNS queries with source IP set to the user’s IP.
4. Capture DNS requests and responses using `tcpdump`.
5. Calculate amplification factor.
6. Send bursts of DNS queries and monitor traffic.
7. Mitigate attacks by limiting DNS response rates (e.g., 5 responses per 5 seconds).

### Task 2: DNSSEC Key Generation and Zone Signing
Steps:

1. Generate KSK and ZSK keys for `example.edu` server.
3. Sign the `edu.example.db`, `edu.db`, and `root.db` files.
4. Verify configuration using `dig` commands; successful NOERROR and AD flags indicate proper setup.

### Task 3: DNSSEC Signature Replay Attack
Steps:
1. Capture DNSSEC traffic using `tcpdump` or Wireshark.
2. Extract signed responses containing RRSIG, A, NS, and SOA records.
3. Replay the captured signatures using `scapy`, `dig +dnssec`, or `tcpreplay`.
4. Monitor the resolver to check if old signatures are accepted.
5. Mitigation: Implement time-based validity and proper TTLs in zone signing to prevent replay attacks.

### Task 4: DNSSEC Keytrap Attack Simulation
Objective: Demonstrate how increasing the number of ZSKs affects CPU usage and server performance.

Steps:
1. Set up `smith2022.edu` name server and generate multiple ZSKs and 1 KSK.
2. Sign zone files and update BIND configurations.
3. Share DS records with EDU nameserver and re-sign `edu.db` and `root.db`.
4. Monitor CPU usage with a script while sending repeated `dig +dnssec` queries.
5. Observe the correlation between the number of keys and server CPU load.

---

## Setup Instructions
1. Install Docker and necessary DNSSEC tools (BIND, `dnssec-signzone`, `dig`, `tcpdump`, `scapy`).
2. Clone this repository.
3. Build Docker containers as described in the report.
4. Follow task-specific steps to run simulations and experiments.

---
## 📊 Results

### DNS Amplification Analysis
- **Amplification Factor**: 28x - 54x (depending on zone configuration)
- **Mitigation Effectiveness**: 85% reduction in response volume with rate limiting
- **Attack Traffic**: ~500 packets/sec without mitigation → ~75 packets/sec with mitigation

### DNSSEC Signature Replay
- **Vulnerability Window**: 24-48 hours (default RRSIG validity period)
- **Detection Rate**: 100% when proper expiration validation is enabled
- **Mitigation**: Reduced signature validity to 6 hours, implemented freshness checks

### KeyTrap CPU Impact
- **Baseline CPU**: 5-8% with single key
- **50 Keys**: 65-80% CPU utilization
- **100 Keys**: 95%+ CPU, query timeouts observed
- **Linear Scaling**: ~1.2% CPU increase per additional key


## 🎓 Learning Outcomes

- **Network Security**: Understanding DNS protocol vulnerabilities and DDoS attack vectors
- **Cryptography**: Practical implementation of digital signatures and PKI trust chains
- **Traffic Analysis**: Packet-level forensics using Wireshark, tcpdump, and Scapy
- **Container Orchestration**: Multi-container Docker networking and service configuration
- **Mitigation Strategies**: Rate limiting, signature validation, and resource management
- **Performance Analysis**: CPU monitoring, bottleneck identification, and scalability testing
- **Automation**: Shell scripting, Python automation, and CSV-based data pipelines

## 📖 References

### Documentation
- [BIND9 Administrator Reference Manual](https://bind9.readthedocs.io/)
- [RFC 4033-4035: DNSSEC Specifications](https://datatracker.ietf.org/doc/html/rfc4033)
- [Scapy Documentation](https://scapy.readthedocs.io/)

### Research Papers
- [DNSSEC KeyTrap Vulnerability Analysis](https://www.athene-center.de/keytrap)
- [DNS Amplification Attack Mitigation Strategies](https://www.usenix.org/conference/usenixsecurity20/presentation/xiang)

### Tutorials
- [SEED Labs - DNSSEC](https://seedsecuritylabs.org/Labs_20.04/Networking/DNS_Security/)
- [Digital Ocean - DNS Security Best Practices](https://www.digitalocean.com/community/tutorials/how-to-setup-dnssec-on-an-authoritative-bind-dns-server)

## 🙏 Acknowledgments
- **IIT Hyderabad CSE Department**: For academic guidance and resources

## ⚠️ Disclaimer

This project is for **educational purposes only**. All attacks were performed in isolated Docker environments. Unauthorized use of these techniques against real infrastructure is illegal and unethical. Always obtain proper authorization before conducting security testing.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.