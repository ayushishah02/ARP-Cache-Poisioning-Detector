# ARP Cache Poisoning Detection Tool

This project is a **Python-based security utility** designed to detect **ARP spoofing / cache poisoning attacks** on a local network. It highlights skills in:

- **Network security** (ARP/MITM detection)  
- **Python programming** with **Scapy** & **Pandas**  
- **DevOps tooling**: Docker, Kubernetes, GitHub Actions (CI/CD)  

It provides both a **command-line tool** for analysis and a **containerized DaemonSet** for continuous monitoring in Kubernetes clusters.

---

## 🔍 Background

**ARP Cache Poisoning** (a form of Man-in-the-Middle attack) occurs when a malicious actor sends forged ARP messages on a local area network. This causes legitimate devices to associate the attacker’s MAC address with the IP address of another host (e.g., a gateway).  

- Result: traffic intended for the gateway is sent to the attacker.  
- Consequence: data theft, session hijacking, or DoS.  

This tool detects anomalies such as:  
- Multiple MAC addresses claiming the same IP address.  
- Excessive gratuitous ARP messages (often a sign of spoofing).

---

## ✨ Features

- **Scapy-powered packet analysis**: Parse live network traffic or `.pcap` files.  
- **Detection logic**:
  - Inconsistent ARP bindings (multiple MACs for one IP).  
  - High volume of gratuitous ARPs.  
- **Structured JSON output**: Summarizes suspicious hosts and alerts.  
- **Reporting with Pandas**: Quick summaries of observed IP–MAC mappings.  
- **CI/CD pipeline**:
  - Flake8 linting  
  - Pytest unit tests  
  - Docker image build on GitHub Actions  
- **Kubernetes deployment**: DaemonSet spec runs a detector pod on each node.

---

## 🚀 Usage

### 1. Local environment
```bash
pip install -r requirements.txt
python detector.py --pcap sample.pcap
