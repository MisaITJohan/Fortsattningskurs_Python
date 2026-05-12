# Denna vecka uppdaterar vi .load_words_from_file() till att använda pathlib
# samt skapar en placeholder för en mer visuell upplevelse när man spelar.
from pathlib import Path
import random

# Vi samlar våra konstanter här för att göra det lättare att konfigurera.
DEFAULT_MAX_INCORRECT_GUESSES = 5


# Model-klassen hanterar spelets data och logik.
class HangmanModel:
    """En klass som hanterar spellogiken samt lagrar information om spelstatus."""

    def __init__(self, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        self.possible_words = None
        self.max_incorrect_guesses = max_incorrect_guesses
        self.incorrect_guesses_count = 0
        self.secret_word = ""
        self.guessed_letters = set()
        self.current_guess = ""
        self.game_finished = False
        self.custom_list_path = ""

    def setup(self):
        self.game_finished = False
        self.incorrect_guesses_count = 0
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
            self.guessed_letters.clear()

    def load_words_from_file(self, target_path=None):
        if target_path is None and not self.custom_list_path:
            target_path = Path("wordlist_creator/wordlist.txt")
        elif self.custom_list_path:
            target_path = self.custom_list_path
        elif target_path:
            self.custom_list_path = target_path

        file_to_check = Path(target_path)

        if not file_to_check.exists():
            if not self.custom_list_path:
                file_to_open = Path("wordlist.txt")
            else:
                file_to_open = Path(self.custom_list_path)
            return file_to_open, False
        else:
            file_to_open = file_to_check

        self.possible_words = file_to_open.read_text(encoding="utf-8").splitlines()
        return file_to_open, True

    def get_word_to_guess(self):
        self.secret_word = random.choice(self.possible_words).lower()

    def check_guess(self):
        return self.current_guess in self.secret_word

    def check_invalid(self, guess):
        previously_guessed = guess in self.guessed_letters
        invalid_length = len(guess) != 1
        is_not_letter = not guess.isalpha()

        is_invalid = previously_guessed or invalid_length or is_not_letter

        return is_invalid

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

    def get_placeholder(self):
        placeholder = self.secret_word
        for char in placeholder:
            if char not in self.guessed_letters:
                placeholder = placeholder.replace(char, "_")
        return placeholder


# View-klassen hanterar allt som visas för spelaren och hämtar input
class HangmanView:
    """En klass som hanterar de synliga delarna av spelet, det som kallas för
    "vyn".
    Vyn ska inte behöva veta någonting om modellen."""

    def display_current_state(self, word_length, guessed_letters,
                               incorrect_guesses_count, guesses_remaining,
                               correct_guesses=None, placeholder=None):
        print(f"Det hemliga ordet är {word_length} tecken långt.")
        if len(guessed_letters) > 0:
            self.display_all_guesses(guessed_letters)
            if correct_guesses is not None:
                self.display_correct_guesses(correct_guesses)
            print(f"Du har gissat fel {incorrect_guesses_count} gånger.")
        print(f"Du har {guesses_remaining} gissningar kvar.\n")
        if placeholder is not None:
            self.display_placeholder(placeholder)

    def display_all_guesses(self, guessed_letters):
        print("Du har gissat dessa bokstäver:",
              *sorted(list(guessed_letters)))

    def display_correct_guesses(self, correct_guesses):
        if correct_guesses:
            print("Av de gissade bokstäverna finns dessa i det hemliga ordet:",
                  *correct_guesses)

    def display_placeholder(self, placeholder):
        print(f"Det hemliga ordet är: {placeholder}")

    def ask_load_wordlist(self, has_custom_list):
        return input(f"Vill du ladda in en {"ny " if has_custom_list else ""}"
                     f"ordlista? ja/NEJ (Lämna blankt för "
                     f"nej.) ").casefold()

    def ask_wordlist_path(self):
        return input("Skriv in namnet på den fil som du vill ladda in: ")

    def display_file_not_found(self, fallback_path, custom_list_path):
        print(f"Det finns ingen fil som heter det som skrevs in, "
              f"{"standardlistan" if not custom_list_path else
              custom_list_path} används.")

    def get_guess(self):
        guess = input(
            "Gissa en bokstav eller lämna tomt för att avsluta omgången: ")
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

    def _handle_wordlist_loading(self):
        custom_list = self.view.ask_load_wordlist(
            bool(self.model.custom_list_path))
        if custom_list == "ja".casefold():
            path = self.view.ask_wordlist_path()
            file_to_open, success = self.model.load_words_from_file(path)
        else:
            file_to_open, success = self.model.load_words_from_file()
        if not success:
            self.view.display_file_not_found(
                file_to_open, self.model.custom_list_path)
            self.model.possible_words = file_to_open.read_text(
                encoding="utf-8").splitlines()

    def game_loop(self):
        self._handle_wordlist_loading()
        self.model.setup()
        while not self.model.game_finished:
            self.view.display_current_state(
                len(self.model.secret_word),
                self.model.guessed_letters,
                self.model.incorrect_guesses_count,
                self.model.guesses_remaining(),
                self.model.get_correct_guesses(),
                self.model.get_placeholder(),
            )
            self._make_guess()

    def _make_guess(self):
        guess = ""

        while self.model.check_invalid(guess):
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
        if check_correct:
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
