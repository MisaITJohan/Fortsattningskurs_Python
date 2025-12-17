# Working with text entry fields

import tkinter as tk

root = tk.Tk()
root.title("Exempel på textinmatningsfält")
root.geometry("400x300")


def greet_user():
    """Funktion för att hämta texten i textrutan och, om det står något där,
    hälsa på användaren."""
    name = name_entry.get()
    if name:
        greeting_label.config(
            text=f"Hej {name}!",
            )
    else:
        greeting_label.config(
            text="Vänligen skriv ditt namn!",
            )

# Label för instruktioner till användaren
instruction_label = tk.Label(
    root,
    text="Vänligen skriv ditt namn:",
    )
instruction_label.pack(pady=10)


# Vi skapar ett textfält och ger det en bredd på 30 tecken
# Man kan skriva in fler tecken än så, bredden är bara visuell.
name_entry = tk.Entry(
    root,
    width=30,
    )
name_entry.pack(pady=10)

greet_button = tk.Button(
    root,
    text="Hälsa på mig!",
    command=greet_user,
    )
greet_button.pack(pady=10)

greeting_label = tk.Label(
    root,
    text="",
    )
greeting_label.pack(pady=10)

root.mainloop()