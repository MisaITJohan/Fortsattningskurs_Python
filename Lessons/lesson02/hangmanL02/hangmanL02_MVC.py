# Första versionen av vårt spel kommer vara simplistiskt men fortfarande ett
# fungerande program. Under kommande veckor kommer vi lägga till mer
# funktionalitet, göra det mer användarvänligt samt förbättra programmets
# flöde.

import random
import sys

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
    """En klass som hanterar spellogiken samt lagrar information om spelstatus."""

    def __init__(self, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        self.max_incorrect_guesses = max_incorrect_guesses
        self.incorrect_guesses_count = 0
        self.secret_word = ""
        self.current_guess = ""
        self.current_guess_is_correct = False
        self.guessed_letters = set()
        self.game_is_over = False
        self.game_is_won = False
        self.game_is_lost = False
        self.select_random_word()

    def setup(self):
        # Här borde vissa delar av __init__() ligga för att korta ned
        # den metoden. Detta kan också användas för att nollställa
        # spelet.
        pass

    def select_random_word(self):
        self.secret_word = random.choice(POSSIBLE_WORDS).lower()

    def process_guess(self, guessed_letter):
        self.current_guess = guessed_letter
        self.guessed_letters.add(self.current_guess)

        if self._check_guess() is True:
            self._handle_correct_guess()
        else:
            self._handle_incorrect_guess()

    def _check_guess(self):
        if self.current_guess in self.secret_word:
            return True
        else:
            return False

    def _handle_correct_guess(self):
        self.current_guess_is_correct = True
        self._check_game_won()

    def _handle_incorrect_guess(self):
        self.current_guess_is_correct = False
        self.incorrect_guesses_count += 1
        self._check_game_lost()

    def _check_game_won(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return
        self.game_is_won = True
        self.game_is_over = True

    def _check_game_lost(self):
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            self.game_is_lost = True
            self.game_is_over = True

    def get_remaining_guesses(self):
        return self.max_incorrect_guesses - self.incorrect_guesses_count



class HangmanView:
    """En klass som hanterar de synliga delarna av spelet, det som kallas för
    "vyn".
    Vyn ska inte behöva veta någonting om modellen."""

    def display_game_status(self, secret_word_len, guessed_letters, incorrect_guesses_count, remaining_guesses):
        print("Det hemliga ordet är", secret_word_len, "tecken långt.")

        if len(guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:", guessed_letters)
            print("Du har gissat fel", incorrect_guesses_count, "gånger.")
        print("Du har", remaining_guesses, "gissningar kvar.")

    def get_guess(self):
        """Hämtar en gissning från användaren."""
        return input("Gissa en bokstav: ")

    def display_correct_guess(self, guessed_letter):
        print("\n", guessed_letter, " finns i det hemliga ordet.\n", sep="")

    def display_incorrect_guess(self, guessed_letter):
        print("\n", guessed_letter, " finns inte i det hemliga ordet.\n", sep="")

    def display_game_won(self):
        print("Du vann!")

    def display_game_over(self):
        print("Game over!")

    def display_secret_word(self, secret_word):
        print("Det hemliga ordet var", secret_word)
        # För att ge oss en chans att se ordet så lägger vi in en input() vars
        # enda syfte att pausa programmet.
        input("Tryck enter för att avsluta.")


class HangmanGame:
    """En klass som kombinerar modellen och vyn."""
    def __init__(self):
        self.model = HangmanModel()
        self.view = HangmanView()
        self.display_current_state()

    def get_word_to_guess(self):
        self.model.select_random_word()

    def display_current_state(self):
        self.view.display_game_status(
            len(self.model.secret_word),
            self.model.guessed_letters,
            self.model.incorrect_guesses_count,
            self.model.get_remaining_guesses()
        )

    def make_guess(self):
        guessed_letter = self.view.get_guess()
        self.model.process_guess(guessed_letter)

        if self.model.current_guess_is_correct is True:
            self._correct_guess()
        else:
            self._incorrect_guess()
        self.display_current_state()


    def _correct_guess(self):
        self.view.display_correct_guess(self.model.current_guess)
        self._check_game_over()

    def _incorrect_guess(self):
        self.view.display_incorrect_guess(self.model.current_guess)
        self._check_game_over()

    def _check_game_over(self):
        if self.model.game_is_over:
            if self.model.game_is_won:
                self.view.display_game_won()
            else:
                self.view.display_game_over()
            self._display_secret()

    def _display_secret(self):
        self.view.display_secret_word(self.model.secret_word)

        # Att avsluta ett program på det här sättet är inte rekommenderat, men
        # tills vi kollat närmare på "Flödeskontroll i Praktiken" så använder
        # vi funktionen exit() från modulen sys.
        sys.exit()

if __name__ == "__main__":
    game = HangmanGame()
    while True:
        game.make_guess()
