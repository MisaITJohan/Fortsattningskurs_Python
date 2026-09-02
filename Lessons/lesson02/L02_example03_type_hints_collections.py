# Exempel på hur man använder typannoteringar med samlingar som listor och mängder.

# 1. Listor och tuples
# Vi talar om att possible_words ska vara en lista.
possible_words: list = ["apa", "banan", "citron"]

# Vi skulle kunna vara extra tydliga och specificera att possible_words ska vara en lista av
#   strängar. Detta görs genom att ange typen i hakparenteser efter samlingens datatyp.
#possible_words: list[str] = ["apa", "banan", "citron"]

# En tuple kan innehålla ett valfritt antal strängar. I tuple[str, ...] anger
#   str-typen för varje värde och ... anger att tuplen kan ha hur många värden
#   som helst, även noll.
possible_word_tuple: tuple[str, ...] = ("apa", "banan", "citron")

# 2. Set ("Mängder")
# Vi talar om att guessed_letters ska vara ett set av strängar.
# Set används ofta för att lagra unika saker, som gissade bokstäver.
guessed_letters: set[str] = {"a", "b"}


# 3. Funktioner med samlingar
# Här anger vi att funktionen tar emot en sträng och en mängd,
#   och att den returnerar en boolean (True/False).
def is_word_guessed(secret_word: str, guesses: set[str]) -> bool:
    """Kontrollerar om alla bokstäver i ordet har gissats."""
    for letter in secret_word:
        if letter not in guesses:
            return False
    return True


# Exempel på användning:

secret: str = "apa"

# Vi anropar funktionen och skickar med vår mängd (guesses)
if is_word_guessed(secret, guessed_letters):
    print("Grattis! Du gissade ordet:", secret)
else:
    print("Fortsätt gissa!")


# 4. Alternativa typer med |
# Ett lodrätt streck betyder "eller". set[str] | None betyder att
# previous_guesses antingen är en mängd av strängar eller saknar ett värde.
# Syntaxen kräver Python 3.10 eller senare.
previous_guesses: set[str] | None = None
