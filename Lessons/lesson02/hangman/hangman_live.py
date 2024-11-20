# Första versionen av vårt spel kommer vara simplistiskt men fortfarande ett
# fungerande program. Under kommande veckor kommer vi lägga till fler funktioner
# samt dela upp programmet i flera filer.

import random

POSSIBLE_WORDS = (
    "Apa",
    "Banan",
    "Cacao",
    "Dans",
    "Elefant",
    )

class HangmanGame:

    def __init__(self, allowed_guesses=5):
        self.allowed_guesses = allowed_guesses
        self.incorrect_guesses_made = 0
        self.word_to_guess = ""
        self.get_word_to_guess()
        self.guessed_letters = set()
        self.current_guess = ""
        self.display_current_state()

    def setup(self):
        # Här borde vissa delar av __init__() ligga för att korta ned
        # den metoden. Detta kan också användas för att nollställa
        # spelet.
        pass

    def get_word_to_guess(self):
        self.word_to_guess = random.choice(POSSIBLE_WORDS).lower()

    def display_current_state(self):
        print("Det hemliga ordet är", len(self.word_to_guess), "tecken långt.")
        if len(self.guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:", self.guessed_letters)
            print("Du gissat fel", self.incorrect_guesses_made, "gånger.")
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
        if self.current_guess in self.word_to_guess:
            return True
        else:
            return False

    def correct_guess(self):
        print("\n", self.current_guess.upper(), " finns i det hemliga ordet.\n", sep="")
        self.check_game_won()

    def incorrect_guess(self):
        print(self.current_guess.upper(), "finns inte i det hemliga ordet.\n")
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
        input("Tryck enter för att avsluta.")
        quit()

if __name__ == "__main__":
    game = HangmanGame()