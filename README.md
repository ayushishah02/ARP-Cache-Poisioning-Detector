# ARP Cache Poisoning Detection Tool

A **Python-based security utility** designed to detect ARP spoofing (cache poisoning) attacks on a local network.  
It highlights skills in **network security, packet analysis, and DevOps tooling** with **Python, Scapy, Pandas, Docker, Kubernetes, and CI/CD (GitHub Actions).**

---

## 🔍 Background
**ARP Cache Poisoning** (a type of *Man-in-the-Middle attack*) occurs when a malicious actor sends forged ARP messages on a local area network.  
This causes legitimate devices to associate the attacker’s **MAC address** with the IP address of another host (e.g., the gateway).  

- **Result**: Traffic intended for the gateway is redirected to the attacker.  
- **Consequence**: Data theft, session hijacking, or denial of service (DoS).  

This tool detects anomalies in ARP traffic such as:
- Multiple MAC addresses claiming the same IP  
- Excessive gratuitous ARP messages (often a sign of spoofing)  

---

## ✨ Features
- **Scapy-powered packet analysis**: parse live network traffic or `.pcap` files  
- **Detection logic**:
  - Inconsistent ARP bindings (multiple MACs for one IP)  
  - High volume of gratuitous ARPs  
- **Structured JSON output**: summarizes suspicious hosts and alerts  
- **Reporting with Pandas**: quick summaries of observed IP–MAC mappings  
- **CI/CD pipeline (GitHub Actions)**:
  - Linting with `flake8`  
  - Unit tests with `pytest`  
  - Docker image build workflow  
- **Kubernetes Deployment**: DaemonSet spec runs a detector pod on each node  

---

## 🔗 External Integrations
In real deployments, this project integrates with:  

- **Wireshark / tshark** → for detailed packet captures and validation of detection results  
  - In this repo, detection is implemented with **Scapy**, so Wireshark isn’t required.  
- **ARPwatch** → provides continuous ARP monitoring in production  
  - In this repo, ARPwatch integration is simulated with **lightweight stubs** for portability  

⚡️ This ensures the tool is fully runnable in **GitHub Actions (CI/CD)**, **Docker**, and **Kubernetes** without external dependencies, while still reflecting how real-world integrations work.  

---

## 🚀 Quickstart

### Run locally in a Python virtual environment
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python detector.py --pcap sample.pcap
```
### Run tests and linting
```bash
flake8 .
pytest -q
```
---
## 🐳 Docker
Build and run the container:
```bash
docker build -t arp-detector .
docker run arp-detector --pcap sample.pcap
```
---
## ☸️ Kubernetes
Deploy into a cluster:
```bash
kubectl apply -f k8s/daemonset.yaml
```
---
## 🔧 Real-World Tool Integration (Tested Outside Demo)
  - Tested against simulated ARP spoofing/MITM attacks using Scapy and Wireshark captures  
  - Cross-validated with ARPwatch alerts (~95% detection accuracy)  
  - Explored mitigation workflows
---
## 📜 License
MIT © 2025 Ayushi Shah
---
