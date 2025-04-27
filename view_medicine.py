# from tkinter import *
# import sqlite3
# import tkinter.messagebox as msg
# from tkinter import ttk
# window = Tk()
# window.geometry('900x600')
# window.title("MediTrack Medical Management System")
# window.iconbitmap('icon.ico')
#
# # Background image
# reg_image = PhotoImage(file="register_bg.png")
# bg_label = Label(window, image=reg_image)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)
#
# # Top Heading Frame
# TopHeadingFrame = Frame(window, width=700, bd=1)
# TopHeadingFrame.pack(side=TOP)
# HeadingLabel = Label(TopHeadingFrame, text="MediTrack Medical Management System - View Medicine ",
#                      font=("Helvetica", 18), fg="blue", bg="white")
# HeadingLabel.grid(row=0, column=0, padx=1, pady=1)
# MidFrame = Frame(window, width=700, bd=1)
# MidFrame.pack(side=TOP)
#
# view_frame = Frame(window,bd=1)
# view_frame.pack(side=TOP,fill=X)
# tv=ttk.Treeview(view_frame,columns=("MedicineName","MedicineID","BrandName","ChemicalComponent","MFG_Date","Exp_Date","Price"))
# tv.heading("#1",text="Medicine Name")
# tv.heading("#2",text="Medicine ID")
# tv.heading("#3",text="Brand Name")
# tv.heading("#4",text="Chemical Component")
# tv.heading("#5",text="MFG_Date")
# tv.heading("#6",text="Exp_Date")
# tv.heading("#7",text="Price")
# tv.column("#0",width=0,stretch=NO)
# tv.column("#1",width=50,stretch=NO)
# tv.column("#2",width=50,stretch=NO)
# tv.column("#3",width=50,stretch=NO)
# tv.column("#4",width=50,stretch=NO)
# tv.column("#5",width=50,stretch=NO)
# tv.column("#6",width=50,stretch=NO)
# tv.column("#7",width=50,stretch=NO)
#
#
# tv.pack(fill=X)
# def view():
#     pass
# view_button = Button(MidFrame,text="view",command=view, font=("Helvetica", 16), fg="black", bg="lightgreen")
# view_button.grid(row=0, column=1, padx=10, pady=10)
# window.mainloop()

from tkinter import *
import sqlite3
import tkinter.messagebox as msg
from tkinter import ttk

# Initialize the main window
window = Tk()
window.geometry('900x600')
window.title("MediTrack Management System")
window.iconbitmap('icon.ico')

# Background image
reg_image = PhotoImage(file="register_bg.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Top Heading Frame
TopHeadingFrame = Frame(window, bd=1)
TopHeadingFrame.pack(side=TOP, pady=20)

HeadingLabel = Label(TopHeadingFrame, text="MediTrack Management System - View Medicine",
                     font=("Helvetica", 18), fg="blue", bg="white")
HeadingLabel.pack(padx=10, pady=10)

# Mid Frame for buttons and controls
MidFrame = Frame(window, bd=1)
MidFrame.pack(side=TOP, pady=10)

# Treeview Frame for displaying medicine data
view_frame = Frame(window, bd=1)
view_frame.pack(side=TOP, fill=X, padx=20)

def back():
    window.destroy()
    import home

# Treeview Widget
tv = ttk.Treeview(view_frame, columns=("MedicineName", "MedicineID", "BrandName", "ChemicalComponent",
                                       "MFG_Date", "Exp_Date", "Price"), show='headings')

tv.heading("MedicineName", text="Medicine Name")
tv.heading("MedicineID", text="Medicine ID")
tv.heading("BrandName", text="Brand Name")
tv.heading("ChemicalComponent", text="Chemical Component")
tv.heading("MFG_Date", text="MFG Date")
tv.heading("Exp_Date", text="EXP Date")
tv.heading("Price", text="Price")

tv.column("MedicineName", width=130)
tv.column("MedicineID", width=100)
tv.column("BrandName", width=130)
tv.column("ChemicalComponent", width=150)
tv.column("MFG_Date", width=100)
tv.column("Exp_Date", width=100)
tv.column("Price", width=80)

tv.pack(fill=X, padx=10, pady=10)


conn=sqlite3.connect("medicine.db")
cursor = conn.cursor()
cursor.execute("select * from 'medicine'")
data = cursor.fetchall()
for i in data:
    tv.insert("","end",values=i)
conn.commit()
Back_button = Button(MidFrame, text="Back", command=back, font=("Helvetica", 16), fg="black", bg="lightgreen")
Back_button.grid(row=8, column=1, padx=10, pady=10)

import threading  # Import threading module for managing
import time       # Import time module for handling the timer

def set_alert():
    def start_timer():
        try:
            duration = int(timer_entry.get())  # timer duration only in seconds
            msg.showinfo("Alert Set", "Reminder set for {} seconds!".format(duration))
            time.sleep(duration)  # Wait for the specified time
            msg.showinfo("Medication Reminder", "It's time to take your medication!")
        except ValueError:
            msg.showerror("Invalid Input", "Please enter a valid number for the timer.")

    threading.Thread(target=start_timer).start()  # Run the timer

# Alert Timer Frame time to take medication!
alert_frame = Frame(window, bd=1)
alert_frame.pack(side=TOP, pady=20)

alert_label = Label(alert_frame, text="Set Medication Alert (in seconds):", font=("Helvetica", 14), fg="blue")
alert_label.pack(side=LEFT, padx=10)

timer_entry = Entry(alert_frame, font=("Helvetica", 14), width=10)
timer_entry.pack(side=LEFT, padx=10)

alert_button = Button(alert_frame, text="Set Alert", command=set_alert, font=("Helvetica", 14), fg="black", bg="orange")
alert_button.pack(side=LEFT, padx=10)

Back_button = Button(MidFrame, text="Back", command=back, font=("Helvetica", 16), fg="black", bg="lightgreen")
Back_button.grid(row=8, column=1, padx=10, pady=10)


# Start the main loop
window.mainloop()
