import json
from pathlib import Path


LOG_FILE = Path("sample_events.json")


def load_events(filename):
    """Load security events from a JSON file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        return []

    except json.JSONDecodeError:
        print(f"Error: {filename} is not valid JSON.")
        return []


def summarize_event(event):
    """Extract useful security information from a Wazuh event."""

    rule = event.get("rule", {})
    data = event.get("data", {})

    return {
        "timestamp": event.get("timestamp"),
        "rule_id": rule.get("id"),
        "severity": rule.get("level"),
        "description": rule.get("description"),
        "source_ip": data.get("srcip"),
        "username": data.get("srcuser"),
        "event_type": data.get("event_type"),
        "url": data.get("url"),
        "status": data.get("status"),
    }


def main():
    events = load_events(LOG_FILE)

    print(f"Loaded {len(events)} security events.\n")

    for event in events:
        summary = summarize_event(event)

        print("-" * 60)
        print(f"Timestamp : {summary['timestamp']}")
        print(f"Rule ID  : {summary['rule_id']}")
        print(f"Severity : {summary['severity']}")
        print(f"Event    : {summary['description']}")
        print(f"Source IP: {summary['source_ip']}")
        print(f"Username : {summary['username']}")
        print(f"URL      : {summary['url']}")
        print(f"Status   : {summary['status']}")


if __name__ == "__main__":
    main()