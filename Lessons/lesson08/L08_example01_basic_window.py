# Creating a basic window with Tkinter

# Import the tkinter library
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set the window title
root.title("My First GUI")

# Set the window size (width x height)
root.geometry("400x300")

# Add a label with text
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)  # Add some padding

# Start the main event loop
# This keeps the window open and responsive
root.mainloop()