# Första versionen av vårt spel kommer vara simplistiskt men fortfarande ett
#   fungerande program. Under kommande veckor kommer vi lägga till mer
#   funktionalitet, göra det mer användarvänligt samt förbättra programmets
#   flöde.
#
# Vi använder MVC-mönstret (Model-View-Controller) för att dela upp koden
#   i tre delar:
# Model:
#   Spelets data och logik (det hemliga ordet, gissningar).
# View:
#   Allt som visas för spelaren (utskrifter och inmatning).
# Controller:
#   Kopplar ihop Model och View, styr spelets flöde.

import random

# Vi samlar våra konstanter här för att göra det lättare att konfigurera.
DEFAULT_MAX_INCORRECT_GUESSES: int = 5

POSSIBLE_WORDS: tuple = (
    "apa",
    "banan",
    "cacao",
    "dans",
    "elefant",
)


# Model-klassen hanterar spelets data och logik.
class HangmanModel:

    def __init__(self,max_incorrect_guesses: int = DEFAULT_MAX_INCORRECT_GUESSES) -> None:
        self.max_incorrect_guesses: int = max_incorrect_guesses
        self.incorrect_guesses_count: int = 0
        self.secret_word: str = ""
        self.guessed_letters: set = set()
        self.current_guess: str = ""
        self.get_word_to_guess()

    def setup(self) -> None:
        # Här borde vissa delar av .__init__() ligga för att korta ned
        #   den metoden. Detta kan också användas för att nollställa
        #   spelet.
        pass

    def get_word_to_guess(self) -> None:
        self.secret_word = random.choice(POSSIBLE_WORDS)

    def check_guess(self) -> bool:
        if self.current_guess in self.secret_word:
            return True
        else:
            return False

    def check_game_won(self) -> bool:
        for letter in self.secret_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def check_game_over(self) -> bool:
        if self.incorrect_guesses_count >= self.max_incorrect_guesses:
            return True
        return False


# View-klassen hanterar allt som visas för spelaren och hanterar input
class HangmanView:
    """En klass som hanterar de synliga delarna av spelet, det som kallas för
    "vyn".
    Vyn ska inte behöva veta något om modellen."""

    def display_current_state(self, model: HangmanModel) -> None:
        print("Det hemliga ordet är", len(model.secret_word), "tecken långt.")
        if len(model.guessed_letters) > 0:
            print("Du har gissat dessa bokstäver:", model.guessed_letters)
            print("Du har gissat fel", model.incorrect_guesses_count, "gånger.")
        print("Du har", model.max_incorrect_guesses - model.incorrect_guesses_count,
              "gissningar kvar.")

    def get_guess(self) -> str:
        guess: str = input("Gissa en bokstav: ")
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
        # För att ge oss en chans att se ordet så lägger vi in en input() vars
        #   enda syfte är att pausa programmet.
        input("Tryck enter för att avsluta.")

print()