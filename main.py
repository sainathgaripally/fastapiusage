import psutil
from fastapi import FastAPI
import mysql.connector

app = FastAPI()

@app.get("/")
def home():
  return "Hi, Welcome to fastapi"

@app.get("/metrics")
def get_metrics():
  metrics_data = {
    "cpu_usage" : psutil.cpu_percent(interval:1),
    "memory_usage" : psutil.virtual_memory().percent,
    "disk_usage" : psutil.disk_usage("/").percent,
    "bytes_received" : psutil.net_io_counters().bytes_recv,
    "bytes_sent" : psutil.net_io_counters().bytes_sent,
    "uptime" : psutil.boot_time()
  }
  return metrics_data


      
