# Denna vecka uppdaterar vi load_words_from_file() till att använda pathlib
# samt skapar en placeholder för en mer visuell upplevelse när man spelar.
import pathlib
import random


class HangmanGame:

    def __init__(self, wordlist_path=None, allowed_guesses=5):
        self.possible_words = None
        self.load_words_from_file(wordlist_path)
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
    
    def load_words_from_file(self, target_path=None):
        if target_path is None:
            target_path = pathlib.Path("wordlist_creator/wordlist.txt")
        
        with open(target_path, "r", encoding="utf-8") as file:
            self.possible_words = [x.strip() for x in file.readlines()]

    def get_word_to_guess(self):
        self.word_to_guess = random.choice(self.possible_words).lower()

    def display_current_state(self):
        print(f"Det hemliga ordet är {len(self.word_to_guess)} tecken långt.")

        if len(self.guessed_letters) > 0:
            self.display_all_guesses()
            self.display_correct_guesses()

            print(f"Du har gissat fel {self.incorrect_guesses_made} gånger.")
        print(f"Du har {self.allowed_guesses - self.incorrect_guesses_made} gissningar kvar.\n")
        self.display_placeholder()

    def display_placeholder(self):
        placeholder = self.word_to_guess
        for char in placeholder:
            if char not in self.guessed_letters:
                placeholder = placeholder.replace(char, "_ ")
        print(f"Det hemliga ordet är: {placeholder}")

    def display_all_guesses(self):
        print("Du har gissat dessa bokstäver:",
              *sorted(list(self.guessed_letters)))

    def display_correct_guesses(self):
        correct_guesses = sorted([x for x in self.guessed_letters if x in self.word_to_guess])
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
        return self.current_guess in self.word_to_guess

    def correct_guess(self):
        print(f"\n{self.current_guess.upper()} finns i det hemliga ordet.\n")
        self.check_game_won()

    def incorrect_guess(self):
        print(f"\n{self.current_guess.upper()} finns inte i det hemliga ordet.\n")
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
        print(f"Det hemliga ordet var {self.word_to_guess}")

    def game_loop(self):
        while not self.game_finished:
            self.display_current_state()
            self.make_guess()
            if self.incorrect_guesses_made >= self.allowed_guesses:
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
