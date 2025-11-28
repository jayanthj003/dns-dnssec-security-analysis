# DNSSEC Vulnerability Explorer: Attack Simulation & Defense Lab
Hands-on DNS security project demonstrating DDoS amplification (28-54x factor), signature replay vulnerabilities, and KeyTrap attacks. 
Docker-based lab with Python automation, Wireshark analysis, and comprehensive mitigation implementations.

[![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-green.svg)](https://www.python.org/)
[![BIND9](https://img.shields.io/badge/BIND-9.x-orange.svg)](https://www.isc.org/bind/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# DNSSEC & DNS Security Analysis Project
A comprehensive practical exploration of DNS Security Extensions (DNSSEC) focusing on attack simulation, vulnerability analysis, and mitigation strategies in a controlled Docker environment.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Results](#results)
- [Repository Structure](#repository-structure)
- [Learning Outcomes](#learning-outcomes)
- [References](#references)
- [Acknowledgments](#acknowledgments)

## 🎯 Overview

This project demonstrates practical implementations of DNS security concepts including:
- DNS Amplification DDoS attacks and mitigation
- DNSSEC infrastructure setup and zone signing
- Signature replay attack simulation
- KeyTrap CPU exhaustion vulnerability analysis

The project uses Docker containers to create an isolated lab environment simulating real-world DNS infrastructure with multiple nameservers, resolvers, and attack scenarios.

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

## 🔧 Prerequisites

- **Operating System**: Ubuntu 20.04/22.04 LTS (Native installation recommended, no VM)
- **Docker**: Version 20.10 or higher
- **Docker Compose**: Version 1.29 or higher
- **Python**: 3.8+ with pip
- **System Packages**: 
  ```bash
  sudo apt-get install bind9utils tcpdump wireshark
  ```

### Python Dependencies
```bash
pip install scapy dnspython
```

## 📥 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/dnssec-security-project.git
cd dnssec-security-project
```

### 2. Install Docker (if not already installed)
```bash
chmod +x scripts/install_docker.sh
./scripts/install_docker.sh
# Restart your system after installation
```

### 3. Setup Lab Environment
```bash
cd Labsetup
docker-compose build
docker-compose up -d
```

### 4. Verify Installation
```bash
docker ps -a
# Should show containers: attacker, dns-server, user, root-server, etc.
```

## 📚 Project Tasks

### Task 1: DNS Amplification Attack (30 Marks)

**Objective**: Simulate DNS amplification attack and implement rate-limiting mitigation

**Steps**:
1. Analyze DNS "ANY" queries and response sizes
2. Craft spoofed DNS packets using Scapy
3. Calculate amplification factor
4. Send burst traffic (5-second continuous attack)
5. Implement rate limiting on DNS server
6. Compare attack effectiveness before/after mitigation

**Key Files**:
- `scripts/dns_amplification_attack.py`
- `pcap/task1_attack.pcap`
- `pcap/task1_mitigation.pcap`
- `configs/named.conf.options`

**Usage**:
```bash
# Run amplification attack
docker exec -it attacker bash
python3 /scripts/dns_amplification_attack.py

# Capture traffic on user machine
docker exec -it user bash
tcpdump -i eth0 -w /captures/amplification.pcap
```

---

### Task 2: DNSSEC Infrastructure Setup (10 Marks)

**Objective**: Configure complete DNSSEC infrastructure with zone signing

**Steps**:
1. Generate DNSKEY and KSK (Key Signing Key) pairs
2. Sign DNS zones with RRSIG records
3. Configure trust anchors and DS records
4. Establish root → TLD → authoritative nameserver chain

**Key Files**:
- `dnssec-configs/zone-signing.sh`
- `dnssec-configs/example.com.signed`
- `logs/dnssec-setup.log`

**Usage**:
```bash
cd local_dns_server
docker-compose up -d --build

# Verify DNSSEC
dig @10.9.0.53 example.com +dnssec
```

---

### Task 3: Signature Replay Attack (30 Marks)

**Objective**: Demonstrate DNSSEC signature replay vulnerability

**Steps**:
1. Capture DNSSEC-signed DNS responses
2. Extract RRSIG records from packet captures
3. Replay old signatures to DNS resolver
4. Analyze timestamp validation behavior
5. Implement expiration-based mitigation

**Key Files**:
- `scripts/signature_replay_attack.py`
- `scripts/check_signature_freshness.py`
- `pcap/task3_capture.pcap`
- `pcap/task3_replay.pcap`

**Usage**:
```bash
# Capture DNSSEC traffic
tcpdump -i eth0 port 53 -w dnssec_capture.pcap

# Run replay attack
python3 scripts/signature_replay_attack.py

# Check signature freshness
python3 scripts/check_signature_freshness.py
```

---

### Task 4: KeyTrap CPU Exhaustion Attack (30 Marks)

**Objective**: Analyze CPU exhaustion through excessive DNSSEC key validation

**Steps**:
1. Generate multiple large DNSKEY records
2. Configure spare-edu nameserver with excessive keys
3. Monitor CPU utilization during DNS queries
4. Plot CPU usage vs. number of keys
5. Analyze performance degradation

**Key Files**:
- `scripts/generate_keys.sh`
- `scripts/monitor_cpu.sh`
- `logs/docker_cpu_log.csv`
- `results/cpu_analysis.png`

**Usage**:
```bash
# Generate multiple keys
cd nameserver/spare-edu
bash /scripts/generate_keys.sh 50

# Monitor CPU during attack
bash scripts/monitor_cpu.sh &

# Execute DNS queries
dig @10.9.0.53 www.smith2022.edu +dnssec

# Analyze results
python3 scripts/plot_cpu_usage.py
```

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

## 📁 Repository Structure

```
dnssec-security-project/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── Labsetup/
│   ├── docker-compose.yml
│   ├── attacker/
│   ├── dns-server/
│   ├── user/
│   └── nameservers/
│
├── scripts/
│   ├── install_docker.sh
│   ├── dns_amplification_attack.py
│   ├── signature_replay_attack.py
│   ├── check_signature_freshness.py
│   ├── generate_keys.sh
│   ├── monitor_cpu.sh
│   └── plot_cpu_usage.py
│
├── configs/
│   ├── named.conf.options
│   ├── named.conf.local
│   └── zone files
│
├── dnssec-configs/
│   ├── zone-signing.sh
│   ├── key generation scripts
│   └── signed zone files
│
├── pcap/
│   ├── task1_attack.pcap
│   ├── task1_mitigation.pcap
│   ├── task3_capture.pcap
│   └── task4_traffic.pcap
│
├── logs/
│   ├── docker_cpu_log.csv
│   ├── attack_logs.txt
│   └── dnssec-setup.log
│
├── results/
│   ├── amplification_analysis.png
│   ├── cpu_utilization_graph.png
│   └── mitigation_comparison.png
│
└── report/
    └── DNSSEC_Project_Report.pdf
```

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