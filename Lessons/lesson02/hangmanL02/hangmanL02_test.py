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

    def __init__(self, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        self.max_incorrect_guesses = max_incorrect_guesses
        self.incorrect_guesses_count = 0
        self.secret_word = ""
        self.current_guess = ""
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
            return True
        else:
            self._handle_incorrect_guess()
            return False

    def _check_guess(self):
        if self.current_guess in self.secret_word:
            return True
        else:
            return False

    def _handle_correct_guess(self):
        self._check_game_won()

    def _handle_incorrect_guess(self):
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

    def display_game_status(self, model):
        print("Det hemliga ordet är", len(model.secret_word), "tecken långt.")

        if len(model.guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:", model.guessed_letters)
            print("Du har gissat fel", model.incorrect_guesses_count, "gånger.")
        print("Du har", model.get_remaining_guesses(), "gissningar kvar.")

    def get_guess(self):
        return input("Gissa en bokstav: ").lower()

    def display_correct_guess(self, guessed_letter):
        print("\n", guessed_letter.upper(), " finns i det hemliga ordet.\n", sep="")

    def display_incorrect_guess(self, guessed_letter):
        print("\n", guessed_letter.upper(), " finns inte i det hemliga ordet.\n", sep="")

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
    def __init__(self):
        self.model = HangmanModel()
        self.view = HangmanView()
        self.view.display_game_status(self.model)

    def get_word_to_guess(self):
        self.model.select_random_word()

    def display_current_state(self):
        self.view.display_game_status(self.model)

    def make_guess(self):
        guessed_letter = self.view.get_guess()
        guess_is_correct = self.model.process_guess(guessed_letter)

        if guess_is_correct is True:
            self._correct_guess()
        else:
            self._incorrect_guess()
        self.display_current_state()


    def _correct_guess(self):
        self.view.display_correct_guess(self.model.current_guess)
        self._check_game_won()

    def _incorrect_guess(self):
        self.view.display_incorrect_guess(self.model.current_guess)
        self._check_game_lost()

    def _check_game_won(self):
        if self.model.game_is_won:
            self.view.display_game_won()
            self.display_secret()

    def _check_game_lost(self):
        if self.model.game_is_lost:
            self.view.display_game_over()
            self.display_secret()

    def display_secret(self):
        self.view.display_secret_word(self.model.secret_word)
        quit()

if __name__ == "__main__":
    game = HangmanGame()
    while True:
        game.make_guess()
