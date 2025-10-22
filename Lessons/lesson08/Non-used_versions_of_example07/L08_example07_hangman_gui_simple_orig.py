# Creating a GUI version of the Hangman game

import tkinter as tk
import random

# A simplified version of the HangmanGame class for GUI implementation
class HangmanGameGUI:
    def __init__(self, master, possible_words=None, allowed_guesses=6):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("500x400")
        self.master.configure(bg="#f0f0f0")

        # Game variables
        if possible_words is None:
            self.possible_words = ["apa", "banan", "cacao", "dans", "elefant"]
        else:
            self.possible_words = possible_words

        self.allowed_guesses = allowed_guesses
        self.incorrect_guesses_made = 0
        self.word_to_guess = ""
        self.guessed_letters = set()
        self.game_finished = False

        # Create the GUI elements
        self.create_widgets()

        # Start a new game
        self.setup_new_game()

    def create_widgets(self):
        # Title frame
        self.title_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.title_frame.pack(pady=10)

        self.title_label = tk.Label(self.title_frame, text="Hangman", 
                                   font=("Arial", 20, "bold"), bg="#f0f0f0")
        self.title_label.pack()

        # Game info frame
        self.info_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.info_frame.pack(pady=10)

        self.word_display = tk.Label(self.info_frame, text="", 
                                    font=("Courier", 18), bg="#f0f0f0")
        self.word_display.pack(pady=5)

        self.guesses_left_label = tk.Label(self.info_frame, text="", 
                                         font=("Arial", 12), bg="#f0f0f0")
        self.guesses_left_label.pack(pady=5)

        self.guessed_letters_label = tk.Label(self.info_frame, text="", 
                                           font=("Arial", 12), bg="#f0f0f0")
        self.guessed_letters_label.pack(pady=5)

        # Message area
        self.message_label = tk.Label(self.info_frame, text="", 
                                    font=("Arial", 12), fg="blue", bg="#f0f0f0")
        self.message_label.pack(pady=10)

        # Input frame
        self.input_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.input_frame.pack(pady=10)

        self.guess_label = tk.Label(self.input_frame, text="Gissa en bokstav:", 
                                  font=("Arial", 12), bg="#f0f0f0")
        self.guess_label.grid(row=0, column=0, padx=5)

        self.guess_entry = tk.Entry(self.input_frame, width=3, font=("Arial", 12))
        self.guess_entry.grid(row=0, column=1, padx=5)
        self.guess_entry.bind('<Return>', lambda event: self.make_guess())

        self.guess_button = tk.Button(self.input_frame, text="Gissa", 
                                    command=self.make_guess, font=("Arial", 12))
        self.guess_button.grid(row=0, column=2, padx=5)

        # Control buttons frame
        self.control_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.control_frame.pack(pady=20)

        self.new_game_button = tk.Button(self.control_frame, text="Nytt spel", 
                                       command=self.setup_new_game, font=("Arial", 12))
        self.new_game_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(self.control_frame, text="Avsluta", 
                                    command=self.master.destroy, font=("Arial", 12))
        self.quit_button.pack(side=tk.LEFT, padx=10)

    def setup_new_game(self):
        # Reset game state
        self.incorrect_guesses_made = 0
        self.guessed_letters.clear()
        self.game_finished = False

        # Choose a new word
        self.word_to_guess = random.choice(self.possible_words)

        # Update display
        self.update_word_display()
        self.update_guesses_left()
        self.update_guessed_letters()
        self.message_label.config(text="Nytt spel har startat!")

        # Reset and focus entry field
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def update_word_display(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        self.word_display.config(text=display)

    def update_guesses_left(self):
        guesses_left = self.allowed_guesses - self.incorrect_guesses_made
        self.guesses_left_label.config(
            text=f"Du har {guesses_left} gissningar kvar."
        )

    def update_guessed_letters(self):
        if self.guessed_letters:
            letters = ", ".join(sorted(self.guessed_letters))
            self.guessed_letters_label.config(
                text=f"Gissade bokstäver: {letters}"
            )
        else:
            self.guessed_letters_label.config(text="Inga gissade bokstäver än.")

    def make_guess(self):
        if self.game_finished:
            self.message_label.config(
                text="Spelet är slut. Starta ett nytt spel!",
                fg="red"
            )
            return

        # Get the guess from the entry field
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        # Validate the guess
        if not guess or len(guess) != 1 or not guess.isalpha():
            self.message_label.config(
                text="Vänligen ange en bokstav!",
                fg="red"
            )
            return

        if guess in self.guessed_letters:
            self.message_label.config(
                text=f"Du har redan gissat på {guess}!",
                fg="red"
            )
            return

        # Add the guess to guessed letters
        self.guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in self.word_to_guess:
            self.message_label.config(
                text=f"{guess.upper()} finns i ordet!",
                fg="green"
            )
            self.check_game_won()
        else:
            self.incorrect_guesses_made += 1
            self.message_label.config(
                text=f"{guess.upper()} finns inte i ordet!",
                fg="red"
            )
            self.check_game_over()

        # Update the display
        self.update_word_display()
        self.update_guesses_left()
        self.update_guessed_letters()

        # Reset focus to entry field
        self.guess_entry.focus()

    def check_game_won(self):
        for letter in self.word_to_guess:
            if letter not in self.guessed_letters:
                return

        self.game_finished = True
        self.message_label.config(
            text=f"Grattis! Du vann! Ordet var '{self.word_to_guess}'.",
            fg="green"
        )

    def check_game_over(self):
        if self.incorrect_guesses_made >= self.allowed_guesses:
            self.game_finished = True
            self.message_label.config(
                text=f"Game over! Ordet var '{self.word_to_guess}'.",
                fg="red"
            )
            self.word_display.config(text=self.word_to_guess)

# Main function to run the game
def main():
    root = tk.Tk()
    hangman_game = HangmanGameGUI(root)
    root.mainloop()

# Run the game if this file is executed directly
if __name__ == "__main__":
    main()
