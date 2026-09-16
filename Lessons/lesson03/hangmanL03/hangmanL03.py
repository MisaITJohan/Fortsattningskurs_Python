# Denna vecka uppdaterar vi vårt program att ha ett bättre programflöde.
# Vi lägger till möjligheten att spela spelet flera gånger utan att behöva
# starta om hela programmet.

import random

# Vi samlar våra konstanter här för att göra det lättare att konfigurera.
DEFAULT_MAX_INCORRECT_GUESSES: int = 5

POSSIBLE_WORDS: tuple[str, ...] = (
    "apa",
    "banan",
    "cacao",
    "dans",
    "elefant",
    )


# Model-klassen hanterar spelets data och logik.
class HangmanModel:
    """En klass som hanterar spellogiken samt lagrar information om spelstatus."""

    def __init__(self, possible_words=None, max_incorrect_guesses=DEFAULT_MAX_INCORRECT_GUESSES):
        if possible_words is None:
            self.possible_words = POSSIBLE_WORDS
        else:
            self.possible_words = possible_words
        self.max_incorrect_guesses: int = max_incorrect_guesses
        self.incorrect_guesses_count: int = 0
        self.secret_word: str = ""
        self.guessed_letters: set[str] = set()
        self.current_guess: str = ""
        self.game_finished: bool = False

    def setup(self) -> None:
        self.game_finished: bool = False
        self.incorrect_guesses_count: int = 0
        self.get_word_to_guess()
        if len(self.guessed_letters) > 0:
        #if self.guessed_letters:
            self.guessed_letters.clear()

    def get_word_to_guess(self) -> None:
        self.secret_word = random.choice(self.possible_words)

    def check_guess(self) -> bool:
        return self.current_guess in self.secret_word

    def check_game_won(self) -> bool:
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def check_game_over(self) -> bool:
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            return True
        return False

    def guesses_remaining(self) -> int:
        return self.max_incorrect_guesses - self.incorrect_guesses_count


# View-klassen hanterar allt som visas för spelaren och hämtar input
class HangmanView:
    """En klass som hanterar de synliga delarna av spelet, det som kallas för
    "vyn".
    Vyn ska inte behöva veta någonting om modellen."""

    def display_current_state(self,
                              word_length: int,
                              guessed_letters: set[str],
                              incorrect_guesses_count: int,
                              guesses_remaining: int,
    ):
        print("Det hemliga ordet är", word_length, "tecken långt.")
        if len(guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:",
                  *sorted(guessed_letters))
            print("Du har gissat fel", incorrect_guesses_count, "gånger.")
        print("Du har", guesses_remaining, "gissningar kvar.")

    def get_guess(self) -> str:
        guess: str = input(
            "Gissa en bokstav eller lämna tomt för att avsluta spelet: ")
        return guess

    def display_correct_guess(self, letter: str) -> None:
        print("\n", letter, " finns i det hemliga ordet.\n", sep="")

    def display_incorrect_guess(self, letter: str) -> None:
        print("\n", letter, " finns inte i det hemliga ordet.\n", sep="")

    def display_game_won(self) -> None:
        print("Du vann!")

    def display_game_over(self) -> None:
        print("Game over!")

    def display_secret(self, secret_word: str) -> None:
        print("Det hemliga ordet var", secret_word)

    def ask_play_again(self) -> str:
        return input("Vill du köra igen? Lämna blankt om du vill avsluta.\n>>>")


# Controller-klassen kopplar ihop Model och View och styr spelets flöde.
class HangmanController:

    def __init__(self) -> None:
        self.model: HangmanModel = HangmanModel()
        self.view: HangmanView = HangmanView()

    def game_loop(self):
        self.model.setup()
        while not self.model.game_finished:
            self.view.display_current_state(
                len(self.model.secret_word),
                self.model.guessed_letters,
                self.model.incorrect_guesses_count,
                self.model.guesses_remaining(),
            )
            self._make_guess()

    def _make_guess(self) -> None:
        guess: str = ""
        while guess in self.model.guessed_letters or len(guess) != 1:
            guess = self.view.get_guess()
            if not guess:
                self.model.game_finished = True
                return
        self._register_guess(guess)
        self._evaluate_guess()

    def _register_guess(self, guess: str) -> None:
        self.model.guessed_letters.add(guess)
        self.model.current_guess = guess

    def _evaluate_guess(self) -> None:
        check_correct: bool = self.model.check_guess()
        if check_correct is True:
            self._correct_guess()
        else:
            self._incorrect_guess()

    def _correct_guess(self) -> None:
        self.view.display_correct_guess(self.model.current_guess)
        if self.model.check_game_won():
            self.view.display_game_won()
            self.view.display_secret(self.model.secret_word)
            self.model.game_finished = True

    def _incorrect_guess(self) -> None:
        self.view.display_incorrect_guess(self.model.current_guess)
        self.model.incorrect_guesses_count += 1
        if self.model.check_game_over():
            self.view.display_game_over()
            self.view.display_secret(self.model.secret_word)
            self.model.game_finished = True


def main():
    controller: HangmanController = HangmanController()
    while True:
        controller.game_loop()
        if not controller.view.ask_play_again():
            break


if __name__ == "__main__":
    main()
