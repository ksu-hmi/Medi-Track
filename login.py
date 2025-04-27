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
HeadingLabel = Label(TopHeadingFrame, text="MediTrack Management System - Login",
                     font=("Helvetica", 18), fg="blue", bg="white")
HeadingLabel.grid(row=0, column=0, padx=1, pady=1)

MidFrame = Frame(window, width=600, bd=1)
MidFrame.pack(side=TOP)

# Username Label and Textbox
username = StringVar()
username.set("")
usernameLabel = Label(MidFrame, text="Username", font=("Helvetica", 16), fg="blue", bg="white")
usernameLabel.grid(row=0, column=0, padx=1, pady=1)
usernameTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=username)
usernameTextBox.grid(row=0, column=1, padx=1, pady=1)  # Adjusted row and column

# Password Label and Textbox
password = StringVar()
password.set("")
passwordLabel = Label(MidFrame, text="Password", font=("Helvetica", 16), fg="blue", bg="white")
passwordLabel.grid(row=1, column=0, padx=1, pady=1)
passwordTextBox = Entry(MidFrame, font=("Helvetica", 16), textvariable=password, show='*')
passwordTextBox.grid(row=1, column=1, padx=1, pady=1)

def register():
    window.destroy()
    import  register
def login():
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute("""select * from "userdata" where 
    UserName =? and Password = ?""",(username.get(),password.get()))
    if len(list(cursor.fetchall()))>0:
        msg.showinfo("Login Confirmation","Login Successfull",icon='info')
        window.destroy()
        import home
    else:
        msg.showinfo("Login Error","User not defined",icon="warning")

# Submit Button
submit_button = Button(MidFrame, text="Register", command=register, font=("Helvetica", 16), fg="black", bg="green")
submit_button.grid(row=3, column=1, padx=1, pady=1)

# Already a User Label and Login Button
notuserLabel = Label(MidFrame, text="Not user yet?", font=("Helvetica", 16), fg="blue", bg="white")
notuserLabel.grid(row=3, column=0, padx=1, pady=1)

login_button = Button(MidFrame, text="Login", command=login, font=("Helvetica", 16), fg="black", bg="pink")
login_button.grid(row=2, column=1, padx=1, pady=1)

window.mainloop()
