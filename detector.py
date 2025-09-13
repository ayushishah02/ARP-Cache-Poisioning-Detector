import argparse
import json
import time
from collections import defaultdict

from scapy.all import rdpcap, sniff, ARP
import pandas as pd


def analyze_packets(packets):
    """
    Detect ARP spoofing:
      - Multiple MACs claiming the same IP
      - Excessive gratuitous ARPs
    """
    ip_to_macs = defaultdict(set)
    gratuitous = 0
    alerts = []

    for p in packets:
        if not p.haslayer(ARP):
            continue
        arp = p[ARP]
        if arp.op in (1, 2):  # who-has / is-at
            ip_to_macs[arp.psrc].add(arp.hwsrc)
            if arp.psrc == arp.pdst:  # gratuitous
                gratuitous += 1

    for ip, macs in ip_to_macs.items():
        if len(macs) > 1:
            alerts.append({
                "type": "INCONSISTENT_BINDING",
                "ip": ip,
                "macs": list(macs),
                "msg": f"Multiple MACs claim {ip}"
            })

    if gratuitous > 10:
        alerts.append({
            "type": "EXCESSIVE_GRATUITOUS_ARP",
            "count": gratuitous,
            "msg": "High volume of gratuitous ARP observed"
        })

    df = pd.DataFrame(
        [{"ip": ip, "macs": list(m)} for ip, m in ip_to_macs.items()]
    )
    summary = {
        "unique_ips": len(df),
        "hosts_observed": df.to_dict(orient="records"),
        "gratuitous_count": gratuitous
    }
    return summary, alerts


def load_packets(pcap_path=None, live=False, iface=None, timeout=10):
    if pcap_path:
        return rdpcap(pcap_path)
    if live:
        return sniff(iface=iface, timeout=timeout, filter="arp")
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pcap", help="Path to ARP pcap")
    ap.add_argument("--live", action="store_true", help="Sniff live ARP traffic")
    ap.add_argument("--iface", help="Interface for live sniffing")
    ap.add_argument("--timeout", type=int, default=10)
    args = ap.parse_args()

    packets = load_packets(args.pcap, args.live, args.iface, args.timeout)
    summary, alerts = analyze_packets(packets)
    out = {"ts": int(time.time()), "summary": summary, "alerts": alerts}
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
