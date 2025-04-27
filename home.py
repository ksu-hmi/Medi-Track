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
HeadingLabel = Label(TopHeadingFrame, text="Shifa Medical Management System - Home",
                     font=("Helvetica", 18), fg="blue", bg="white")
HeadingLabel.grid(row=0, column=0, padx=10, pady=10)

MidFrame = Frame(window, width=600, bd=1)
MidFrame.pack(side=TOP)

def add():
    try:
        window.destroy()
        import add_medicine
    except ModuleNotFoundError:
        msg.showerror("Error", "The module 'add_medicine' could not be found.")

def view():
    try:
        window.destroy()
        import view_medicine
    except ModuleNotFoundError:
        msg.showerror("Error", "The module 'view_medicine' could not be found.")

def search():
    try:
        window.destroy()
        import search_medicine
    except ModuleNotFoundError:
        msg.showerror("Error", "The module 'search_medicine' could not be found.")

def delete():
    try:
        window.destroy()
        import delete_medicine
    except ModuleNotFoundError:
        msg.showerror("Error", "The module 'delete_medicine' could not be found.")

def logout():
    if msg.askyesno("Logout", "Are you sure you want to logout?"):
        try:
            window.destroy()
            import login
        except ModuleNotFoundError:
            msg.showerror("Error", "The module 'login' could not be found.")

# Buttons
add_button = Button(MidFrame, text="Add Medicine", command=add, font=("Helvetica", 16), fg="black", bg="pink")
add_button.grid(row=0, column=1, padx=10, pady=10)

view_button = Button(MidFrame, text="View Medicine", command=view, font=("Helvetica", 16), fg="black", bg="pink")
view_button.grid(row=1, column=1, padx=10, pady=10)

search_button = Button(MidFrame, text="Search Medicine", command=search, font=("Helvetica", 16), fg="black", bg="pink")
search_button.grid(row=2, column=1, padx=10, pady=10)

delete_button = Button(MidFrame, text="Delete Medicine", command=delete, font=("Helvetica", 16), fg="black", bg="pink")
delete_button.grid(row=3, column=1, padx=10, pady=10)

login_button = Button(MidFrame, text="Logout", command=logout, font=("Helvetica", 16), fg="black", bg="pink")
login_button.grid(row=4, column=1, padx=10, pady=10)

window.mainloop()
