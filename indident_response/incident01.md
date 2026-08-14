# Incident 001 — Suspected Credential Compromise

## Executive Summary

A simulated security incident was conducted against
the laboratory Ubuntu web server.

Multiple SSH authentication failures were generated
from a single source, followed by a successful login.
Subsequent suspicious HTTP requests were observed.

The activity was detected using Wazuh telemetry and
analyzed using Python security analytics.

## Severity

HIGH

## Affected Asset

Ubuntu Web Server

## Detection

Wazuh SSH brute-force detection

## Supporting Evidence

- SSH authentication logs
- Wazuh alerts
- Nginx access logs
- Python risk analysis

## Attack Sequence

1. Multiple failed SSH authentication attempts
2. Successful SSH authentication
3. Suspicious web requests
4. Security alert generated
5. Analyst investigation performed

## Investigation

[Summarize what you found.]

## Impact

No actual compromise was performed.
This was a controlled laboratory simulation.

## Containment

[Describe the recommended containment actions.]

## Remediation

[Describe recommended security improvements.]

## Lessons Learned

- Authentication telemetry is critical for detecting credential attacks.
- Correlation provides more context than individual events.
- Web and authentication telemetry can be analyzed together.
- Detection thresholds must be tuned to reduce false positives.
