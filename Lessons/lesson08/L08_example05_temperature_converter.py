# Exempel på ett fungerande program i tkinter.
# Väldigt inspirerat av exempel hittade på nätet.

import tkinter as tk


def convert_temperature():
    """Funktion för att konvertera temperaturer i Celsius till Fahrenheit."""
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        result_label.config(text=f"{celsius}°C = {fahrenheit:.1f}°F")
        error_label.config(text="")
    except ValueError:
        error_label.config(text="Vänligen skriv in en siffra!")
        result_label.config(text="")

def is_valid_number(value):
    """Funktion för att kontrollera att fältet enbart innehåller
    siffror eller ingenting."""
    return value.isdigit() or value == ""


# Skapa fönstret precis som tidigare
root = tk.Tk()
root.title("Temperaturomvandlare")
root.geometry("400x250")

# Vi skapar en ram för att lättare få alla Widgets där vi vill ha dem.
frame = tk.Frame(
    root,
    padx=20,
    pady=20,
    )
frame.pack()

# Vi skapar en Label för titeln. Vi använder grid() för att lättare organisera
# våra Widgets på ett snyggt sätt.
title_label = tk.Label(
    frame,
    text="Temperaturomvandlare",
    font=("Arial", 14, "bold"),
    )
title_label.grid(row=0, column=0, columnspan=2, pady=10)


# En Label för instruktioner. Notera att vi specificerar att Label:n ska vara
# fäst till vänstra kanten av vår Frame.
instruction_label = tk.Label(
    frame,
    text="Skriv in en temperatur i grader Celsius:",
    )
instruction_label.grid(row=1, column=0, sticky="w", pady=5)


# Ett textfält för inmatning från användaren. Argumenten validate och
# validatecommand ser till att det enbart är siffror som skrivs in i fältet.
# Se SubjectExamples/Validation_in_tkinter_Entry.py för mer om validering.
celsius_entry = tk.Entry(
    frame,
    width=10,
    validate="key",
    validatecommand=(root.register(is_valid_number), "%P"),
    )
celsius_entry.grid(row=1, column=1, pady=5)

# Här gör jag så att textfältet är markerat när programmet startas.
celsius_entry.focus()

# Här "binder" jag Event:et "Return", alltså ett tryck på tangenten som vi
# kallar för enter, till att convert_temperature() ska köras.
# Notera! Det är enbart om textrutan är markerad som programmet reagerar på
# denna bindning.
celsius_entry.bind("<Return>", lambda event: convert_temperature())

# Vi skapar en knapp som kör konverteringsfunktionen. Notera vad som händer
# om man har med den bortkommenterade kodbiten.
convert_button = tk.Button(
    frame,
    text="Konvertera",
    command=convert_temperature,
    )
convert_button.grid(row=2, column=0, columnspan=2, pady=10)  # , sticky = "ew")


# Labels för resultatet samt felmeddelanden
result_label = tk.Label(
    frame,
    text="",
    font=("Arial", 12),
    )
result_label.grid(row=3, column=0, columnspan=2, pady=5)

error_label = tk.Label(
    frame,
    text="",
    fg="red",
    )
error_label.grid(row=4, column=0, columnspan=2, pady=5)


root.mainloop()