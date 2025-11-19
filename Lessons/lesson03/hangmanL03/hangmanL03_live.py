# Denna vecka uppdaterar vi vårt program att ha ett bättre programflöde.
# Vi lägger till möjligheten att spela spelet flera gånger utan att behöva
# starta om hela programmet.
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
        self.game_finished = False

    def setup(self):
        self.game_finished = False
        self.incorrect_guesses_count = 0
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
            self.guessed_letters.clear()

    def get_word_to_guess(self):
        self.secret_word = random.choice(self.possible_words).lower()

    def display_current_state(self):
        print("Det hemliga ordet är", len(self.secret_word), "tecken långt.")
        if len(self.guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:",
                  *sorted(list(self.guessed_letters)))
            print("Du har gissat fel", self.incorrect_guesses_count, "gånger.")
        print("Du har", self.max_incorrect_guesses - self.incorrect_guesses_count, "gissningar kvar.")

    def make_guess(self):
        guess = ""
        while guess in self.guessed_letters or len(guess) != 1:
            guess = input("Gissa en bokstav eller lämna tomt för att avsluta spelet: ").lower()
            if not guess:
                self.game_finished = True
                return
        self.guessed_letters.add(guess)
        self.current_guess = guess
        check_correct = self.check_guess()
        if check_correct is True:
            self.correct_guess()
        else:
            self.incorrect_guess()

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
        self.game_finished = True

    def check_game_over(self):
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            print("Game over!")
            self.display_secret()
            self.game_finished = True

    def display_secret(self):
        print("Det hemliga ordet var", self.secret_word)

    def game_loop(self):
        while not self.game_finished:
            self.display_current_state()
            self.make_guess()
            if self.incorrect_guesses_count >= self.max_incorrect_guesses:
                break


def main():
    game = HangmanGame()
    done = False
    while done != "":
        game.setup()
        game.game_loop()

        done = input("Vill du köra igen? Lämna blankt om du vill avsluta.\n>>>")


if __name__ == "__main__":
    main()
