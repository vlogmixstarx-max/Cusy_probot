#!/usr/bin/env python3
import subprocess, json, time
from collections import Counter

def get_calls(): return json.loads(subprocess.run(['termux-telephony-calllog'], capture_output=True, text=True).stdout)

while True:
    nums = [c['_number'] for c in get_calls()[-10:]]
    for num, count in Counter(nums).items():
        if count > 3: print(f"🚨 SPAM: {num} ({count}x)")
    time.sleep(10)
