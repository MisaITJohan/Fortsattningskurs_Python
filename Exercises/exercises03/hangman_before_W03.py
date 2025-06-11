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
        self.game_finished = False


    def setup(self):
        self.game_finished = False
        self.incorrect_guesses_made = 0
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
            self.guessed_letters.clear()

    def get_word_to_guess(self):
        self.word_to_guess = random.choice(self.possible_words).lower()

    def display_current_state(self):
        print("Det hemliga ordet är", len(self.word_to_guess), "tecken långt.")
        if len(self.guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:",
                  *sorted(list(self.guessed_letters)))
            print("Du har gissat fel", self.incorrect_guesses_made, "gånger.")
        print("Du har", self.allowed_guesses - self.incorrect_guesses_made, "gissningar kvar.")

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
        self.game_finished = True


    def check_game_over(self):
        if self.incorrect_guesses_made >= self.allowed_guesses:
            print("Game over!")
            self.display_secret()
            self.game_finished = True


    def display_secret(self):
        print("Det hemliga ordet var", self.word_to_guess)

    # def game_loop(self):
    #     while True:
    #         self.display_current_state()
    #         self.make_guess()
    #         if self.incorrect_guesses_made >= self.allowed_guesses:
    #             break


def main():
    game = HangmanGame()
    done = False
    while done != "":
        game.setup()
        while game.game_finished is not True:
            game.display_current_state()
            game.make_guess()

        done = input("Vill du köra igen? Lämna blankt om du vill avsluta.\n>>>")



if __name__ == '__main__':
    main()
