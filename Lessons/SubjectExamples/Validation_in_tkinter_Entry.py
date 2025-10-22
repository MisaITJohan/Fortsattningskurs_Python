# Med hjälp av argumenten validation_function, validatecommand och
#   invalidcommand kan man kontrollera vad som användaren skriver in i realtid.


# invalidcommand() är frivillig att använda, även utan det argumentet så
#   accepteras inte en ogiltig inmatning.

import tkinter as tk

# -------------------------------
# Funktion som kontrollerar inmatning
# -------------------------------
# Den här funktionen används för att kontrollera vad användaren skriver i textfältet.
# Den kontrollerar om texten bara innehåller siffror eller är tom.
# Den ändrar också bakgrundsfärgen i textfältet som visuell återkoppling.
# I detta exempel tillåts endast siffror (0–9) eller tomt fält.
def only_numbers_or_blank(new_text):
    if new_text.isdigit() or new_text == "":
        entry.config(bg="lightgreen")  # Giltig inmatning
        return True
    else:
        entry.config(bg="lightcoral")  # Ogiltig inmatning
        return False

# -------------------------------
# Skapa huvudfönstret
# -------------------------------
root = tk.Tk()
root.title("Valideringsexempel")
root.geometry("300x150")

# -------------------------------
# Instruktion till användaren
# -------------------------------
# En tydlig etikett som förklarar vad användaren ska göra.
instruction_label = tk.Label(
    root,
    text="Skriv bara siffror:",
    font=("Arial", 12),
    )
instruction_label.pack(pady=10)

# -------------------------------
# Registrera valideringsfunktionen
# -------------------------------
# Tkinter kräver att man registrerar Python-funktionen innan den används som
#   validatecommand.
# "%P" är en specialkod som betyder: skicka den nya texten till funktionen.
# Namnet är godtyckligt valt.
validation_function = (root.register(only_numbers_or_blank), "%P")

# -------------------------------
# Skapa textfält med validering
# -------------------------------
# Här skapas ett textfält (Entry) där användaren skriver in text.
# validate="key" betyder att validering sker vid varje tangenttryck.
# validatecommand=validation_function kopplar vår funktion till textfältet.
# invalidcommand definierar vilken funktion som ska köras om något ogiltigt
#   skrivs in.
entry = tk.Entry(
    root,
    validate="key",
    validatecommand=validation_function,
    invalidcommand=lambda: entry.config(fg="red"),
    font=("Arial", 12),
    bg="white",
    )
entry.pack(pady=5)

# -------------------------------
# Starta programmet
# -------------------------------
# mainloop håller fönstret öppet och lyssnar på användarens interaktioner.
root.mainloop()
