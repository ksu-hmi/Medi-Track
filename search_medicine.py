from tkinter import *
import sqlite3
import tkinter.messagebox as msg
from tkinter import ttk


def search():
    tv.delete(*tv.get_children())  # Clear previous search results
    query = "SELECT * FROM medicine WHERE MedicineName LIKE ? OR MedicineID=?"
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute(query, ('%' + search_term.get() + '%', search_term.get()))
    data = cursor.fetchall()

    if data:
        for row in data:
            tv.insert("", "end", values=row)
    else:
        msg.showinfo("Search Result", "No medicine found.")

    conn.close()


# Initialize the main window
window = Tk()
window.geometry('900x600')
window.title("MediTrack Medical Management System - Search Medicine")
window.iconbitmap('icon.ico')

# Background image
reg_image = PhotoImage(file="register_bg.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Top Heading Frame
TopHeadingFrame = Frame(window, bd=1)
TopHeadingFrame.pack(side=TOP, pady=20)

HeadingLabel = Label(TopHeadingFrame, text="MediTrack Medical Management System - Search Medicine",
                     font=("Helvetica", 18), fg="blue", bg="white")
HeadingLabel.pack(padx=10, pady=10)

# Mid Frame for buttons and controls
MidFrame = Frame(window, bd=1)
MidFrame.pack(side=TOP, pady=10)

# Search Label and Entry
search_term = StringVar()
SearchLabel = Label(MidFrame, text="Search Medicine by Name or ID:", font=("Helvetica", 16), fg="blue", bg="white")
SearchLabel.grid(row=0, column=0, padx=10, pady=10)
SearchEntry = Entry(MidFrame, font=("Helvetica", 16), textvariable=search_term)
SearchEntry.grid(row=0, column=1, padx=10, pady=10)

# Search Button
SearchButton = Button(MidFrame, text="Search", command=search, font=("Helvetica", 16), fg="black", bg="lightgreen")
SearchButton.grid(row=0, column=2, padx=10, pady=10)

# Treeview Frame for displaying search results
view_frame = Frame(window, bd=1)
view_frame.pack(side=TOP, fill=X, padx=20)

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


def back():
    window.destroy()
    import home


# Back Button
Back_button = Button(MidFrame, text="Back", command=back, font=("Helvetica", 16), fg="black", bg="lightgreen")
Back_button.grid(row=1, column=2, padx=10, pady=10)

# Start the main loop
window.mainloop()
