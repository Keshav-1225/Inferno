import tkinter as tk
from tkinter import messagebox

def get_ascii():
    try:
        user_input = entry.get()
        ascii_code = int(user_input)
        if 0 <= ascii_code <= 127:
            char = chr(ascii_code)
            result_label.config(text=f'ASCII Character: {char}', fg='green')
        else:
            result_label.config(text='Error: Enter a number between 0 and 127', fg='red')
    except ValueError:
        result_label.config(text='Error: Please enter a valid integer', fg='red')

# Create main window
root = tk.Tk()
root.title("ASCII Finder")
root.geometry("300x200")


# Label
label = tk.Label(root, text="Enter an ASCII Code (0-127):", font=("Arial", 32))
label.pack(pady=10)

# Entry widget
entry = tk.Entry(root, font=("Arial", 32))
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Get ASCII Character", command=get_ascii, font=("Arial", 12))
button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 32))
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
