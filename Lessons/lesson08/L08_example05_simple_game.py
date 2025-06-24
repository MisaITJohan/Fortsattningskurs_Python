# Simple clicker game with Tkinter

import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Cookie Clicker Game")
root.geometry("400x400")

# Game variables
score = 0
click_value = 1

# Function to handle clicking the cookie
def click_cookie():
    global score
    score += click_value
    score_label.config(text=f"Score: {score}")
    
    # Randomly change the cookie position slightly
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    cookie_button.place(x=cookie_button.winfo_x() + x, y=cookie_button.winfo_y() + y)

# Function to upgrade the click value
def upgrade_click():
    global click_value, score
    
    if score >= 10:
        score -= 10
        click_value += 1
        score_label.config(text=f"Score: {score}")
        click_value_label.config(text=f"Click Value: {click_value}")
    else:
        status_label.config(text="Not enough points! Need 10 points.")

# Create frames
header_frame = tk.Frame(root)
header_frame.pack(pady=10)

game_frame = tk.Frame(root)
game_frame.pack(pady=20)

# Add score label
score_label = tk.Label(header_frame, text="Score: 0", font=("Arial", 14))
score_label.pack()

# Add click value label
click_value_label = tk.Label(header_frame, text="Click Value: 1", font=("Arial", 12))
click_value_label.pack()

# Add cookie button
cookie_button = tk.Button(game_frame, text="🍪", font=("Arial", 40), command=click_cookie)
cookie_button.pack(pady=20)

# Add upgrade button
upgrade_button = tk.Button(game_frame, text="Upgrade (Cost: 10 points)", command=upgrade_click)
upgrade_button.pack(pady=10)

# Add status label
status_label = tk.Label(game_frame, text="", fg="red")
status_label.pack(pady=10)

# Instructions
instructions = tk.Label(root, text="Click the cookie to earn points.\nUpgrade to get more points per click!")
instructions.pack(side=tk.BOTTOM, pady=20)

# Start the main event loop
root.mainloop()