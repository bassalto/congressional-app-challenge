import tkinter as tk
from tkinter import messagebox
import json
from threading import Timer
import os

reminder_data = []

def save_reminders():
    with open('reminders.json', 'w') as file:
        json.dump(reminder_data, file)
    messagebox.showinfo("Success", "Reminders saved successfully!")

def load_reminders():
    global reminder_data
    if os.path.exists('reminders.json'):
        with open('reminders.json', 'r') as file:
            reminder_data = json.load(file)
        
        for reminder in reminder_data:
            med_name = reminder['med_name']
            delay = int(reminder['delay'])
            Timer(delay, lambda med_name=med_name: messagebox.showinfo("Reminder", f"Time to take {med_name}!")).start()
        
        messagebox.showinfo("Success", "Reminders loaded successfully and timers set!")
    else:
        messagebox.showinfo("Error", "No reminders file found!")

def set_reminder(med_name, delay, date, time):
    reminder = {
        "med_name": med_name,
        "delay": delay,
        "date": date,
        "time": time
    }
    reminder_data.append(reminder)
    save_reminders()
    Timer(delay, lambda: messagebox.showinfo("Reminder", f"Time to take {med_name}!")).start()

def submit_reminder():
    med_name = med_name_entry.get()
    delay = int(reminder_time_entry.get())
    date = reminder_date_entry.get()
    time = reminder_time_exact_entry.get()
    set_reminder(med_name, delay, date, time)
    messagebox.showinfo("Success", f"Reminder set for {med_name}")

app = tk.Tk()
app.title("Medication & Appointment Reminder")

tk.Label(app, text="Enter the Medication Name").pack()
med_name_entry = tk.Entry(app)
med_name_entry.pack()

tk.Label(app, text="Enter Reminder Time (in seconds)").pack()
reminder_time_entry = tk.Entry(app)
reminder_time_entry.pack()

tk.Label(app, text="Enter Reminder Date (MM/DD/YYYY)").pack()
reminder_date_entry = tk.Entry(app)
reminder_date_entry.pack()

tk.Label(app, text="Enter Reminder Exact Time (HH:MM)").pack()
reminder_time_exact_entry = tk.Entry(app)
reminder_time_exact_entry.pack()

tk.Button(app, text="Set Reminder", command=submit_reminder).pack()
tk.Button(app, text="Save Reminders", command=save_reminders).pack()
tk.Button(app, text="Load Reminders", command=load_reminders).pack()

app.mainloop()
