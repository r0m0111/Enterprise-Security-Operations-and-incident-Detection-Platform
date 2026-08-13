# Lab Architecture

## Objective

The lab simulates a small enterprise environment consisting
of Windows and Linux endpoints monitored by a centralized
Wazuh security platform.

## Components

### Windows Endpoint
The Windows host represents an employee workstation and
generates Windows security and system telemetry.

### Wazuh Server
The Wazuh VM acts as the centralized security monitoring
platform.

### Ubuntu Server
The Ubuntu VM represents a Linux production server running
Nginx and SSH.

## Data Flow

Windows → Wazuh Agent → Wazuh Manager

Ubuntu → Wazuh Agent → Wazuh Manager

Nginx → Wazuh Agent → Wazuh Manager
