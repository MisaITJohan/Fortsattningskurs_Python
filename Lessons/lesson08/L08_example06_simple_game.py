# Simpelt klickspel med tkinter
# Väldigt inspirerat av exempel hittade på nätet.

import tkinter as tk
import random

root = tk.Tk()
root.title("Cookie Clicker Game")
root.geometry("400x450")

# Spelets variabler
score = 0
click_value = 1

# Funktion för att hantera att kakan klickas på
def click_cookie():
    global score
    score += click_value
    score_label.config(text=f"Score: {score}")
    
    # Slumpvis flytta kakan en liten bit
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    cookie_button.place(x=cookie_button.winfo_x() + x, y=cookie_button.winfo_y() + y)

# Funktion för att öka poäng per klick
def upgrade_click():
    global click_value, score
    
    if score >= 10:
        score -= 10
        click_value += 1
        score_label.config(text=f"Score: {score}")
        click_value_label.config(text=f"Click Value: {click_value}")
    else:
        status_label.config(text="Not enough points! Need 10 points.")


# Skapa ramar
header_frame = tk.Frame(root)
header_frame.pack(pady=10)

game_frame = tk.Frame(root)
game_frame.pack(pady=20)

# Lägg till label för poäng
score_label = tk.Label(
    header_frame,
    text="Score: 0",
    font=("Arial", 14),
    )
score_label.pack()

# Lägg till label för mängden poäng per klick
click_value_label = tk.Label(
    header_frame,
    text="Click Value: 1",
    font=("Arial", 12),
    )
click_value_label.pack()

# Lägg till knappen med kakan
cookie_button = tk.Button(
    game_frame,
    text="🍪",
    font=("Arial", 40),
    command=click_cookie,
    )
cookie_button.pack(pady=20)

# Lägg till knapp för att uppgradera
upgrade_button = tk.Button(
    game_frame,
    text="Upgrade (Cost: 10 points)",
    command=upgrade_click,
    )
upgrade_button.pack(pady=10)

# Lägg til len statuslabel
status_label = tk.Label(
    game_frame,
    text="",
    fg="red",
    )
status_label.pack(pady=10)

# Label med instruktioner
instruction_label = tk.Label(
    root,
    text="Click the cookie to earn points.\nUpgrade to get more points per click!",
    )
instruction_label.pack(side=tk.BOTTOM, pady=20)


root.mainloop()