import os
from datetime import datetime

file_log = "activity_log.md"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(file_log, "a") as f:
    f.write(f"- **{timestamp}**: Automated Cloud Update\n")

print(f"Log updated at {timestamp}")
