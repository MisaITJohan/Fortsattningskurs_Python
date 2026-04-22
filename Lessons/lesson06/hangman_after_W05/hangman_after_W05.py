import os
import random

# Vi samlar våra konstanter här för att göra det lättare att konfigurera.
DEFAULT_MAX_INCORRECT_GUESSES = 5


# Model-klassen hanterar spelets data och logik.
class HangmanModel:
    """En klass som hanterar spellogiken samt lagrar information om spelstatus."""

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
        if target_path is None or not os.path.exists(target_path):
            target_path = "wordlist.txt"

        with open(target_path, "r", encoding="utf-8") as file:
            self.possible_words = [x.strip() for x in file.readlines()]

    def get_word_to_guess(self):
        self.secret_word = random.choice(self.possible_words)

    def check_guess(self):
        return self.current_guess in self.secret_word

    def check_game_won(self):
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def check_game_over(self):
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            return True
        return False

    def guesses_remaining(self):
        return self.max_incorrect_guesses - self.incorrect_guesses_count

    def get_correct_guesses(self):
        return sorted([x for x in self.guessed_letters
                       if x in self.secret_word])


# View-klassen hanterar allt som visas för spelaren och hämtar input
class HangmanView:
    """En klass som hanterar de synliga delarna av spelet, det som kallas för
    "vyn".
    Vyn ska inte behöva veta någonting om modellen."""

    def display_current_state(self, word_length, guessed_letters,
                               incorrect_guesses_count, guesses_remaining,
                               correct_guesses=None):
        print(f"Det hemliga ordet är {word_length} tecken långt.")
        if len(guessed_letters) > 0:
            self.display_all_guesses(guessed_letters)
            if correct_guesses is not None:
                self.display_correct_guesses(correct_guesses)
            print(f"Du har gissat fel {incorrect_guesses_count} gånger.")
        print(f"Du har {guesses_remaining} gissningar kvar.\n")

    def display_all_guesses(self, guessed_letters):
        print("Du har gissat dessa bokstäver:",
              *sorted(list(guessed_letters)))

    def display_correct_guesses(self, correct_guesses):
        if correct_guesses:
            print("Av de gissade bokstäverna finns dessa i det hemliga ordet:",
                  *correct_guesses)

    def get_guess(self):
        guess = input(
            "Gissa en bokstav eller lämna tomt för att avsluta spelet: ")
        return guess

    def display_correct_guess(self, letter):
        print(f"\n{letter} finns i det hemliga ordet.\n")

    def display_incorrect_guess(self, letter):
        print(f"\n{letter} finns inte i det hemliga ordet.\n")

    def display_game_won(self):
        print("Du vann!")

    def display_game_over(self):
        print("Game over!")

    def display_secret(self, secret_word):
        print(f"Det hemliga ordet var {secret_word}")

    def ask_play_again(self):
        return input("Vill du köra igen? Lämna blankt om du vill avsluta.\n>>>")


# Controller-klassen kopplar ihop Model och View och styr spelets flöde.
class HangmanController:

    def __init__(self):
        self.model = HangmanModel()
        self.view = HangmanView()

    def game_loop(self):
        self.model.setup()
        while not self.model.game_finished:
            self.view.display_current_state(
                len(self.model.secret_word),
                self.model.guessed_letters,
                self.model.incorrect_guesses_count,
                self.model.guesses_remaining(),
                self.model.get_correct_guesses()
            )
            self._make_guess()

    def _make_guess(self):
        guess = ""
        while guess in self.model.guessed_letters or len(guess) != 1:
            guess = self.view.get_guess()
            if not guess:
                self.model.game_finished = True
                return
        self._register_guess(guess)
        self._evaluate_guess()

    def _register_guess(self, guess):
        self.model.guessed_letters.add(guess)
        self.model.current_guess = guess

    def _evaluate_guess(self):
        check_correct = self.model.check_guess()
        if check_correct is True:
            self._correct_guess()
        else:
            self._incorrect_guess()

    def _correct_guess(self):
        self.view.display_correct_guess(self.model.current_guess)
        if self.model.check_game_won():
            self.view.display_game_won()
            self.view.display_secret(self.model.secret_word)
            self.model.game_finished = True

    def _incorrect_guess(self):
        self.view.display_incorrect_guess(self.model.current_guess)
        self.model.incorrect_guesses_count += 1
        if self.model.check_game_over():
            self.view.display_game_over()
            self.view.display_secret(self.model.secret_word)
            self.model.game_finished = True


def main():
    controller = HangmanController()
    while True:
        controller.game_loop()
        if not controller.view.ask_play_again():
            break


if __name__ == "__main__":
    main()
