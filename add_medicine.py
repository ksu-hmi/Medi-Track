from tkinter import *
import sqlite3
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')
window.title("Shifa Medical Management System")

# Load window icon
try:
    window.iconbitmap('icon.ico')
except Exception as e:
    print(f"Icon file not found: {e}")

# Background image
reg_image = PhotoImage(file="register_bg.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Top Heading Frame
TopHeadingFrame = Frame(window, width=700, bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame, text="Shifa Medical Management System - Add Medicine",
                     font=("Helvetica", 18), fg="blue", bg="white")
HeadingLabel.grid(row=0, column=0, padx=10, pady=10)

# Mid Frame
MidFrame = Frame(window, width=600, bd=1)
MidFrame.pack(side=TOP)

# Verify table structure
conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(medicine)")
print(cursor.fetchall())  # This will print the current structure of the table

# Recreate the table with correct structure
cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicine (
        MedicineName TEXT, 
        MedicineID INT, 
        BrandName TEXT, 
        ChemicalComponent TEXT, 
        MFG_Date TEXT, 
        Exp_Date TEXT,  -- Ensure this name matches the one in the INSERT query
        Price FLOAT
    )
""")
conn.commit()
conn.close()

# Medicine Name Label and Textbox
Medicine_name = StringVar()
Medicine_name.set("")
Medicine_NameLabel = Label(MidFrame, text="Medicine Name", font=("Helvetica", 12), fg="blue", bg="white")
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

# Brand Name Label and Textbox
Brandname = StringVar()
Brandname.set("")
BrandnameLabel = Label(MidFrame, text="Brand Name", font=("Helvetica", 16), fg="blue", bg="white")
BrandnameLabel.grid(row=2, column=0, padx=10, pady=10)
BrandnameTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=Brandname)
BrandnameTextBox.grid(row=2, column=1, padx=10, pady=10)

# Chemical Component Label and Textbox
ChemicalComponent = StringVar()
ChemicalComponent.set("")
ChemicalComponentLabel = Label(MidFrame, text="Chemical Component", font=("Helvetica", 16), fg="blue", bg="white")
ChemicalComponentLabel.grid(row=3, column=0, padx=10, pady=10)
ChemicalComponentTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=ChemicalComponent)
ChemicalComponentTextBox.grid(row=3, column=1, padx=10, pady=10)

# MFG Date Label and Textbox
mfg = StringVar()
mfg.set("")
mfgLabel = Label(MidFrame, text="MFG Date", font=("Helvetica", 16), fg="blue", bg="white")
mfgLabel.grid(row=4, column=0, padx=10, pady=10)
mfgTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=mfg)
mfgTextBox.grid(row=4, column=1, padx=10, pady=10)

# Expiration Date Label and Textbox
Exp = StringVar()
Exp.set("")
ExpLabel = Label(MidFrame, text="Expiration Date", font=("Helvetica", 16), fg="blue", bg="white")
ExpLabel.grid(row=5, column=0, padx=10, pady=10)
ExpTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=Exp)
ExpTextBox.grid(row=5, column=1, padx=10, pady=10)

# Price Label and Textbox
Price = IntVar()
Price.set("")
PriceLabel = Label(MidFrame, text="Price", font=("Helvetica", 16), fg="blue", bg="white")
PriceLabel.grid(row=6, column=0, padx=10, pady=10)
PriceTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=Price)
PriceTextBox.grid(row=6, column=1, padx=10, pady=10)

# Function to Add Medicine
def add():
    try:
        conn = sqlite3.connect("medicine.db")
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO medicine 
                        (MedicineName, MedicineID, BrandName, ChemicalComponent, MFG_Date, Exp_Date, Price) 
                        VALUES(?, ?, ?, ?, ?, ?, ?)""",
                       (Medicine_name.get(), Medicine_id.get(), Brandname.get(), ChemicalComponent.get(),
                        mfg.get(), Exp.get(), Price.get()))
        conn.commit()

        if cursor.rowcount > 0:
            msg.showinfo("Add Medicine", "New Medicine Added Successfully", icon="info")
        else:
            msg.showwarning("Error", "Medicine Not Added", icon="warning")

        conn.close()

    except Exception as e:
        msg.showerror("Error", f"An error occurred: {e}")

# Function to Return to Home
def back():
    window.destroy()
    import home

# Add and Back Buttons
add_button = Button(MidFrame, text="Add", command=add, font=("Helvetica", 16), fg="black", bg="pink")
add_button.grid(row=7, column=1, padx=10, pady=10)

Back_button = Button(MidFrame, text="Back", command=back, font=("Helvetica", 16), fg="black", bg="lightgreen")
Back_button.grid(row=8, column=1, padx=10, pady=10)

window.mainloop()
