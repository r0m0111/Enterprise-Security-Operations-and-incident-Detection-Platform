import json
from collections import Counter


LOG_FILE = "sample_events.json"


SUSPICIOUS_PATHS = {
    "/admin",
    "/wp-admin",
    "/phpmyadmin",
    "/.env"
}


def load_events(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def analyze_web_events(events):

    web_events = [
        event
        for event in events
        if event.get("data", {}).get("event_type") in {
            "web_recon",
            "http_error"
        }
    ]

    suspicious_requests = []

    for event in web_events:
        url = event.get("data", {}).get("url")

        if url in SUSPICIOUS_PATHS:
            suspicious_requests.append(event)

    return web_events, suspicious_requests


def main():

    events = load_events(LOG_FILE)

    web_events, suspicious_requests = analyze_web_events(events)

    print("Web Security Analysis")
    print("=" * 40)

    print(f"Total web events: {len(web_events)}")
    print(f"Suspicious requests: {len(suspicious_requests)}")
    print()

    for event in suspicious_requests:

        data = event.get("data", {})

        print(f"Source IP: {data.get('srcip')}")
        print(f"URL: {data.get('url')}")
        print(f"HTTP status: {data.get('status')}")
        print()


if __name__ == "__main__":
    main()