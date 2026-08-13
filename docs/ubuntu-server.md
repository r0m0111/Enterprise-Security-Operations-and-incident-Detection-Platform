# Ubuntu Web Server

## Role

The Ubuntu VM represents a Linux server hosting web
and infrastructure services.

## VM Configuration

- VM: Workstation Pro 17.6.4
- OS: Ubuntu Server 24.04 LTS
- CPU: 2 cores
- RAM: 2 GB
- Storage: 25 GB

## Services

- Nginx
- OpenSSH
- Wazuh Agent

## Logs

Nginx generates:

- access.log
- error.log

These logs are collected by the Wazuh agent.

## Data Flow

Nginx
 ↓
Nginx Logs


##Set Up Commands
- sudo apt update
- sudo apt install curl wget git vim
 ↓
Wazuh Agent
 ↓
Wazuh Manager
 ↓
Wazuh Dashboard
