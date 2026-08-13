# SSH Brute Force Detection

## Objective

Detect repeated failed SSH authentication attempts
originating from the same source IP.

## Data Source

Ubuntu `/var/log/auth.log`

## Detection Logic

Multiple failed SSH authentication attempts
from the same source within a short time window.

## Test

Five intentional failed authentication attempts
were generated against the lab Ubuntu server.

## Expected Result

Wazuh identifies the repeated authentication
activity and generates security events.

## Evidence

- Wazuh event screenshot
- Ubuntu auth.log screenshot

## Severity

High

## Recommended Response

Investigate the source IP, review authentication
history, validate whether the account was compromised,
and apply appropriate SSH hardening.
