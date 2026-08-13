import json
from collections import defaultdict


LOG_FILE = "sample_events.json"


def load_events(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def calculate_risk(events):

    scores = defaultdict(int)

    for event in events:

        data = event.get("data", {})
        source_ip = data.get("srcip")

        if not source_ip:
            continue

        event_type = data.get("event_type")

        # Failed SSH authentication
        if event_type == "ssh_failed_login":
            scores[source_ip] += 2

        # Wazuh brute-force detection
        elif event_type == "ssh_bruteforce":
            scores[source_ip] += 10

        # Suspicious web request
        elif event_type == "web_recon":
            scores[source_ip] += 3

        # HTTP error activity
        elif event_type == "http_error":
            scores[source_ip] += 2

    return scores


def get_risk_level(score):

    if score >= 15:
        return "CRITICAL"

    if score >= 10:
        return "HIGH"

    if score >= 5:
        return "MEDIUM"

    return "LOW"


def main():

    events = load_events(LOG_FILE)

    scores = calculate_risk(events)

    print("Security Risk Assessment")
    print("=" * 40)

    for source_ip, score in scores.items():

        risk = get_risk_level(score)

        print(f"Source IP : {source_ip}")
        print(f"Risk Score: {score}")
        print(f"Risk Level: {risk}")
        print()


if __name__ == "__main__":
    main()