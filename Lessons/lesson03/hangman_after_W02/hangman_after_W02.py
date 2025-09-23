# Första versionen av vårt spel kommer vara simplistiskt men fortfarande ett
# fungerande program. Under kommande veckor kommer vi lägga till fler funktioner.

import random

POSSIBLE_WORDS = (
    "Apa",
    "Banan",
    "Cacao",
    "Dans",
    "Elefant",
    )


class HangmanGame:

    def __init__(self, possible_words=None, allowed_guesses=5):
        if possible_words is None:
            self.possible_words = POSSIBLE_WORDS
        self.allowed_guesses = allowed_guesses
        self.incorrect_guesses_made = 0
        self.word_to_guess = ""
        self.guessed_letters = set()
        self.current_guess = ""


    def setup(self):
        self.incorrect_guesses_made = 0
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
            self.guessed_letters.clear()
        self.display_current_state()

    def get_word_to_guess(self):
        self.word_to_guess = random.choice(self.possible_words).lower()

    def display_current_state(self):
        print("Det hemliga ordet är", len(self.word_to_guess), "tecken långt.")
        if len(self.guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:",
                  *sorted(list(self.guessed_letters)))
            print("Du har gissat fel", self.incorrect_guesses_made, "gånger.")
        print("Du har", self.allowed_guesses - self.incorrect_guesses_made, "gissningar kvar.")
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
        return self.current_guess in self.word_to_guess

    def correct_guess(self):
        print("\n", self.current_guess.upper(), " finns i det hemliga ordet.\n", sep="")
        self.check_game_won()

    def incorrect_guess(self):
        print("\n", self.current_guess.upper(), " finns inte i det hemliga ordet.\n", sep="")
        self.incorrect_guesses_made += 1
        self.check_game_over()

    def check_game_won(self):
        for letter in self.word_to_guess:
            if letter not in self.guessed_letters:
                return
        print("Du vann!")
        self.display_secret()

    def check_game_over(self):
        if self.incorrect_guesses_made >= self.allowed_guesses:
            print("Game over!")
            self.display_secret()

    def display_secret(self):
        print("Det hemliga ordet var", self.word_to_guess)
        # För att ge oss en chans att se ordet så lägger vi in en input() vars
        # enda syfte är att pausa programmet.
        input("Tryck enter för att avsluta.")
        quit()


if __name__ == "__main__":
    game = HangmanGame()
    game.setup()
