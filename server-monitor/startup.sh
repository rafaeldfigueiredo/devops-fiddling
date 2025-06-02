#!/bin/bash
echo "[startup] Beginning startup setup..."
source /workspaces/devops-fiddling/server-monitor/venv/bin/activate
echo "[startup] Virtual environment activated."

if ! command -v cron >/dev/null; then
  echo "[startup] Installing cron..."
  sudo apt-get update && sudo apt-get install -y cron
fi
echo "[startup] Starting cron service..."
sudo service cron start
mkdir -p /workspaces/devops-fiddling/server-monitor/logs
echo "[startup] Log directory ensured."
CRON_JOB="*/5 * * * * /bin/bash /workspaces/devops-fiddling/server-monitor/run_monitor.sh"
(crontab -l 2>/dev/null | grep -F "$CRON_JOB" >/dev/null) || (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
echo "[startup] Cron job registered."
echo "[startup] Startup complete."
