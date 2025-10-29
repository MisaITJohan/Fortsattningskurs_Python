# Hangman game with improved modularity
import random

# Constants
DEFAULT_MAX_INCORRECT_GUESSES = 5
POSSIBLE_WORDS = (
    "Apa",
    "Banan",
    "Cacao",
    "Dans",
    "Elefant",
)

class HangmanGame:
    def __init__(self, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        self.max_incorrect_guesses = max_incorrect_guesses
        self.incorrect_guesses_count = 0
        self.secret_word = self._get_random_word()
        self.guessed_letters = set()
        self.current_guess = ""
        self.game_over = False

    def setup(self):
        pass

    def _get_random_word(self):
        """Get a random word from the list of possible words"""
        return random.choice(POSSIBLE_WORDS).lower()

    def display_game_status(self):
        """Display the current game status"""
        print("Det hemliga ordet är", len(self.secret_word), "tecken långt.")
        if len(self.guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:", self.guessed_letters)
            print("Du har gissat fel", self.incorrect_guesses_count, "gånger.")
        print("Du har", self.max_incorrect_guesses - self.incorrect_guesses_count, "gissningar kvar.")

    def process_guess(self, letter):
        """Process a letter guess and update game state"""
        # Convert to lowercase and add to guessed letters
        letter = letter.lower()
        self.guessed_letters.add(letter)
        self.current_guess = letter

        # Check if the guess is correct
        if letter in self.secret_word:
            self._handle_correct_guess()
        else:
            self._handle_incorrect_guess()

    def _handle_correct_guess(self):
        """Handle logic for a correct guess"""
        print("\n", self.current_guess.upper(), " finns i det hemliga ordet.\n", sep="")
        self._check_if_won()

    def _handle_incorrect_guess(self):
        """Handle logic for an incorrect guess"""
        print("\n", self.current_guess.upper(), " finns inte i det hemliga ordet.\n", sep="")
        self.incorrect_guesses_count += 1
        self._check_if_lost()

    def _check_if_won(self):
        """Check if the player has won"""
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
                
        print("Du vann!")
        self._reveal_secret_word()
        self.game_over = True
        return True

    def _check_if_lost(self):
        """Check if the player has lost"""
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            print("Game over!")
            self._reveal_secret_word()
            self.game_over = True
            return True
        return False

    def _reveal_secret_word(self):
        """Show the secret word to the player"""
        print("Det hemliga ordet var", self.secret_word)

    def is_game_over(self):
        """Return whether the game is over"""
        return self.game_over


def play_game():
    """Main game loop function"""
    game = HangmanGame()
    game.display_game_status()
    
    while not game.is_game_over():
        # Get user input
        guess = input("Gissa en bokstav: ")
        
        # Process the guess and display updated status
        game.process_guess(guess)
        game.display_game_status()
    
    # Give the user a chance to see the final state
    input("Tryck enter för att avsluta.")


if __name__ == "__main__":
    play_game()
