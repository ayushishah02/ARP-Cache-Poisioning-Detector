# ARP Cache Poisoning Detection Tool

Detect ARP spoofing attempts using Scapy, summarize suspicious traffic with Pandas,
and emit JSON alerts. Includes Docker, Kubernetes DaemonSet, and CI.

## Quickstart
```bash
pip install -r requirements.txt
python detector.py --pcap sample.pcap
```

## Docker
```bash
docker build -t arp-detector:local .
docker run --rm -v %cd%:/data arp-detector:local --pcap /data/sample.pcap
```

## Kubernetes
```bash
kubectl apply -f k8s/daemonset.yaml
```
