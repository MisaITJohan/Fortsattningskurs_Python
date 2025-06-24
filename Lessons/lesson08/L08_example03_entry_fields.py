# Working with text entry fields

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Entry Example")
root.geometry("400x300")

# Function to handle button click
def greet_user():
    name = name_entry.get()  # Get text from entry field
    if name:
        greeting_label.config(text=f"Hello, {name}!")
    else:
        greeting_label.config(text="Please enter your name!")

# Add a label
instruction_label = tk.Label(root, text="Please enter your name:")
instruction_label.pack(pady=10)

# Add an entry field
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=10)

# Add a button
greet_button = tk.Button(root, text="Greet Me!", command=greet_user)
greet_button.pack(pady=10)

# Add a label to show greeting
greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)

# Start the main event loop
root.mainloop()