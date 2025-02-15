
import tkinter as tk
from tkinter import messagebox

def check_password():
    if entry.get() == "04818R3X":
        messagebox.showinfo("Success", "Congrats! You saved the world")
    else:
        messagebox.showerror("Error", "Incorrect password")

app = tk.Tk()
app.title("Password Checker")
label = tk.Label(app, text="Enter Password:")
label.pack(pady=100)

entry = tk.Entry(app, show="*")
entry.pack(pady=10)

button = tk.Button(app, text="Submit", command=check_password)
button.pack(pady=10)

label.config(font=("Arial", 30))
label.pack(pady=20)
entry.config(font=("Arial", 14),width=40)
button.config(font=("Arial", 14))

def check_password_and_close():
    if entry.get() == "04818R3X":
        messagebox.showinfo("Success", "Congrats! You saved the world")
        app.destroy()
    else:
        messagebox.showerror("Error", "Incorrect password")

button.config(command=check_password_and_close)
app.bind('<Return>', lambda event: check_password_and_close())

# Center the window
app.update_idletasks()
width = app.winfo_width()
height = app.winfo_height()
x = (app.winfo_screenwidth() // 2) - (width // 2)
y = (app.winfo_screenheight() // 2) - (height // 2)
app.geometry(f'{width}x{height}+{x}+{y}')

app.mainloop()
