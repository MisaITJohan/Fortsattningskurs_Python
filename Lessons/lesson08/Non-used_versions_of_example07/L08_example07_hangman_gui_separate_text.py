import tkinter as tk
from tkinter import filedialog
import pathlib
import random
import os

# Constants
# UI appearance and configuration
UI_COLORS = {
    "background": "#f0f0f0",
    "success": "green",
    "error": "red",
    "info": "blue"
}

UI_FONTS = {
    "title": ("Arial", 24, "bold"),
    "normal": ("Arial", 12),
    "word": ("Courier", 18),
    "emphasis": ("Arial", 12, "bold")
}

# Game messages and text (enables easier internationalization)
MESSAGES = {
    "title": "Hangman",
    "guess_prompt": "Gissa en bokstav eller lämna tomt för att avsluta omgången:",
    "guess_button": "Gissa",
    "load_wordlist": "Ladda ordlista",
    "new_game": "Nytt spel",
    "quit": "Avsluta",
    "default_wordlist": "Använder standardordlista",
    "using_wordlist": "Använder ordlista: {}",
    "wordlist_loaded": "Ordlista laddad: {} ord",
    "file_error": "Kunde inte läsa från den valda filen.",
    "new_game_started": "Nytt spel har startat!",
    "word_length": "Det hemliga ordet är {} tecken långt.",
    "guesses_left": "Du har {} gissningar kvar.",
    "no_guesses_yet": "Du har inte gissat några bokstäver än.",
    "guessed_letters": "Du har gissat dessa bokstäver: {}",
    "correct_letters": "Av de gissade bokstäverna finns dessa i det hemliga ordet: {}",
    "game_over": "Spelet är slut. Starta ett nytt spel!",
    "game_quit": "Spelet avslutades.",
    "invalid_guess": "Ogiltig gissning! Ange en bokstav som du inte har gissat tidigare.",
    "correct_guess": "{} finns i det hemliga ordet.",
    "incorrect_guess": "{} finns inte i det hemliga ordet.",
    "win": "Du vann! Det hemliga ordet var {}.",
    "loss": "Game over! Det hemliga ordet var {}."
}


class HangmanGame:
    """Model class that handles the game logic without UI dependencies"""
    
    def __init__(self, allowed_guesses=5):
        self.allowed_guesses = allowed_guesses
        self._initialize_game()


    def _initialize_game(self):
        """Initialize the game state"""
        self.word_to_guess = ""
        self.guessed_letters = set()
        self.incorrect_guesses_made = 0
        self.game_finished = False
        self.current_guess = ""

    def reset_game_state(self):
        """Reset the game state for a new game. Provides an
        external interface for this method."""
        self._initialize_game()

    def set_word(self, word):
        """Set the word to be guessed"""
        self.word_to_guess = word.lower()
        
    def make_guess(self, guess):
        """Process a player's guess and return the result"""
        guess = guess.lower()
        
        # Handle empty guess (quit)
        if not guess:
            self.game_finished = True
            return {"status": "quit"}
        
        # Check for invalid guess
        if self.is_invalid_guess(guess):
            return {"status": "invalid"}
        
        # Record the guess
        self.guessed_letters.add(guess)
        self.current_guess = guess
        
        # Check if guess is correct
        is_correct = guess in self.word_to_guess
        
        if is_correct:
            result = {"status": "correct", "letter": guess.upper()}
            # Check for win condition
            if self.all_letters_guessed():
                self.game_finished = True
                result["game_over"] = True
                result["win"] = True
        else:
            self.incorrect_guesses_made += 1
            result = {"status": "incorrect", "letter": guess.upper()}
            # Check for loss condition
            if self.incorrect_guesses_made >= self.allowed_guesses:
                self.game_finished = True
                result["game_over"] = True
                result["win"] = False
                
        return result
    
    def is_invalid_guess(self, guess):
        """Check if a guess is invalid"""
        return (guess in self.guessed_letters or 
                len(guess) != 1 or 
                not guess.isalpha())
    
    def all_letters_guessed(self):
        """Check if all letters in the word have been guessed"""
        return all(letter in self.guessed_letters for letter in self.word_to_guess)
    
    def get_word_with_placeholders(self):
        """Get the word with placeholders for unguessed letters"""
        display_chars = []
        for letter in self.word_to_guess:
            if letter in self.guessed_letters:
                display_chars.append(letter + " ")
            else:
                display_chars.append("_ ")
        return "".join(display_chars)
    
    def get_correct_guesses(self):
        """Get a sorted list of correct guesses"""
        return sorted([letter for letter in self.guessed_letters 
                      if letter in self.word_to_guess])
    
    def get_game_state(self):
        """Get the current game state"""
        return {
            "word_length": len(self.word_to_guess),
            "word_display": self.get_word_with_placeholders(),
            "guesses_left": self.allowed_guesses - self.incorrect_guesses_made,
            "guessed_letters": sorted(list(self.guessed_letters)),
            "correct_guesses": self.get_correct_guesses(),
            "game_finished": self.game_finished,
            "word": self.word_to_guess
        }


class HangmanGameGUI:
    """View class that handles the UI for the Hangman game"""
    
    def __init__(self, master, wordlist=None, allowed_guesses=5):
        # Setup main window
        self.master = master
        self.master.title(MESSAGES["title"])
        self.master.geometry("600x550")
        self.master.configure(bg=UI_COLORS["background"])
        
        # Create game model
        self.game = HangmanGame(allowed_guesses)
        
        # Game state variables
        self.possible_words = None
        
        # Create widgets first so the wordlist label exists when fetch_words is called
        self.create_widgets()
        
        # Initialize the game
        self.fetch_words(wordlist)
        self.start_new_game()
    
    def create_widgets(self):
        self._create_title_section()
        self._create_game_info_section()
        self._create_input_section()
        self._create_control_section()
    
    def _create_title_section(self):
        """Create the title section of the UI"""
        self.title_frame = tk.Frame(self.master, bg=UI_COLORS["background"])
        self.title_frame.pack(pady=10)
        
        self.title_label = tk.Label(
            self.title_frame, 
            text=MESSAGES["title"],
            font=UI_FONTS["title"], 
            bg=UI_COLORS["background"]
        )
        self.title_label.pack()
    
    def _create_game_info_section(self):
        """Create the game information display section"""
        self.info_frame = tk.Frame(self.master, bg=UI_COLORS["background"])
        self.info_frame.pack(pady=10)
        
        # Word length info
        self.word_length_label = tk.Label(
            self.info_frame, 
            text="",
            font=UI_FONTS["normal"], 
            bg=UI_COLORS["background"]
        )
        self.word_length_label.pack(pady=5)
        
        # Display the current word with placeholders
        self.word_display = tk.Label(
            self.info_frame, 
            text="",
            font=UI_FONTS["word"], 
            bg=UI_COLORS["background"]
        )
        self.word_display.pack(pady=10)
        
        # Guesses information
        self.guesses_left_label = tk.Label(
            self.info_frame, 
            text="",
            font=UI_FONTS["normal"], 
            bg=UI_COLORS["background"]
        )
        self.guesses_left_label.pack(pady=5)
        
        self.guessed_letters_label = tk.Label(
            self.info_frame, 
            text="",
            font=UI_FONTS["normal"], 
            bg=UI_COLORS["background"]
        )
        self.guessed_letters_label.pack(pady=5)
        
        self.correct_guesses_label = tk.Label(
            self.info_frame, 
            text="",
            font=UI_FONTS["normal"], 
            bg=UI_COLORS["background"]
        )
        self.correct_guesses_label.pack(pady=5)
        
        # Message area for game feedback
        self.message_label = tk.Label(
            self.info_frame, 
            text="",
            font=UI_FONTS["emphasis"], 
            fg=UI_COLORS["info"],
            bg=UI_COLORS["background"]
        )
        self.message_label.pack(pady=10)
    
    def _create_input_section(self):
        """Create the user input section"""
        self.input_frame = tk.Frame(self.master, bg=UI_COLORS["background"])
        self.input_frame.pack(pady=10)
        
        self.guess_label = tk.Label(
            self.input_frame, 
            text=MESSAGES["guess_prompt"], 
            font=UI_FONTS["normal"], 
            bg=UI_COLORS["background"]
        )
        self.guess_label.grid(row=0, column=0, padx=5)
        
        self.guess_entry = tk.Entry(self.input_frame, width=3, font=UI_FONTS["normal"])
        self.guess_entry.grid(row=0, column=1, padx=5)
        self.guess_entry.bind('<Return>', lambda event: self.make_guess())
        
        self.guess_button = tk.Button(
            self.input_frame, 
            text=MESSAGES["guess_button"], 
            command=self.make_guess, 
            font=UI_FONTS["normal"]
        )
        self.guess_button.grid(row=0, column=2, padx=5)
    
    def _create_control_section(self):
        """Create the game control buttons section"""
        self.control_frame = tk.Frame(self.master, bg=UI_COLORS["background"])
        self.control_frame.pack(pady=20)
        
        # Add a button to load a custom wordlist
        self.load_wordlist_button = tk.Button(
            self.control_frame, 
            text=MESSAGES["load_wordlist"], 
            command=self.load_custom_wordlist, 
            font=UI_FONTS["normal"]
        )
        self.load_wordlist_button.pack(side=tk.LEFT, padx=10)
        
        self.new_game_button = tk.Button(
            self.control_frame, 
            text=MESSAGES["new_game"], 
            command=self.start_new_game, 
            font=UI_FONTS["normal"]
        )
        self.new_game_button.pack(side=tk.LEFT, padx=10)
        
        self.quit_button = tk.Button(
            self.control_frame, 
            text=MESSAGES["quit"], 
            command=self.master.destroy, 
            font=UI_FONTS["normal"]
        )
        self.quit_button.pack(side=tk.LEFT, padx=10)
        
        # Add a label to show the current wordlist file
        self.wordlist_info_frame = tk.Frame(self.master, bg=UI_COLORS["background"])
        self.wordlist_info_frame.pack(pady=5)
        
        self.wordlist_label = tk.Label(
            self.wordlist_info_frame, 
            text=MESSAGES["default_wordlist"], 
            font=(UI_FONTS["normal"][0], 10), 
            bg=UI_COLORS["background"]
        )
        self.wordlist_label.pack()
    
    def load_custom_wordlist(self):
        """Open a file dialog to let the user select a custom word file"""
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
                self.wordlist_label.config(text=MESSAGES["using_wordlist"].format(filename))
                # Start a new game with the new wordlist
                self.show_message(
                    MESSAGES["wordlist_loaded"].format(len(words)), 
                    "info"
                )
                self.start_new_game()
            else:
                self.show_message(MESSAGES["file_error"], "error")
    
    def fetch_words(self, target=None):
        """Load words from a file with fallback options"""
        # Default wordlist if all else fails
        default_words = ["apa", "banan", "cacao", "dans", "elefant"]
        
        # Try loading from different sources in order of priority
        sources = [
            # 1. Custom provided path
            lambda: self._load_from_file(target) if target else None,
            # 2. Default wordlist path
            lambda: self._load_from_file(pathlib.Path("../wordlist_creator/wordlist.txt")),
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
                    self.wordlist_label.config(text=MESSAGES["default_wordlist"])
                return
    
    def _load_from_file(self, file_path):
        """Helper method to load words from a file"""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return [x.strip() for x in file.readlines()]
        except (FileNotFoundError, IOError):
            return None
    
    def start_new_game(self):
        """Reset and start a new game"""
        self.game.reset_game_state()
        # Select a new word
        new_word = random.choice(self.possible_words)
        self.game.set_word(new_word)
        
        # Update all UI elements
        self.update_ui()
        self.show_message(MESSAGES["new_game_started"], "info")
        
        # Reset and focus entry field
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()
    
    def update_ui(self):
        """Update all UI elements based on current game state"""
        game_state = self.game.get_game_state()
        
        # Update word length
        self.word_length_label.config(
            text=MESSAGES["word_length"].format(game_state["word_length"])
        )
        
        # Update word display
        self.word_display.config(text=game_state["word_display"])
        
        # Update guesses left
        self.guesses_left_label.config(
            text=MESSAGES["guesses_left"].format(game_state["guesses_left"])
        )
        
        # Update guessed letters
        if game_state["guessed_letters"]:
            guessed_text = MESSAGES["guessed_letters"].format(
                " ".join(game_state["guessed_letters"])
            )
        else:
            guessed_text = MESSAGES["no_guesses_yet"]
        self.guessed_letters_label.config(text=guessed_text)
        
        # Update correct guesses
        correct_guesses = game_state["correct_guesses"]
        if correct_guesses:
            correct_text = MESSAGES["correct_letters"].format(" ".join(correct_guesses))
        else:
            correct_text = ""
        self.correct_guesses_label.config(text=correct_text)
    
    def make_guess(self):
        """Process a player's guess"""
        # Check if game is already finished
        if self.game.game_finished:
            self.show_message(MESSAGES["game_over"], "error")
            return
        
        # Get and clear the guess from the entry field
        guess = self.guess_entry.get()
        self.guess_entry.delete(0, tk.END)
        
        # Process the guess and handle the result
        result = self.game.make_guess(guess)
        
        if result["status"] == "quit":
            self.show_message(MESSAGES["game_quit"], "info")
        elif result["status"] == "invalid":
            self.show_message(MESSAGES["invalid_guess"], "error")
        elif result["status"] == "correct":
            self.show_message(
                MESSAGES["correct_guess"].format(result["letter"]), 
                "success"
            )
            # Check if game is won
            if "game_over" in result and result["win"]:
                self.show_message(
                    MESSAGES["win"].format(self.game.word_to_guess),
                    "success"
                )
        elif result["status"] == "incorrect":
            self.show_message(
                MESSAGES["incorrect_guess"].format(result["letter"]), 
                "error"
            )
            # Check if game is lost
            if "game_over" in result and not result["win"]:
                self.show_message(
                    MESSAGES["loss"].format(self.game.word_to_guess),
                    "error"
                )
                # Reveal the word
                self.word_display.config(text=self.game.word_to_guess)
        
        # Update the UI with the new game state
        self.update_ui()
        
        # Reset focus to entry field
        self.guess_entry.focus()
    
    def show_message(self, message, message_type="info"):
        """Display a message with appropriate styling"""
        self.message_label.config(text=message, fg=UI_COLORS[message_type])


def main():
    """Main function to run the Hangman game"""
    root = tk.Tk()
    # Set window icon and other properties if needed
    root.configure(bg=UI_COLORS["background"])
    
    # Center window on screen
    window_width = 600
    window_height = 550
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