from collections import Counter
import os

ips = Counter()

script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "sample_auth.log")

with open(log_path, "r") as log:
    for line in log:
        if "Failed password" in line:
            parts = line.split()
            ip = parts[-4]
            ips[ip] += 1

for ip, count in ips.items():
    if count > 5:
        print(f"[!] {ip} - {count} failed attempts")
