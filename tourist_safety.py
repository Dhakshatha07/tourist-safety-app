import random
import time
from datetime import datetime

# Function to simulate GPS location
def get_location():
    lat = round(random.uniform(8.0, 13.0), 5)
    lon = round(random.uniform(76.0, 80.0), 5)
    return lat, lon

# Define risky areas (latitude and longitude ranges)
RISKY_AREAS = [
    {"name": "Dense Forest Zone", "lat_min": 8.5, "lat_max": 9.5, "lon_min": 77.0, "lon_max": 77.8},
    {"name": "Mountain Cliff Area", "lat_min": 10.0, "lat_max": 10.8, "lon_min": 78.5, "lon_max": 79.0},
    {"name": "Restricted Border Area", "lat_min": 11.0, "lat_max": 11.5, "lon_min": 79.0, "lon_max": 79.8}
]

# Function to simulate network signal
def check_signal():
    return random.choice([True, True, True, False])  # 75% OK, 25% no signal

# Function to check if tourist is inside a risky area
def check_risky_area(lat, lon):
    for area in RISKY_AREAS:
        if area["lat_min"] <= lat <= area["lat_max"] and area["lon_min"] <= lon <= area["lon_max"]:
            return area["name"]
    return None

# Function to log or print alerts
def send_alert(lat, lon, reason):
    message = f"🚨 ALERT: {reason} at location ({lat}, {lon})"
    print(message)
    with open("alert_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} | {message}\n")
    print("Alert recorded in alert_log.txt\n")

# Main monitoring function
def monitor_tourist():
    print("=== Tourist Safety App Activated ===")
    print("Monitoring tourist movement...\n")

    for i in range(1, 11):
        lat, lon = get_location()
        print(f"[{i}] Current Location → Latitude: {lat}, Longitude: {lon}")

        # Check risky area
        risky_area = check_risky_area(lat, lon)
        signal_ok = check_signal()

        if risky_area:
            print(f"⚠️ WARNING: Tourist entered {risky_area}!")
            send_alert(lat, lon, f"Entered {risky_area}")

        if not signal_ok:
            print("❌ Signal Lost! Triggering safety alert...")
            send_alert(lat, lon, "No signal detected")

        if not risky_area and signal_ok:
            print("✅ Area Safe. Signal OK. Monitoring continues...\n")

        time.sleep(2)

    print("Monitoring complete. Stay safe!\n")

# Run the program
if __name__ == "__main__":
    monitor_tourist()
