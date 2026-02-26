#!/usr/bin/env python3
import subprocess, json, time, re

def get_sms(): return json.loads(subprocess.run(['termux-sms-list'], capture_output=True, text=True).stdout)

while True:
    for sms in get_sms():
        body = sms['_body'].lower()
        if re.search(r'(otp|verify|password|welcome|login)', body):
            print(f"🚫 BLOCKED: {sms['_address']} - {body[:30]}")
    time.sleep(3)
