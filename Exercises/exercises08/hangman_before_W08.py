# Denna vecka ändrar vi ingenting under lektionen.
import pathlib
import random


class HangmanGame:

    def __init__(self, allowed_guesses=5):
        self.possible_words = None
        self.allowed_guesses = allowed_guesses
        self.incorrect_guesses_made = 0
        self.word_to_guess = ""
        self.guessed_letters = set()
        self.current_guess = ""
        self.game_finished = False
        self.custom_list_path = ""


    def setup(self):
        self.game_finished = False
        self.incorrect_guesses_made = 0
        custom_list = input(f"Vill du ladda in en {"ny " if self.custom_list_path else ""}"
                            f"ordlista? ja/NEJ (Lämna blankt för "
                            f"nej.) ").casefold()
        if custom_list == "ja".casefold():
            self.load_words_from_file(input("Skriv in namnet på den fil som du vill ladda in: "))
        else:
            self.load_words_from_file()
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
            self.guessed_letters.clear()

    def load_words_from_file(self, file_path=None):
        if file_path is None and not self.custom_list_path:
            file_path = "wordlist.txt"
        elif self.custom_list_path:
            file_path = self.custom_list_path
        elif file_path:
            self.custom_list_path = file_path

        file_to_check = pathlib.Path(file_path)

        if not file_to_check.exists():
            print(f"Det finns ingen fil som heter det som skrevs in, "
                  f"{"standardlistan" if not self.custom_list_path else
                  self.custom_list_path} används.")
            if not self.custom_list_path:
                file_to_open = pathlib.Path("wordlist.txt")
            else:
                file_to_open = pathlib.Path(self.custom_list_path)
        else:
            file_to_open = file_to_check

        self.possible_words = file_to_open.read_text(encoding="utf-8").splitlines()

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

        while self.check_invalid(guess):
            guess = input("Gissa en bokstav eller lämna tomt för att avsluta omgången: ").lower()
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

    def check_invalid(self, guess):
        previously_guessed = guess in self.guessed_letters
        invalid_length = len(guess) != 1
        is_not_letter = not guess.isalpha()

        is_invalid = previously_guessed or invalid_length or is_not_letter

        return is_invalid

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
