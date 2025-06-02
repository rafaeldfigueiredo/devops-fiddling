#!/bin/bash

echo "[monitor] Running monitoring script..."
source /workspaces/devops-fiddling/server-monitor/venv/bin/activate
mkdir -p /workspaces/devops-fiddling/server-monitor/logs
python3 /workspaces/devops-fiddling/server-monitor/monitor.py

echo "[monitor] Monitoring script complete."
