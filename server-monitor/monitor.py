import datetime
import os
import psutil
import logging

logging.basicConfig(
  filename="logs/system.log",
  level=logging.INFO,
  format="[%(asctime)s] %(levelname)s: %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S"
)

cpuPercent = psutil.cpu_percent(interval=1)
virtualMemory = psutil.virtual_memory().percent
diskUsage = psutil.disk_usage('/').percent

timestamp = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

os.makedirs("logs",exist_ok=True)

logging.info(f"\nCPU Usage: {cpuPercent}%\nMemory Usage: {virtualMemory}%\nDisk Usage: {diskUsage}%")