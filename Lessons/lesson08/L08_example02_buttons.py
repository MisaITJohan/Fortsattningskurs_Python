# Working with buttons in Tkinter

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Button Example")
root.geometry("400x300")

# Create a counter variable
counter = 0

# Function to handle button click
def button_clicked():
    global counter
    counter += 1
    result_label.config(text=f"Button clicked {counter} times!")

# Add a label
instruction_label = tk.Label(root, text="Click the button below:")
instruction_label.pack(pady=10)

# Add a button
button = tk.Button(root, text="Click Me!", command=button_clicked)
button.pack(pady=10)

# Add a label to show results
result_label = tk.Label(root, text="Button clicked 0 times!")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()