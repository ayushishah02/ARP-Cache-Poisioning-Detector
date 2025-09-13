from detector import analyze_packets

def test_logic_with_empty():
    summary, alerts = analyze_packets([])
    assert summary["unique_ips"] == 0
    assert isinstance(alerts, list)
