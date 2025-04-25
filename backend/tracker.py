import time
import json
import os
from collections import defaultdict
from plyer import notification

try:
    import win32gui
except ImportError:
    print("This script works on Windows only (uses win32gui)")
    exit()

DATA_FILE = "usage_data.json"
ALERT_LIMITS = {
    "YouTube": 30 * 60,   # 30 minutes
    "Chrome": 60 * 60     # 1 hour
}

# Load saved data or start fresh
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        usage_data = defaultdict(int, json.load(f))
else:
    usage_data = defaultdict(int)

def get_active_window_title():
    window = win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def alert_user(app, seconds):
    mins = seconds // 60
    notification.notify(
        title="⏳ Time Limit Reached!",
        message=f"You’ve used {app} for {mins} minutes today. Time for a break!",
        timeout=5
    )

print("🧘 Digital Wellbeing Tracker is running... Press Ctrl+C to stop.")

prev_app = None
start_time = time.time()

try:
    while True:
        current_app = get_active_window_title()

        # Only track real app titles (ignore empty)
        if current_app.strip():
            if current_app != prev_app:
                elapsed = int(time.time() - start_time)
                if prev_app:
                    usage_data[prev_app] += elapsed
                    print(f"🔹 {prev_app} → {usage_data[prev_app] // 60} min")

                    # Alert if over time limit
                    for keyword, limit in ALERT_LIMITS.items():
                        if keyword.lower() in prev_app.lower() and usage_data[prev_app] > limit:
                            alert_user(prev_app, usage_data[prev_app])

                start_time = time.time()
                prev_app = current_app

        # Save data every 60 seconds
        if int(time.time()) % 10 == 0:
            with open(DATA_FILE, "w") as f:
                json.dump(dict(usage_data), f, indent=4)

        time.sleep(1)

except KeyboardInterrupt:
    print("\n🛑 Stopped. Saving usage data...")
    with open(DATA_FILE, "w") as f:
        json.dump(dict(usage_data), f, indent=4)
    print("✅ Data saved to usage_data.json")
