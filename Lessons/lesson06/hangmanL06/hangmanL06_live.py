# Denna vecka uppdaterar vi load_words_from_file() till att använda pathlib
# samt skapar en placeholder för en mer visuell upplevelse när man spelar.
import pathlib
import random

# Vi samlar våra konstanter här för att göra det lättare att konfigurera.
DEFAULT_MAX_INCORRECT_GUESSES = 5


class HangmanGame:

    def __init__(self, wordlist_path=None, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        self.possible_words = None
        self.load_words_from_file(wordlist_path)
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
    
    def load_words_from_file(self, target_path=None):
        if target_path is None or not pathlib.Path(target_path).exists():
            target_path = pathlib.Path("wordlist_creator/wordlist.txt")
        
        with open(target_path, "r", encoding="utf-8") as file:
            # .strip() kan istället köras när ett ord väljs ut så sparar man
            # in mängder av anrop.
            self.possible_words = [x.strip() for x in file.readlines()]

    def get_word_to_guess(self):
        self.secret_word = random.choice(self.possible_words).lower()

    def display_current_state(self):
        print(f"Det hemliga ordet är {len(self.secret_word)} tecken långt.")

        if len(self.guessed_letters) > 0:
            self.display_all_guesses()
            self.display_correct_guesses()

            print(f"Du har gissat fel {self.incorrect_guesses_count} gånger.")
        print(f"Du har {self.max_incorrect_guesses - self.incorrect_guesses_count} gissningar kvar.\n")
        self.display_placeholder()

    def display_placeholder(self):
        placeholder = self.secret_word
        for char in placeholder:
            if char not in self.guessed_letters:
                placeholder = placeholder.replace(char, "_")
        print(f"Det hemliga ordet är: {placeholder}")

    def display_all_guesses(self):
        print("Du har gissat dessa bokstäver:",
              *sorted(list(self.guessed_letters)))

    def display_correct_guesses(self):
        correct_guesses = sorted([x for x in self.guessed_letters if x in self.secret_word])
        if correct_guesses:
            print("Av de gissade bokstäverna finns dessa i det hemliga ordet:", *correct_guesses)

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
        if check_correct:
            self.correct_guess()
        else:
            self.incorrect_guess()

    def check_guess(self):
        return self.current_guess in self.secret_word

    def correct_guess(self):
        print(f"\n{self.current_guess.upper()} finns i det hemliga ordet.\n")
        self.check_game_won()

    def incorrect_guess(self):
        print(f"\n{self.current_guess.upper()} finns inte i det hemliga ordet.\n")
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
        print(f"Det hemliga ordet var {self.secret_word}")

    def game_loop(self):
        while not self.game_finished:
            self.display_current_state()
            self.make_guess()
            # if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            #     break


def main():
    game = HangmanGame()
    done = False
    while done != "":
        game.setup()
        game.game_loop()

        done = input("Vill du köra igen? Lämna blankt om du vill avsluta.\n>>>")


if __name__ == "__main__":
    main()
