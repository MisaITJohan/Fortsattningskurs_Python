# Exempel på knappar och hur de kan köra funktioner.
# Även ett exempel på hur man använder strängar för att skapa dokumentation.

import tkinter as tk

root = tk.Tk()
root.title("Knappexempel")
root.geometry("400x300")

# Vi skapar en variabel för att räkna klick på vår knapp
counter = 0

def button_clicked():
    """En funktion som ökar counter och ändrar text-egenskapen på result_label"""
    global counter  # Utan denna så skapas en ny counter-variabel i funktionen
    counter += 1
    result_label.config(text=f"Du har tryckt på knappen {counter} gång"
                             f"{"" if counter == 1 else "er"}!")


instruction_label = tk.Label(root, text="Tryck på knappen:")
instruction_label.pack(pady=10)


# Skapa en knapp och ställ in egenskapen command.
# command ska peka på en funktion. Notera att jag inte lägger till några
# parenteser då funktionen inte ska köras när knappen skapas.
button = tk.Button(root, text="Klicka på mig!", command=button_clicked)
button.pack(pady=10)


# Denna Label blir konfigurerad av button_clicked()
result_label = tk.Label(root, text="Du har tryckt på knappen 0 gånger!")
result_label.pack(pady=10)

root.mainloop()