from tkinter import *
import sqlite3
import tkinter.messagebox as msg

window = Tk()
window.geometry('900x600')
window.title("Shifa Medical Management System")
window.iconbitmap('icon.ico')
# Background image
reg_image = PhotoImage(file="register_bg.png")
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Top Heading Frame
TopHeadingFrame = Frame(window, width=700, bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame, text="Shifa Medical Management System - Register", 
                     font=("Helvetica", 18), fg="blue", bg="white")
HeadingLabel.grid(row=0, column=0, padx=1, pady=1)

# Mid Frame
MidFrame = Frame(window, width=600, bd=1)
MidFrame.pack(side=TOP)

# Database connection and table creation
conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS 'userdata'
               (Name TEXT, ID INT, UserName TEXT, Password TEXT, Mobile TEXT, Email TEXT)""")
conn.commit()

# Name Label and Textbox
name = StringVar()
name.set("")
NameLabel = Label(MidFrame, text="Name", font=("Helvetica", 12), fg="blue", bg="white")
NameLabel.grid(row=0, column=0, padx=1, pady=1)
NameTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=name)
NameTextBox.grid(row=0, column=1, padx=1, pady=1)

# ID Label and Textbox
id = IntVar()
id.set("")
idLabel = Label(MidFrame, text="ID", font=("Helvetica", 16), fg="blue", bg="white")
idLabel.grid(row=1, column=0, padx=1, pady=1)
idTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=id)
idTextBox.grid(row=1, column=1, padx=1, pady=1)

# Username Label and Textbox
username = StringVar()
username.set("")
usernameLabel = Label(MidFrame, text="Username", font=("Helvetica", 16), fg="blue", bg="white")
usernameLabel.grid(row=2, column=0, padx=1, pady=1)
usernameTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=username)
usernameTextBox.grid(row=2, column=1, padx=1, pady=1)

# Password Label and Textbox
password = StringVar()
password.set("")
passwordLabel = Label(MidFrame, text="Password", font=("Helvetica", 16), fg="blue", bg="white")
passwordLabel.grid(row=3, column=0, padx=1, pady=1)
passwordTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=password, show='*')
passwordTextBox.grid(row=3, column=1, padx=1, pady=1)

# Mobile Label and Textbox
mobile = StringVar()
mobile.set("")
mobileLabel = Label(MidFrame, text="Mobile", font=("Helvetica", 16), fg="blue", bg="white")
mobileLabel.grid(row=4, column=0, padx=1, pady=1)
mobileTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=mobile)
mobileTextBox.grid(row=4, column=1, padx=1, pady=1)

# Email Label and Textbox
email = StringVar()
email.set("")
emailLabel = Label(MidFrame, text="Email", font=("Helvetica", 16), fg="blue", bg="white")
emailLabel.grid(row=5, column=0, padx=1, pady=1)
emailTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=email)
emailTextBox.grid(row=5, column=1, padx=1, pady=1)

# Register function
def register():
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO 'userdata'
               (Name, ID, UserName, Password, Mobile, Email) VALUES(?,?,?,?,?,?)""",
               (name.get(), id.get(), username.get(), password.get(), mobile.get(), email.get()))
    conn.commit()
    
    if cursor.rowcount > 0:
        msg.showinfo("Confirmation", "New User Added", icon="info")
    else:
        msg.showinfo("Error", "New User Not Added", icon="warning")

# Login function
def login():
    window.destroy()
    import login

# Submit Button
submit_button = Button(MidFrame, text="Submit", command=register, font=("Helvetica", 16), fg="black", bg="green")
submit_button.grid(row=6, column=1, padx=1, pady=1)

# Already a User Label and Login Button
alreadyuserLabel = Label(MidFrame, text="Already a user?", font=("Helvetica", 16), fg="blue", bg="white")
alreadyuserLabel.grid(row=7, column=0, padx=1, pady=1)

login_button = Button(MidFrame, text="Login", command=login, font=("Helvetica", 16), fg="black", bg="pink")
login_button.grid(row=7, column=1, padx=1, pady=1)

window.config()
window.mainloop()
