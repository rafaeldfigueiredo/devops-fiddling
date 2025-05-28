import datetime
import os
import psutil

cpuPercent = psutil.cpu_percent(interval=1)
virtualMemory = psutil.virtual_memory().percent
diskUsage = psutil.disk_usage('/').percent

timestamp = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

os.makedirs("logs",exist_ok=True)

with open(f"logs/systemlog_{timestamp}.txt","w") as file:
  file.write(f'''System Monitor Log\nTimestamp: {timestamp}\n
CPU Usage: {cpuPercent}%
Memory Usage: {virtualMemory}%
Disk Usage: {diskUsage}%
  ''')