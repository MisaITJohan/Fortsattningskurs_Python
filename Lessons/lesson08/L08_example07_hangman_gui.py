# Denna fil är en GUI-version av hangmanL08.py, som använder MVC-mönstret.
# Model-klassen är identisk med den i hangmanL08.py.
# View-klassen är en GUI-version som ersätter konsol-vyn med tkinter-widgets.
# Controller-klassen kopplar ihop Model och View och styr spelets flöde.

# Eftersom tkinter är händelsestyrt (event-driven) istället för sekventiellt
# som en konsolapplikation, kan Controller inte använda exakt samma game_loop()
# med blockerande input()-anrop. Istället använder Controller samma metoder
# (_make_guess, _register_guess, _evaluate_guess, _correct_guess,
# _incorrect_guess) men anropas av GUI:ts händelser istället för att driva
# en egen loop.

# Notera att View-klassen har samma metod-gränssnitt som konsol-vyn i
# hangmanL08.py (display_correct_guess, display_incorrect_guess,
# display_game_won, display_game_over, display_current_state, etc.)
# så att Controller inte behöver veta vilken typ av vy den arbetar med.

# För att demonstrera en potentiell förbättring har jag gjort något som man
# inte bör göra på ett inkonsekvent sätt: jag kombinerar metoder för hur jag
# hanterar de formaterade strängarna. I dict:en MESSAGES har jag påbörjat
# processen av att byta till ett system som gör programmet enklare att uppdatera
# och skulle göra det enklare att översätta.


import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import random


# Vi samlar våra konstanter här för att göra det lättare att konfigurera.
DEFAULT_MAX_INCORRECT_GUESSES = 5

# Constants for UI appearance and configuration
COLORS = {
    "background": "#f0f0f0",
    "success": "green",
    "error": "red",
    "info": "blue",
}

FONTS = {
    "title": ("Arial", 24, "bold"),
    "normal": ("Arial", 12),
    "word": ("Courier", 18),
    "emphasis": ("Arial", 12, "bold"),
}

# This dictionary contains messages used in the UI, allowing for translation
# to other languages.
MESSAGES = {
    "title": "Hangman",
    "guess_prompt": "Gissa en bokstav eller lämna tomt för att avsluta omgången:",
    "guess_button": "Gissa",
    "load_wordlist": "Ladda ordlista",
    "new_game": "Nytt spel",
    "using_wordlist": "Använder ordlista: {}",
    "wordlist_loaded": "Ordlista laddad: {word_count} ord",
}


# Model-klassen hanterar spelets data och logik.
class HangmanModel:
    """En klass som hanterar spellogiken samt lagrar information om spelstatus."""

    def __init__(self, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        self.possible_words = None
        self.max_incorrect_guesses = max_incorrect_guesses
        self.incorrect_guesses_count = 0
        self.secret_word = ""
        self.guessed_letters = set()
        self.current_guess = ""
        self.game_finished = False
        self.custom_list_path = ""

    def setup(self):
        self.game_finished = False
        self.incorrect_guesses_count = 0
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
            self.guessed_letters.clear()

    def load_words_from_file(self, target_path=None):
        if target_path is None and not self.custom_list_path:
            target_path = Path("wordlist_creator/wordlist.txt")
        elif self.custom_list_path:
            target_path = self.custom_list_path
        elif target_path:
            self.custom_list_path = target_path

        file_to_open = Path(target_path)

        try:
            self.possible_words = file_to_open.read_text(encoding="utf-8").splitlines()
            return file_to_open, True
        except FileNotFoundError:
            if not self.custom_list_path:
                file_to_open = Path("wordlist.txt")
            else:
                file_to_open = Path(self.custom_list_path)
            return file_to_open, False

    def get_word_to_guess(self):
        self.secret_word = random.choice(self.possible_words).lower()

    def check_guess(self):
        return self.current_guess in self.secret_word

    def check_invalid(self, guess):
        previously_guessed = guess in self.guessed_letters
        invalid_length = len(guess) != 1
        is_not_letter = not guess.isalpha()

        is_invalid = previously_guessed or invalid_length or is_not_letter

        return is_invalid

    def check_game_won(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def check_game_over(self):
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            return True
        return False

    def guesses_remaining(self):
        return self.max_incorrect_guesses - self.incorrect_guesses_count

    def get_correct_guesses(self):
        return sorted([x for x in self.guessed_letters
                       if x in self.secret_word])

    def get_placeholder(self):
        placeholder = self.secret_word
        for char in placeholder:
            if char not in self.guessed_letters:
                placeholder = placeholder.replace(char, "_")
        return placeholder


# View-klassen hanterar allt som visas för spelaren via GUI.
# Den har samma metod-gränssnitt som konsol-vyn i hangmanL08.py.
class HangmanGUIView:
    """En klass som hanterar de synliga delarna av spelet via tkinter.
    Vyn ska inte behöva veta någonting om modellen."""

    def __init__(self, master):
        self.master = master
        self.master.title(MESSAGES["title"])
        self.master.configure(bg=COLORS["background"])

        self._create_widgets()

    def _create_widgets(self):
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

        self.word_length_label = tk.Label(
            self.info_frame, text="",
            font=FONTS["normal"],
            bg=COLORS["background"])
        self.word_length_label.pack(pady=5)

        self.word_display = tk.Label(
            self.info_frame,
            text="",
            font=FONTS["word"],
            bg=COLORS["background"])
        self.word_display.pack(pady=10)

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
            text=MESSAGES["guess_prompt"],
            font=FONTS["normal"],
            bg=COLORS["background"]
        )
        self.guess_label.grid(row=0, column=0, padx=5)

        self.guess_entry = tk.Entry(self.input_frame, width=3, font=FONTS["normal"])
        self.guess_entry.grid(row=0, column=1, padx=5)

        self.guess_button = tk.Button(
            self.input_frame,
            text=MESSAGES["guess_button"],
            font=FONTS["normal"]
        )
        self.guess_button.grid(row=0, column=2, padx=5)

    def _create_control_section(self):
        """Create the game control buttons section"""
        self.control_frame = tk.Frame(self.master, bg=COLORS["background"])
        self.control_frame.pack(pady=20)

        self.load_wordlist_button = tk.Button(
            self.control_frame,
            text=MESSAGES["load_wordlist"],
            font=FONTS["normal"]
        )
        self.load_wordlist_button.pack(side=tk.LEFT, padx=10)

        self.new_game_button = tk.Button(
            self.control_frame,
            text=MESSAGES["new_game"],
            font=FONTS["normal"]
        )
        self.new_game_button.pack(side=tk.LEFT, padx=10)

        self.quit_button = tk.Button(
            self.control_frame,
            text="Avsluta",
            font=FONTS["normal"]
        )
        self.quit_button.pack(side=tk.LEFT, padx=10)

        self.wordlist_info_frame = tk.Frame(self.master, bg=COLORS["background"])
        self.wordlist_info_frame.pack(pady=5)

        self.wordlist_label = tk.Label(
            self.wordlist_info_frame,
            text="Använder standardordlista",
            font=(FONTS["normal"][0], 10),
            bg=COLORS["background"])
        self.wordlist_label.pack()

    # --- Metoder som matchar konsol-vyns gränssnitt ---

    def display_current_state(self, word_length, guessed_letters,
                               incorrect_guesses_count, guesses_remaining,
                               correct_guesses=None, placeholder=None):
        """Update all display elements with current game state"""
        self.word_length_label.config(
            text=f"Det hemliga ordet är {word_length} tecken långt."
        )
        self.guesses_left_label.config(
            text=f"Du har {guesses_remaining} gissningar kvar."
        )

        if len(guessed_letters) > 0:
            sorted_letters = sorted(list(guessed_letters))
            self.guessed_letters_label.config(
                text=f"Du har gissat dessa bokstäver: {' '.join(sorted_letters)}"
            )
            if correct_guesses:
                self.correct_guesses_label.config(
                    text=f"Av de gissade bokstäverna finns dessa i det "
                         f"hemliga ordet: {' '.join(correct_guesses)}"
                )
            else:
                self.correct_guesses_label.config(text="")
        else:
            self.guessed_letters_label.config(
                text="Du har inte gissat några bokstäver än."
            )
            self.correct_guesses_label.config(text="")

        if placeholder is not None:
            self.display_placeholder(placeholder)

    def display_placeholder(self, placeholder):
        """Update the word display with placeholders"""
        self.word_display.config(text=" ".join(placeholder))

    def display_correct_guess(self, letter):
        self._show_message(
            f"{letter.upper()} finns i det hemliga ordet.", "success"
        )

    def display_incorrect_guess(self, letter):
        self._show_message(
            f"{letter.upper()} finns inte i det hemliga ordet.", "error"
        )

    def display_game_won(self):
        self._show_message("Du vann!", "success")

    def display_game_over(self):
        self._show_message("Game over!", "error")

    def display_secret(self, secret_word):
        self._show_message(
            f"Det hemliga ordet var {secret_word}.", "info"
        )

    def display_file_not_found(self, fallback_path, custom_list_path):
        self._show_message(
            f"Det finns ingen fil som heter det som skrevs in, "
            f"{'standardlistan' if not custom_list_path else custom_list_path}"
            f" används.", "error"
        )

    def display_invalid_guess(self):
        self._show_message(
            "Ogiltig gissning! Ange en bokstav som du inte har gissat tidigare.",
            "error"
        )

    def display_game_ended(self):
        self._show_message("Spelet avslutades.", "info")

    def display_new_game(self):
        self._show_message("Nytt spel har startat!", "info")

    def display_wordlist_info(self, filename):
        self.wordlist_label.config(
            text=MESSAGES["using_wordlist"].format(filename)
        )

    def display_wordlist_loaded(self, word_count):
        self._show_message(
            MESSAGES["wordlist_loaded"].format(word_count=word_count), "info"
        )

    def display_default_wordlist(self):
        self.wordlist_label.config(text="Använder standardordlista")

    # --- GUI-specifika metoder ---

    def get_guess(self):
        """Get and clear the guess from the entry field"""
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        return guess

    def ask_load_wordlist(self, has_custom_list):
        """Open a file dialog to let the user select a custom word file.
        GUI-versionen av konsol-vyns ask_load_wordlist + ask_wordlist_path."""
        return filedialog.askopenfilename(
            title="Välj en ordlistefil",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialdir=os.getcwd()
        )

    def focus_entry(self):
        """Focus the entry field"""
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    def bind_guess(self, callback):
        """Bind the guess button and Enter key to a callback"""
        self.guess_button.config(command=callback)
        self.guess_entry.bind('<Return>', lambda event: callback())

    def bind_new_game(self, callback):
        """Bind the new game button to a callback"""
        self.new_game_button.config(command=callback)

    def bind_load_wordlist(self, callback):
        """Bind the load wordlist button to a callback"""
        self.load_wordlist_button.config(command=callback)

    def bind_quit(self, callback):
        """Bind the quit button to a callback"""
        self.quit_button.config(command=callback)

    def _show_message(self, message, message_type="info"):
        """Display a message with appropriate styling"""
        self.message_label.config(text=message, fg=COLORS[message_type])


# Controller-klassen kopplar ihop Model och View och styr spelets flöde.
# Den använder samma metoder som konsol-versionen i hangmanL08.py
# (_make_guess, _register_guess, _evaluate_guess, _correct_guess,
# _incorrect_guess) men anpassad för händelsestyrd GUI-interaktion.
class HangmanController:

    def __init__(self, master):
        self.model = HangmanModel()
        self.view = HangmanGUIView(master)

        # Bind view events to controller methods
        self.view.bind_guess(self._make_guess)
        self.view.bind_new_game(self._new_game)
        self.view.bind_load_wordlist(self._handle_wordlist_loading)
        self.view.bind_quit(master.destroy)

        # Load words and start the game
        self._initialize_wordlist()
        self._new_game()

    def _initialize_wordlist(self):
        """Load the default wordlist at startup"""
        file_to_open, success = self.model.load_words_from_file()
        if not success:
            self.view.display_file_not_found(
                file_to_open, self.model.custom_list_path)
            try:
                self.model.possible_words = file_to_open.read_text(
                    encoding="utf-8").splitlines()
            except FileNotFoundError:
                self.model.possible_words = [
                    "apa", "banan", "cacao", "dans", "elefant"
                ]
                self.view.display_default_wordlist()

    def _handle_wordlist_loading(self):
        """Handle loading a custom wordlist via file dialog"""
        file_path = self.view.ask_load_wordlist(
            bool(self.model.custom_list_path))

        if file_path:
            file_to_open, success = self.model.load_words_from_file(file_path)
            if success:
                filename = Path(file_path).name
                self.view.display_wordlist_info(filename)
                self.view.display_wordlist_loaded(len(self.model.possible_words))
                self._new_game()
            else:
                self.view.display_file_not_found(
                    file_to_open, self.model.custom_list_path)

    def _new_game(self):
        """Start a new game"""
        self.model.setup()
        self._update_display()
        self.view.display_new_game()
        self.view.focus_entry()

    def _update_display(self):
        """Update the view with current model state"""
        self.view.display_current_state(
            len(self.model.secret_word),
            self.model.guessed_letters,
            self.model.incorrect_guesses_count,
            self.model.guesses_remaining(),
            self.model.get_correct_guesses(),
            self.model.get_placeholder(),
        )

    def _make_guess(self):
        """Process a player's guess — same logic as console version"""
        if self.model.game_finished:
            return

        guess = self.view.get_guess()

        if not guess:
            self.model.game_finished = True
            self.view.display_game_ended()
            return

        if self.model.check_invalid(guess):
            self.view.display_invalid_guess()
            self.view.focus_entry()
            return

        self._register_guess(guess)
        self._evaluate_guess()
        self._update_display()
        self.view.focus_entry()

    def _register_guess(self, guess):
        self.model.guessed_letters.add(guess)
        self.model.current_guess = guess

    def _evaluate_guess(self):
        check_correct = self.model.check_guess()
        if check_correct:
            self._correct_guess()
        else:
            self._incorrect_guess()

    def _correct_guess(self):
        self.view.display_correct_guess(self.model.current_guess)
        if self.model.check_game_won():
            self.view.display_game_won()
            self.view.display_secret(self.model.secret_word)
            self.model.game_finished = True

    def _incorrect_guess(self):
        self.view.display_incorrect_guess(self.model.current_guess)
        self.model.incorrect_guesses_count += 1
        if self.model.check_game_over():
            self.view.display_game_over()
            self.view.display_secret(self.model.secret_word)
            self.model.game_finished = True


def main():
    """Main function to run the Hangman game"""
    root = tk.Tk()
    root.configure(bg=COLORS["background"])

    # Center window on screen
    window_width = 600
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Create controller (which creates model and view)
    HangmanController(root)

    root.mainloop()


if __name__ == "__main__":
    main()
