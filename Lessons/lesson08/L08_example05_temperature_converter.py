# Temperature converter application

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x250")

# Function to convert Celsius to Fahrenheit
def convert_temperature():
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit:.1f}°F")
        error_label.config(text="")
    except ValueError:
        error_label.config(text="Please enter a valid number!")
        result_label.config(text="")

# Create a frame for better organization
frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

# Add a title label
title_label = tk.Label(frame, text="Temperature Converter", font=("Arial", 14, "bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Add an instruction label
instruction_label = tk.Label(frame, text="Enter temperature in Celsius:")
instruction_label.grid(row=1, column=0, sticky="w", pady=5)

# Add an entry field
celsius_entry = tk.Entry(frame, width=10)
celsius_entry.grid(row=1, column=1, pady=5)

# Add a convert button
convert_button = tk.Button(frame, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

# Add a label for results
result_label = tk.Label(frame, text="", font=("Arial", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Add a label for error messages
error_label = tk.Label(frame, text="", fg="red")
error_label.grid(row=4, column=0, columnspan=2, pady=5)

# Start the main event loop
root.mainloop()