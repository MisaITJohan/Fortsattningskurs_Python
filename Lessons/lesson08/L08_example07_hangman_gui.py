import tkinter as tk
from tkinter import filedialog
import pathlib
import random
import os

# Constants for UI appearance and configuration
COLORS = {
    "background": "#f0f0f0",
    "success": "green",
    "error": "red",
    "info": "blue"
}

FONTS = {
    "title": ("Arial", 24, "bold"),
    "normal": ("Arial", 12),
    "word": ("Courier", 18),
    "emphasis": ("Arial", 12, "bold")
}

# This class implements a GUI version of the Hangman game
# Based on the functionality of the original HangmanGame class
class HangmanGameGUI:
    def __init__(self, master, wordlist=None, allowed_guesses=5):
        # Setup main window
        self.master = master
        self.master.title("Hangman Spel")
        self.master.geometry("600x550")  # Increased height for wordlist info
        self.master.configure(bg=COLORS["background"])

        # Game state variables 
        self.possible_words = None
        self.allowed_guesses = allowed_guesses
        self.incorrect_guesses_made = 0
        self.word_to_guess = ""
        self.guessed_letters = set()
        self.current_guess = ""
        self.game_finished = False

        # Create widgets first so the wordlist label exists when fetch_words is called
        self.create_widgets()

        # Initialize the game
        self.fetch_words(wordlist)
        self.setup()

    def create_widgets(self):
        self._create_title_section()
        self._create_game_info_section()
        self._create_input_section()
        self._create_control_section()

    def _create_title_section(self):
        """Create the title section of the UI"""
        self.title_frame = tk.Frame(self.master, bg=COLORS["background"])
        self.title_frame.pack(pady=10)

        self.title_label = tk.Label(
            self.title_frame,
            text="Hangman",
            font=FONTS["title"],
            bg=COLORS["background"]
            )
        self.title_label.pack()

    def _create_game_info_section(self):
        """Create the game information display section"""
        self.info_frame = tk.Frame(self.master, bg=COLORS["background"])
        self.info_frame.pack(pady=10)

        # Word length info
        self.word_length_label = tk.Label(
            self.info_frame, text="",
            font=FONTS["normal"],
            bg=COLORS["background"])
        self.word_length_label.pack(pady=5)

        # Display the current word with placeholders
        self.word_display = tk.Label(
            self.info_frame,
            text="",
            font=FONTS["word"],
            bg=COLORS["background"])
        self.word_display.pack(pady=10)

        # Guesses information
        self.guesses_left_label = tk.Label(
            self.info_frame,
            text="",
            font=FONTS["normal"],
            bg=COLORS["background"]
            )
        self.guesses_left_label.pack(pady=5)

        self.guessed_letters_label = tk.Label(
            self.info_frame,
            text="",
            font=FONTS["normal"],
            bg=COLORS["background"]
            )
        self.guessed_letters_label.pack(pady=5)

        self.correct_guesses_label = tk.Label(
            self.info_frame,
            text="",
            font=FONTS["normal"],
            bg=COLORS["background"]
            )
        self.correct_guesses_label.pack(pady=5)

        # Message area for game feedback
        self.message_label = tk.Label(
            self.info_frame,
            text="",
            font=FONTS["emphasis"],
            fg=COLORS["info"],
            bg=COLORS["background"]
            )
        self.message_label.pack(pady=10)

    def _create_input_section(self):
        """Create the user input section"""
        self.input_frame = tk.Frame(self.master, bg=COLORS["background"])
        self.input_frame.pack(pady=10)

        self.guess_label = tk.Label(
            self.input_frame,
            text="Gissa en bokstav eller lämna tomt för att avsluta omgången:",
            font=FONTS["normal"],
            bg=COLORS["background"]
            )
        self.guess_label.grid(row=0, column=0, padx=5)

        self.guess_entry = tk.Entry(self.input_frame, width=3, font=FONTS["normal"])
        self.guess_entry.grid(row=0, column=1, padx=5)
        self.guess_entry.bind('<Return>', lambda event: self.make_guess())

        self.guess_button = tk.Button(
            self.input_frame,
            text="Gissa",
            command=self.make_guess,
            font=FONTS["normal"]
            )
        self.guess_button.grid(row=0, column=2, padx=5)

    def _create_control_section(self):
        """Create the game control buttons section"""
        self.control_frame = tk.Frame(self.master, bg=COLORS["background"])
        self.control_frame.pack(pady=20)

        # Add a button to load a custom wordlist
        self.load_wordlist_button = tk.Button(
            self.control_frame,
            text="Ladda ordlista",
            command=self.load_custom_wordlist,
            font=FONTS["normal"]
            )
        self.load_wordlist_button.pack(side=tk.LEFT, padx=10)

        self.new_game_button = tk.Button(
            self.control_frame,
            text="Nytt spel",
            command=self.setup,
            font=FONTS["normal"]
            )
        self.new_game_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(
            self.control_frame,
            text="Avsluta",
            command=self.master.destroy,
            font=FONTS["normal"]
            )
        self.quit_button.pack(side=tk.LEFT, padx=10)

        # Add a label to show the current wordlist file
        self.wordlist_info_frame = tk.Frame(self.master, bg=COLORS["background"])
        self.wordlist_info_frame.pack(pady=5)

        self.wordlist_label = tk.Label(
            self.wordlist_info_frame,
            text="Använder standardordlista",
            font=(FONTS["normal"][0], 10),
            bg=COLORS["background"])
        self.wordlist_label.pack()

    def load_custom_wordlist(self):
        """Open a file dialog to let the user select a custom word file"""
        # Show file dialog to select a word list file
        file_path = filedialog.askopenfilename(
            title="Välj en ordlistefil",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialdir=os.getcwd()
        )

        if file_path:  # If a file was selected
            words = self._load_from_file(file_path)
            if words:  # If the file contained valid words
                self.possible_words = words
                # Update the wordlist label with the filename
                filename = os.path.basename(file_path)
                self.wordlist_label.config(text=f"Använder ordlista: {filename}")
                # Start a new game with the new wordlist
                self.show_message(f"Ordlista laddad: {len(words)} ord", "info")
                self.setup()
            else:
                self.show_message("Kunde inte läsa från den valda filen.", "error")

    def fetch_words(self, target=None):
        """Load words from a file with fallback options"""
        # Default wordlist if all else fails
        default_words = ["apa", "banan", "cacao", "dans", "elefant"]

        # Try loading from different sources in order of priority
        sources = [
            # 1. Custom provided path
            lambda: self._load_from_file(target) if target else None,
            # 2. Default wordlist path
            lambda: self._load_from_file(pathlib.Path("wordlist_creator/wordlist.txt")),
            # 3. Fallback to hardcoded list
            lambda: default_words
        ]

        # Try each source until we get a valid wordlist
        for source in sources:
            result = source()
            if result:
                self.possible_words = result
                # If using the default words, update the label
                if result == default_words:
                    self.wordlist_label.config(text="Använder standardordlista")
                return

    def _load_from_file(self, file_path):
        """Helper method to load words from a file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return [x.strip() for x in file.readlines()]
        except (FileNotFoundError, IOError):
            return None

    def setup(self):
        """Reset and start a new game"""
        # Reset game state
        self.game_finished = False
        self.incorrect_guesses_made = 0
        self.guessed_letters.clear()
        self.get_word_to_guess()

        # Update all UI elements
        self._update_all_displays()
        self.message_label.config(text="Nytt spel har startat!", fg=COLORS["info"])

        # Reset and focus entry field
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def _update_all_displays(self):
        """Update all display elements at once"""
        self.update_word_length_label()
        self.update_word_display()
        self.update_guesses_left()
        self.update_guessed_letters()
        self.update_correct_guesses_label()

    def get_word_to_guess(self):
        """Choose a random word from the available words"""
        self.word_to_guess = random.choice(self.possible_words).lower()

    def update_word_length_label(self):
        """Update the label showing word length"""
        self.word_length_label.config(
            text=f"Det hemliga ordet är {len(self.word_to_guess)} tecken långt."
        )

    def update_word_display(self):
        """Update the display of the word with placeholders"""
        # Create a display with underscores for unguessed letters
        display = self._get_word_with_placeholders()
        self.word_display.config(text=display)

    def _get_word_with_placeholders(self):
        """Helper method to format the word display with placeholders"""
        display_chars = []
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display_chars.append(letter + " ")
            else:
                display_chars.append("_ ")
        return "".join(display_chars)

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
            text = f"Du har gissat dessa bokstäver: {' '.join(sorted_letters)}"
        else:
            text = "Du har inte gissat några bokstäver än."
        self.guessed_letters_label.config(text=text)

    def update_correct_guesses_label(self):
        """Update the label showing correct guesses"""
        correct_guesses = self._get_correct_guesses()
        if correct_guesses:
            text = (f"Av de gissade bokstäverna finns dessa i det hemliga ordet: "
                    f"{' '.join(correct_guesses)}")
        else:
            text = ""
        self.correct_guesses_label.config(text=text)

    def _get_correct_guesses(self):
        """Helper method to get sorted list of correct guesses"""
        return sorted([letter for letter in self.guessed_letters if letter in self.word_to_guess])

    def make_guess(self):
        """Process a player's guess"""
        # Check if game is already finished
        if self.game_finished:
            self.show_message("Spelet är slut. Starta ett nytt spel!", "error")
            return

        # Get and clear the guess from the entry field
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        # Handle different guess scenarios
        if not guess:
            self._handle_empty_guess()
        elif self.check_invalid(guess):
            self._handle_invalid_guess()
        else:
            self._process_valid_guess(guess)

        # Reset focus to entry field
        self.guess_entry.focus()

    def _handle_empty_guess(self):
        """Handle when player submits an empty guess (quits game)"""
        self.game_finished = True
        self.show_message("Spelet avslutades.", "info")

    def _handle_invalid_guess(self):
        """Handle when player submits an invalid guess"""
        self.show_message(
            "Ogiltig gissning! Ange en bokstav som du inte har gissat tidigare.", 
            "error"
        )

    def _process_valid_guess(self, guess):
        """Process a valid guess"""
        # Record the guess
        self.guessed_letters.add(guess)
        self.current_guess = guess

        # Check if guess is correct and handle accordingly
        if self.check_guess():
            self.correct_guess()
        else:
            self.incorrect_guess()

        # Update all displays
        self._update_all_displays()

    def show_message(self, message, message_type="info"):
        """Display a message with appropriate styling"""
        self.message_label.config(text=message, fg=COLORS[message_type])

    def check_invalid(self, guess):
        """Check if a guess is invalid"""
        validations = [
            guess in self.guessed_letters,  # previously guessed
            len(guess) != 1,               # not a single character
            not guess.isalpha()            # not a letter
        ]
        return any(validations)

    def check_guess(self):
        """Check if the guess is in the word"""
        return self.current_guess in self.word_to_guess

    def correct_guess(self):
        """Handle a correct guess"""
        self.show_message(
            f"{self.current_guess.upper()} finns i det hemliga ordet.",
            "success"
        )
        self.check_game_won()

    def incorrect_guess(self):
        """Handle an incorrect guess"""
        self.show_message(
            f"{self.current_guess.upper()} finns inte i det hemliga ordet.",
            "error"
        )
        self.incorrect_guesses_made += 1
        self.check_game_over()

    def check_game_won(self):
        """Check if the player has won"""
        if self._all_letters_guessed():
            self._handle_win()

    def _all_letters_guessed(self):
        """Check if all letters in the word have been guessed"""
        return all(letter in self.guessed_letters for letter in self.word_to_guess)

    def _handle_win(self):
        """Handle when player wins the game"""
        self.game_finished = True
        self.show_message(
            f"Du vann! Det hemliga ordet var {self.word_to_guess}.",
            "success"
        )

    def check_game_over(self):
        """Check if the player has lost"""
        if self.incorrect_guesses_made >= self.allowed_guesses:
            self._handle_loss()

    def _handle_loss(self):
        """Handle when player loses the game"""
        self.game_finished = True
        self.show_message(
            f"Game over! Det hemliga ordet var {self.word_to_guess}.",
            "error"
        )
        # Reveal the word
        self.word_display.config(text=self.word_to_guess)

def main():
    """Main function to run the Hangman game"""
    root = tk.Tk()
    # Set window icon and other properties if needed
    root.configure(bg=COLORS["background"])

    # Center window on screen
    window_width = 600
    window_height = 550  # Increased height for wordlist info
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Create game instance
    hangman_game = HangmanGameGUI(root)

    # Start the main loop
    root.mainloop()

# Run the game if this file is executed directly
if __name__ == "__main__":
    main()