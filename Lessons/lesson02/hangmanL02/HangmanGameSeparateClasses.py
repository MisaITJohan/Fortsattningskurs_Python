# Första versionen av vårt spel kommer vara simplistiskt men fortfarande ett
# fungerande program. Under kommande veckor kommer vi lägga till fler funktioner.
import random

# Vi samlar våra konstanter här för att göra det lättare att konfigurera.
DEFAULT_MAX_INCORRECT_GUESSES = 5
POSSIBLE_WORDS = (
    "Apa",
    "Banan",
    "Cacao",
    "Dans",
    "Elefant",
)

class HangmanModel:
    """Handles the game logic and state for the Hangman game."""
    
    def __init__(self, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        self.max_incorrect_guesses = max_incorrect_guesses
        self.incorrect_guesses_count = 0
        self.secret_word = ""
        self.guessed_letters = set()
        self.is_game_over = False
        self.is_game_won = False
        self.select_random_word()
    
    def select_random_word(self):
        """Select a random word from the list of possible words."""
        self.secret_word = random.choice(POSSIBLE_WORDS).lower()
    
    def process_guess(self, letter):
        """Process a letter guess and update game state."""
        letter = letter.lower()
        self.guessed_letters.add(letter)
        
        if letter in self.secret_word:
            self._check_if_won()
            return True
        else:
            self.incorrect_guesses_count += 1
            self._check_if_lost()
            return False
    
    def _check_if_won(self):
        """Check if all letters in the secret word have been guessed."""
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return
        self.is_game_won = True
        self.is_game_over = True
    
    def _check_if_lost(self):
        """Check if the maximum number of incorrect guesses has been reached."""
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            self.is_game_over = True
    
    def get_remaining_guesses(self):
        """Return the number of remaining guesses."""
        return self.max_incorrect_guesses - self.incorrect_guesses_count


class HangmanView:
    """Handles the user interface for the Hangman game."""
    
    def display_game_status(self, model):
        """Display the current game status."""
        print("Det hemliga ordet är", len(model.secret_word), "tecken långt.")
        if model.guessed_letters:
            print("Du har gissat dessa bokstäver:", model.guessed_letters)
            print("Du har gissat fel", model.incorrect_guesses_count, "gånger.")
        print("Du har", model.get_remaining_guesses(), "gissningar kvar.")
    
    def get_guess(self):
        """Get a letter guess from the user."""
        return input("Gissa en bokstav: ")
    
    def display_correct_guess(self, letter):
        """Display a message for a correct guess."""
        print(f"\n{letter.upper()} finns i det hemliga ordet.\n")
    
    def display_incorrect_guess(self, letter):
        """Display a message for an incorrect guess."""
        print(f"\n{letter.upper()} finns inte i det hemliga ordet.\n")
    
    def display_game_won(self):
        """Display a message for a won game."""
        print("Du vann!")
    
    def display_game_over(self):
        """Display a message for a lost game."""
        print("Game over!")
    
    def display_secret_word(self, word):
        """Display the secret word and wait for user input to exit."""
        print("Det hemliga ordet var", word)
        # För att ge oss en chans att se ordet så lägger vi in en input() vars
        # enda syfte att pausa programmet.
        input("Tryck enter för att avsluta.")


class HangmanGame:
    """Main Hangman game class that combines the model and view."""
    
    def __init__(self, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        self.model = HangmanModel(max_incorrect_guesses)
        self.view = HangmanView()
        self.view.display_game_status(self.model)
    
    def setup(self):
        # Här borde vissa delar av __init__() ligga för att korta ned
        # den metoden. Detta kan också användas för att nollställa
        # spelet.
        pass
    
    def get_word_to_guess(self):
        self.model.select_random_word()
    
    def display_current_state(self):
        self.view.display_game_status(self.model)
    
    def make_guess(self):
        letter = self.view.get_guess()
        is_correct = self.model.process_guess(letter)
        
        if is_correct:
            self.correct_guess(letter)
        else:
            self.incorrect_guess(letter)
        
        self.display_current_state()
    
    def check_guess(self):
        # This method is kept for compatibility but no longer used
        pass
    
    def correct_guess(self, letter):
        self.view.display_correct_guess(letter)
        if self.model.is_game_won:
            self.view.display_game_won()
            self.display_secret()
    
    def incorrect_guess(self, letter):
        self.view.display_incorrect_guess(letter)
        self.check_game_over()
    
    def check_game_won(self):
        # This method is kept for compatibility but no longer used
        pass
    
    def check_game_over(self):
        if self.model.is_game_over and not self.model.is_game_won:
            self.view.display_game_over()
            self.display_secret()
    
    def display_secret(self):
        self.view.display_secret_word(self.model.secret_word)
        quit()


if __name__ == "__main__":
    game = HangmanGame()
    while True:
        game.make_guess()
