# Web Reconnaissance Detection

## Objective

Identify repeated requests for administrative or
potentially sensitive web paths.

## Data Source

Nginx access logs.

## Simulated Activity

Requests were made against:

- /admin
- /login
- /wp-admin
- /phpmyadmin

No exploitation was performed.

## Detection Logic

Multiple suspicious URL requests from the same
source within a short period.

## Expected Result

Wazuh identifies the web activity and provides
events that can be correlated into a reconnaissance
pattern.
