#This helps users track when medications should be taken and notifies the patient.
from tkinter import *
import sqlite3
import tkinter.messagebox as msg

def create_schedule_window():
    window = Tk()
    window.geometry('700x400')
    window.title("Medication Schedule Tracker")

    # Create schedule table if not exists
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            MedicineName TEXT,
            ScheduleTime TEXT
        )
    """)
    conn.commit()
    conn.close()

    # Labels and Inputs
    Label(window, text="Medicine Name:", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=10)
    med_name_var = StringVar()
    Entry(window, textvariable=med_name_var, font=("Helvetica", 12)).grid(row=0, column=1)

    Label(window, text="Schedule Time (YYYY-MM-DD HH:MM):", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10)
    sched_time_var = StringVar()
    Entry(window, textvariable=sched_time_var, font=("Helvetica", 12)).grid(row=1, column=1)

    # Add Schedule Function
    def add_schedule():
        try:
            conn = sqlite3.connect("medicine.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO schedule (MedicineName, ScheduleTime) VALUES (?, ?)",
                           (med_name_var.get(), sched_time_var.get()))
            conn.commit()
            conn.close()
            msg.showinfo("Success", "Schedule Added Successfully")
        except Exception as e:
            msg.showerror("Error", f"Error adding schedule: {e}")

    Button(window, text="Add Schedule", command=add_schedule, font=("Helvetica", 12), bg="lightblue").grid(row=2, column=1, pady=20)

    window.mainloop()

if __name__ == "__main__":
    create_schedule_window()
