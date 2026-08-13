import json
from collections import Counter


LOG_FILE = "sample_events.json"


def load_events(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def analyze_ssh_events(events):
    failed_logins = [
        event
        for event in events
        if event.get("data", {}).get("event_type") == "ssh_failed_login"
    ]

    source_counts = Counter(
        event.get("data", {}).get("srcip")
        for event in failed_logins
    )

    return source_counts


def main():
    events = load_events(LOG_FILE)

    source_counts = analyze_ssh_events(events)

    print("SSH Authentication Analysis")
    print("=" * 40)

    if not source_counts:
        print("No failed SSH authentication events found.")
        return

    for source_ip, count in source_counts.items():
        print(f"Source IP: {source_ip}")
        print(f"Failed attempts: {count}")

        if count >= 5:
            print("Risk: HIGH")
        elif count >= 3:
            print("Risk: MEDIUM")
        else:
            print("Risk: LOW")

        print()


if __name__ == "__main__":
    main()