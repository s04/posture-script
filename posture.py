"""
Use MacOS Automator:
- Create new shell script app
- /usr/bin/python3 /path/to/posture_reminder.py
Open System Preferences and go to Users & Groups.
Select your user account and click on the Login Items tab.
Click the + button, find the Automator application you saved, and add it.
"""

import tkinter as tk
from tkinter import messagebox
import time
import threading

def show_posture_breathing_reminder():
    root.deiconify()
    root.lift()
    root.attributes("-topmost", True)
    root.after_idle(root.attributes, "-topmost", False)
    messagebox.showinfo("🧘 Posture Reminder", "Check your posture and take a deep breath! 🧘")
    root.withdraw()

def show_20_20_20_reminder():
    root.deiconify()
    root.lift()
    root.attributes("-topmost", True)
    root.after_idle(root.attributes, "-topmost", False)
    messagebox.showinfo("👀 20/20/20 Reminder", "Take a 20-second break and look at something 20 feet away! 👀")
    root.withdraw()

def show_stretch_reminder():
    root.deiconify()
    root.lift()
    root.attributes("-topmost", True)
    root.after_idle(root.attributes, "-topmost", False)
    messagebox.showinfo("🤸 Stretch Reminder", "Get up and stretch for a few minutes! 🤸")
    root.withdraw()

def start_reminders(testing=False):
    posture_breathing_interval = 8 * 60  # 8 minutes
    twenty_twenty_twenty_interval = 20 * 60  # 20 minutes
    stretch_interval = 55 * 60  # 55 minutes

    if testing:
        # Trigger all reminders in succession for testing
        show_posture_breathing_reminder()
        time.sleep(1)
        show_20_20_20_reminder()
        time.sleep(1)
        show_stretch_reminder()
        return

    while True:
        time.sleep(1)  # Check every second
        current_time = time.time()

        if int(current_time) % posture_breathing_interval == 0:
            show_posture_breathing_reminder()

        if int(current_time) % twenty_twenty_twenty_interval == 0:
            show_20_20_20_reminder()

        if int(current_time) % stretch_interval == 0:
            show_stretch_reminder()

# Create the main window
root = tk.Tk()
root.withdraw()  # Hide the main window initially

# Start the reminder thread
reminder_thread = threading.Thread(target=start_reminders, args=(False,))  # Set True for testing
reminder_thread.daemon = True  # This makes the thread exit when the main program exits
reminder_thread.start()

# Start the Tkinter main loop
root.mainloop()
