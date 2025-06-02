import json
import datetime, os, psutil, logging, smtplib,subprocess,time,shutil
from subprocess import run
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

#Set Emailing Function
def send_email_alert(subject,body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.getenv("EMAIL_ADDRESS")
    msg["To"] = os.getenv("RECIPIENT")
    msg.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.starttls()
            smtp.login(os.getenv("EMAIL_ADDRESS"),os.getenv("EMAIL_PASSWORD"))
            smtp.send_message(msg)
            logging.info("Alert Email Incoming. Hey Fig")
    except Exception as e:
        logging.error(f"Failed to send email. Problem:\n{e}")

#Basic Logging stuff

log_path = "./server-monitor/logs/system.log"
archive_dir = "./server-monitor/logs/archive"
os.makedirs(archive_dir,exist_ok=True)
if os.path.exists(log_path) and os.path.getsize(log_path) > 1000000:
   timestamp = time.strftime("%Y%m%d-%H%M%S")
   archived_path = f"{archive_dir}/system_{timestamp}.log"
   shutil.move(log_path,archived_path)

logging.basicConfig(
  filename="/workspaces/devops-fiddling/server-monitor/logs/system.log",
  level=logging.INFO,
  format="[%(asctime)s] %(levelname)s: %(message)s",
  datefmt="%Y-%m-%d %H:%M:%S"
)

cpuPercent = psutil.cpu_percent(interval=1)
virtualMemory = psutil.virtual_memory().percent
diskUsage = psutil.disk_usage('/').percent

timestamp = datetime.datetime.now().strftime("%d.%m.%Y-%H:%M:%S")

logging.info(f"\nCPU Usage: {cpuPercent}%\nMemory Usage: {virtualMemory}%\nDisk Usage: {diskUsage}%")

if cpuPercent > 1:
  send_email_alert("HIGH CPU USAGE",f"CPU AT {cpuPercent}")
if virtualMemory > 90:
  send_email_alert("HIGH MEMORY USAGE",f"Memory at {virtualMemory}")
if diskUsage > 90:
  send_email_alert("HIGH DISK USAGE",f"DISK USAGE AT {diskUsage}")

logging.info(run(["df","-h"],capture_output=True,text=True))

csv_path = "./server-monitor/logs/metrics.csv"
write_header = not os.path.exists(csv_path)

with open(csv_path,"a" ) as csv_file:
  if write_header:
      csv_file.write("timestamp,cpu,memory,disk\n")
  csv_file.write(f"{timestamp},{cpuPercent} %,{virtualMemory} %,{diskUsage} %\n")

json_path = "./server-monitor/logs/metrics.json"
data_point = {
   "timestamp":timestamp,
   "cpu":cpuPercent,
   "memory":virtualMemory,
   "disk":diskUsage
}
with open(json_path,"a") as json_file:
   json_file.write(json.dumps(data_point)+"\n")