import tkinter as tk
import pathlib
import random

# This class implements a GUI version of the Hangman game
# Based on the functionality of the original HangmanGame class
class HangmanGameGUI:
    def __init__(self, master, wordlist=None, allowed_guesses=5):
        # Setup main window
        self.master = master
        self.master.title("Hangman Spel")
        self.master.geometry("600x500")
        self.master.configure(bg="#f0f0f0")

        # Game variables (matching the original HangmanGame)
        self.possible_words = None
        self.fetch_words(wordlist)
        self.allowed_guesses = allowed_guesses
        self.incorrect_guesses_made = 0
        self.word_to_guess = ""
        self.guessed_letters = set()
        self.current_guess = ""
        self.game_finished = False

        # Create the GUI elements
        self.create_widgets()

        # Start a new game
        self.setup()

    def create_widgets(self):
        # Title frame
        self.title_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.title_frame.pack(pady=10)

        self.title_label = tk.Label(self.title_frame, text="Hangman", 
                                   font=("Arial", 24, "bold"), bg="#f0f0f0")
        self.title_label.pack()

        # Game info frame
        self.info_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.info_frame.pack(pady=10)

        # Word length info
        self.word_length_label = tk.Label(self.info_frame, text="", 
                                       font=("Arial", 12), bg="#f0f0f0")
        self.word_length_label.pack(pady=5)

        # Display the current word with placeholders
        self.word_display = tk.Label(self.info_frame, text="", 
                                    font=("Courier", 18), bg="#f0f0f0")
        self.word_display.pack(pady=10)

        # Guesses information
        self.guesses_left_label = tk.Label(self.info_frame, text="", 
                                         font=("Arial", 12), bg="#f0f0f0")
        self.guesses_left_label.pack(pady=5)

        self.guessed_letters_label = tk.Label(self.info_frame, text="", 
                                           font=("Arial", 12), bg="#f0f0f0")
        self.guessed_letters_label.pack(pady=5)

        self.correct_guesses_label = tk.Label(self.info_frame, text="", 
                                            font=("Arial", 12), bg="#f0f0f0")
        self.correct_guesses_label.pack(pady=5)

        # Message area for game feedback
        self.message_label = tk.Label(self.info_frame, text="", 
                                    font=("Arial", 12, "bold"), fg="blue", bg="#f0f0f0")
        self.message_label.pack(pady=10)

        # Input frame
        self.input_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.input_frame.pack(pady=10)

        self.guess_label = tk.Label(self.input_frame, 
                                  text="Gissa en bokstav eller lämna tomt för att avsluta omgången:", 
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
                                       command=self.setup, font=("Arial", 12))
        self.new_game_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(self.control_frame, text="Avsluta", 
                                    command=self.master.destroy, font=("Arial", 12))
        self.quit_button.pack(side=tk.LEFT, padx=10)

    def fetch_words(self, target=None):
        """Load words from a file, matching the original implementation"""
        # First try to use the provided wordlist
        if target is not None:
            try:
                with open(target, "r", encoding="utf-8") as file:
                    self.possible_words = [x.strip() for x in file.readlines()]
                return
            except (FileNotFoundError, IOError):
                pass  # Fall back to default if file not found

        # Then try to use the default wordlist path
        try:
            default_path = pathlib.Path("../wordlist_creator/wordlist.txt")
            with open(default_path, "r", encoding="utf-8") as file:
                self.possible_words = [x.strip() for x in file.readlines()]
        except (FileNotFoundError, IOError):
            # Finally, fall back to hardcoded words
            self.possible_words = [
                "apa", "banan", "cacao", "dans", "elefant"
            ]

    def setup(self):
        """Reset and start a new game, matching the original implementation"""
        self.game_finished = False
        self.incorrect_guesses_made = 0
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
            self.guessed_letters.clear()

        # Update display for the new game
        self.update_word_length_label()
        self.update_word_display()
        self.update_guesses_left()
        self.update_guessed_letters()
        self.update_correct_guesses_label()
        self.message_label.config(text="Nytt spel har startat!")

        # Reset and focus entry field
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def get_word_to_guess(self):
        """Choose a random word, matching the original implementation"""
        self.word_to_guess = random.choice(self.possible_words).lower()

    def update_word_length_label(self):
        """Update the label showing word length"""
        self.word_length_label.config(
            text=f"Det hemliga ordet är {len(self.word_to_guess)} tecken långt."
        )

    def update_word_display(self):
        """Update the display of the word with placeholders"""
        # Create a display with underscores for unguessed letters
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        self.word_display.config(text=display)

    def update_guesses_left(self):
        """Update the label showing remaining guesses"""
        guesses_left = self.allowed_guesses - self.incorrect_guesses_made
        self.guesses_left_label.config(
            text=f"Du har {guesses_left} gissningar kvar."
        )

    def update_guessed_letters(self):
        """Update the label showing all guessed letters"""
        if self.guessed_letters:
            sorted_letters = sorted(list(self.guessed_letters))
            self.guessed_letters_label.config(
                text=f"Du har gissat dessa bokstäver: {' '.join(sorted_letters)}"
            )
        else:
            self.guessed_letters_label.config(text="Du har inte gissat några bokstäver än.")

    def update_correct_guesses_label(self):
        """Update the label showing correct guesses"""
        correct_guesses = sorted([x for x in self.guessed_letters if x in self.word_to_guess])
        if correct_guesses:
            self.correct_guesses_label.config(
                text=f"Av de gissade bokstäverna finns dessa i det hemliga ordet: {' '.join(correct_guesses)}"
            )
        else:
            self.correct_guesses_label.config(text="")

    def make_guess(self):
        """Process a player's guess, matching the original implementation"""
        if self.game_finished:
            self.message_label.config(
                text="Spelet är slut. Starta ett nytt spel!",
                fg="red"
            )
            return

        # Get the guess from the entry field
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        # Handle empty guess (quit game)
        if not guess:
            self.game_finished = True
            self.message_label.config(
                text="Spelet avslutades.",
                fg="blue"
            )
            return

        # Check if the guess is valid
        if self.check_invalid(guess):
            self.message_label.config(
                text="Ogiltig gissning! Ange en bokstav som du inte har gissat tidigare.",
                fg="red"
            )
            return

        # Process the valid guess
        self.guessed_letters.add(guess)
        self.current_guess = guess

        # Check if the guess is correct
        if self.check_guess():
            self.correct_guess()
        else:
            self.incorrect_guess()

        # Update the display
        self.update_word_display()
        self.update_guesses_left()
        self.update_guessed_letters()
        self.update_correct_guesses_label()

        # Reset focus to entry field
        self.guess_entry.focus()

    def check_invalid(self, guess):
        """Check if a guess is invalid, matching the original implementation"""
        previously_guessed = guess in self.guessed_letters
        invalid_length = len(guess) != 1
        is_not_letter = not guess.isalpha()

        is_invalid = previously_guessed or invalid_length or is_not_letter

        return is_invalid

    def check_guess(self):
        """Check if the guess is in the word, matching the original implementation"""
        return self.current_guess in self.word_to_guess

    def correct_guess(self):
        """Handle a correct guess, matching the original implementation"""
        self.message_label.config(
            text=f"{self.current_guess.upper()} finns i det hemliga ordet.",
            fg="green"
        )
        self.check_game_won()

    def incorrect_guess(self):
        """Handle an incorrect guess, matching the original implementation"""
        self.message_label.config(
            text=f"{self.current_guess.upper()} finns inte i det hemliga ordet.",
            fg="red"
        )
        self.incorrect_guesses_made += 1
        self.check_game_over()

    def check_game_won(self):
        """Check if the player has won, matching the original implementation"""
        for letter in self.word_to_guess:
            if letter not in self.guessed_letters:
                return

        self.game_finished = True
        self.message_label.config(
            text=f"Du vann! Det hemliga ordet var {self.word_to_guess}.",
            fg="green"
        )

    def check_game_over(self):
        """Check if the player has lost, matching the original implementation"""
        if self.incorrect_guesses_made >= self.allowed_guesses:
            self.game_finished = True
            self.message_label.config(
                text=f"Game over! Det hemliga ordet var {self.word_to_guess}.",
                fg="red"
            )
            # Reveal the word
            self.word_display.config(text=self.word_to_guess)

# Main function to run the game
def main():
    root = tk.Tk()
    hangman_game = HangmanGameGUI(root)
    root.mainloop()

# Run the game if this file is executed directly
if __name__ == "__main__":
    main()