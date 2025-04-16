import csv
import os
from datetime import datetime

LOG_FILE = "logs/results.csv"

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

def log_result(topic, tone, choice, outcome):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    header = ["Timestamp", "Topic", "Tone", "User Choice", "Outcome"]
    data = [timestamp, topic, tone, choice, outcome]
    
    file_exists = os.path.isfile(LOG_FILE)
    with open (LOG_FILE, "a", newline= '') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(data)