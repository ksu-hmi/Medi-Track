from tkinter import *
import sqlite3
import tkinter.messagebox as msg

def delete():
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    query = "DELETE FROM medicine WHERE MedicineName=? OR MedicineID=?"
    cursor.execute(query, (Medicine_name.get(), Medicine_id.get()))

    if cursor.rowcount > 0:
        conn.commit()
        msg.showinfo("Delete Medicine", "Medicine deleted successfully", icon="info")
    else:
        msg.showwarning("Delete Medicine", "No matching medicine found", icon="warning")

    conn.close()

# Initialize the main window
window = Tk()
window.geometry('900x600')
window.title("MediTrack Medical Management System - Delete Medicine")
window.iconbitmap('icon.ico')

# Background image
reg_image = PhotoImage(file="register_bg.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Top Heading Frame
TopHeadingFrame = Frame(window, bd=1)
TopHeadingFrame.pack(side=TOP, pady=20)

HeadingLabel = Label(TopHeadingFrame, text="MediTrack Medical Management System - Delete Medicine",
                     font=("Helvetica", 18), fg="blue", bg="white")
HeadingLabel.pack(padx=10, pady=10)

# Mid Frame for buttons and controls
MidFrame = Frame(window, bd=1)
MidFrame.pack(side=TOP, pady=10)

# Medicine Name Label and Textbox
Medicine_name = StringVar()
Medicine_name.set("")
Medicine_NameLabel = Label(MidFrame, text="Medicine Name", font=("Helvetica", 16), fg="blue", bg="white")
Medicine_NameLabel.grid(row=0, column=0, padx=10, pady=10)
Medicine_NameTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=Medicine_name)
Medicine_NameTextBox.grid(row=0, column=1, padx=10, pady=10)

# Medicine ID Label and Textbox
Medicine_id = IntVar()
Medicine_id.set("")
Medicine_idLabel = Label(MidFrame, text="Medicine ID", font=("Helvetica", 16), fg="blue", bg="white")
Medicine_idLabel.grid(row=1, column=0, padx=10, pady=10)
Medicine_idTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=Medicine_id)
Medicine_idTextBox.grid(row=1, column=1, padx=10, pady=10)

# Delete Button
DeleteButton = Button(MidFrame, text="Delete", command=delete, font=("Helvetica", 16), fg="black", bg="pink")
DeleteButton.grid(row=2, column=1, padx=10, pady=10)

def back():
    window.destroy()
    import home

# Back Button
Back_button = Button(MidFrame, text="Back", command=back, font=("Helvetica", 16), fg="black", bg="lightgreen")
Back_button.grid(row=3, column=1, padx=10, pady=10)

# Start the main loop
window.mainloop()
