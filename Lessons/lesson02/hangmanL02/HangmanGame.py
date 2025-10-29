# Hangman Game Implementation
import random

# Game configuration constants
DEFAULT_MAX_INCORRECT_GUESSES = 5
POSSIBLE_WORDS = (
    "Apa",
    "Banan", 
    "Cacao",
    "Dans",
    "Elefant",
)

# Message constants
MSG_WORD_LENGTH = "Det hemliga ordet är {} tecken långt."
MSG_GUESSED_LETTERS = "Du har gissat dessa bokstäver: {}"
MSG_WRONG_GUESSES = "Du har gissat fel {} gånger."
MSG_GUESSES_LEFT = "Du har {} gissningar kvar."
MSG_CORRECT_GUESS = "\n{} finns i det hemliga ordet.\n"
MSG_INCORRECT_GUESS = "\n{} finns inte i det hemliga ordet.\n"
MSG_WIN = "Du vann!"
MSG_GAME_OVER = "Game over!"
MSG_SECRET_WORD = "Det hemliga ordet var {}"
MSG_PRESS_ENTER = "Tryck enter för att avsluta."

class HangmanGame:
    """Implements the Hangman word-guessing game."""
    
    def __init__(self, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        """Initialize the game with default settings."""
        self.max_incorrect_guesses = max_incorrect_guesses
        self.setup()
        self.display_current_state()
    
    def setup(self):
        """Setup or reset the game state."""
        self.incorrect_guesses_count = 0
        self.select_secret_word()
        self.guessed_letters = set()
        self.current_guess = ""
    
    def select_secret_word(self):
        """Select a random word from the list of possible words."""
        self.secret_word = random.choice(POSSIBLE_WORDS).lower()
    
    def display_current_state(self):
        """Display the current game state including word progress."""
        print(MSG_WORD_LENGTH.format(len(self.secret_word)))
        
        # Display current word with revealed letters
        self.display_word_progress()
        
        if self.guessed_letters:
            print(MSG_GUESSED_LETTERS.format(self.guessed_letters))
            print(MSG_WRONG_GUESSES.format(self.incorrect_guesses_count))
        
        print(MSG_GUESSES_LEFT.format(self.max_incorrect_guesses - self.incorrect_guesses_count))
    
    def display_word_progress(self):
        """Show the word with guessed letters revealed and others hidden."""
        displayed_word = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        print(displayed_word)
    
    def make_guess(self):
        """Process the player's letter guess."""
        guess = input("Gissa en bokstav: ").lower()
        self.guessed_letters.add(guess)
        self.current_guess = guess
        
        if self.is_guess_correct():
            self.handle_correct_guess()
        else:
            self.handle_incorrect_guess()
            
        self.display_current_state()
    
    def is_guess_correct(self):
        """Check if the current guess is in the secret word."""
        return self.current_guess in self.secret_word
    
    def handle_correct_guess(self):
        """Handle logic for a correct guess."""
        print(MSG_CORRECT_GUESS.format(self.current_guess.upper()))
        self.check_for_win()
    
    def handle_incorrect_guess(self):
        """Handle logic for an incorrect guess."""
        print(MSG_INCORRECT_GUESS.format(self.current_guess.upper()))
        self.incorrect_guesses_count += 1
        self.check_for_loss()
    
    def check_for_win(self):
        """Check if the player has won the game."""
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return
        
        print(MSG_WIN)
        self.end_game()
    
    def check_for_loss(self):
        """Check if the player has lost the game."""
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            print(MSG_GAME_OVER)
            self.end_game()
    
    def end_game(self):
        """End the game and reveal the secret word."""
        print(MSG_SECRET_WORD.format(self.secret_word))
        input(MSG_PRESS_ENTER)
        quit()

if __name__ == "__main__":
    game = HangmanGame()
    while True:
        game.make_guess()
