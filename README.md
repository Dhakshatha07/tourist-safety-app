Tourist Safety App – Safe and Risky Area Detection (Offline Version)

This Python-based Tourist Safety App simulates a system that monitors tourist movement, detects risky areas, checks signal status, and logs emergency alerts — all offline, without APIs or the internet.
It’s developed as a mini project to demonstrate Python concepts like randomization, conditionals, and file handling for real-world problem solving.

⚙️ Features

Simulates GPS location using random coordinates

Detects risky zones (forests, cliffs, restricted areas)

Checks network signal and triggers alerts if lost

Logs alerts with date and time in alert_log.txt

Works offline, no Twilio or APIs required

🧩 Python Modules Used
Module	Purpose
random	Generates random locations and signal values
time	Creates a real-time monitoring delay
datetime	Adds timestamp for every alert
💻 How to Run

Save the file as tourist_safety_app.py

Open VS Code or terminal in the same folder

Run the command:

python tourist_safety_app.py


View outputs on the terminal and check alert_log.txt for alert history

🧾 Sample Output
=== Tourist Safety App Activated ===
Monitoring tourist movement...

[1] Current Location → Latitude: 9.23456, Longitude: 77.54321
⚠️ WARNING: Tourist entered Dense Forest Zone!
🚨 ALERT: Entered Dense Forest Zone at location (9.23456, 77.54321)
Alert recorded in alert_log.txt

✅ Area Safe. Signal OK. Monitoring continues...

📘 Objectives

Simulate a tourist monitoring system using Python

Detect and log unsafe conditions automatically

Demonstrate Python’s use in safety and automation projects

💡 Future Enhancements

Add real GPS and map visualization

Enable SMS or app notifications

Create a graphical user interface for better usability

👩‍💻 Author

Dhakshatha J
B.Tech – Artificial Intelligence and Data Science
Amrita Vishwa Vidyapeetham, Nagercoil

📎 GitHub Repository
[https://github.com/Dhakshatha07/tourist-safety-app/commit/47af41404f6833d3a5c30ed65d51e1a1cf99a6a9](url)
