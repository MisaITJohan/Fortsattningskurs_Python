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
    pass

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
        pass

    def make_guess(self):
        pass

    def check_guess(self):
        pass

    def correct_guess(self):
        pass

    def incorrect_guess(self):
        pass

    def check_game_won(self):
        pass

    def check_game_over(self):
        pass

    def display_secret(self):
        pass