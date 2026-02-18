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


class HangmanGame:

    def __init__(self, possible_words=None, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        if possible_words is None:
            self.possible_words = POSSIBLE_WORDS
        else:
            self.possible_words = possible_words
        self.max_incorrect_guesses = max_incorrect_guesses
        self.incorrect_guesses_count = 0
        self.secret_word = ""
        self.guessed_letters = set()
        self.current_guess = ""

    def _setup(self):
        self.incorrect_guesses_count = 0
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
            self.guessed_letters.clear()
        self.display_current_state()

    def get_word_to_guess(self):
        self.secret_word = random.choice(self.possible_words).lower()

    def display_current_state(self):
        print("Det hemliga ordet är", len(self.secret_word), "tecken långt.")
        if len(self.guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:",
                  *sorted(list(self.guessed_letters)))
            print("Du har gissat fel", self.incorrect_guesses_count, "gånger.")
        print("Du har", self.max_incorrect_guesses - self.incorrect_guesses_count,
              "gissningar kvar.")
        self.make_guess()

    def make_guess(self):
        guess = input("Gissa en bokstav: ").lower()
        self.guessed_letters.add(guess)
        self.current_guess = guess
        check_correct = self.check_guess()
        if check_correct is True:
            self.correct_guess()
        else:
            self.incorrect_guess()
        self.display_current_state()

    def check_guess(self):
        return self.current_guess in self.secret_word

    def correct_guess(self):
        print("\n", self.current_guess.upper(), " finns i det hemliga ordet.\n", sep="")
        self.check_game_won()

    def incorrect_guess(self):
        print("\n", self.current_guess.upper(), " finns inte i det hemliga ordet.\n", sep="")
        self.incorrect_guesses_count += 1
        self.check_game_over()

    def check_game_won(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return
        print("Du vann!")
        self.display_secret()

    def check_game_over(self):
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            print("Game over!")
            self.display_secret()

    def display_secret(self):
        print("Det hemliga ordet var", self.secret_word)
        # För att ge oss en chans att se ordet så lägger vi in en input() vars
        # enda syfte är att pausa programmet.
        input("Tryck enter för att avsluta.")
        quit()

    def restart_game(self):
        self._setup()


if __name__ == "__main__":
    game = HangmanGame()
    game.restart_game()
