#!/bin/bash
echo 'Running It now'
cd /workspaces/devops-fiddling/server-monitor

# Activate virtual environment with absolute path
source /workspaces/devops-fiddling/server-monitor/venv/bin/activate

# Ensure logs folder exists
mkdir -p /workspaces/devops-fiddling/server-monitor/logs

# Run the monitor with absolute path
python3 /workspaces/devops-fiddling/server-monitor/monitor.py