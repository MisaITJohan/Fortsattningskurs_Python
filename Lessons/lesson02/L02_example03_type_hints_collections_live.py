# Exempel på hur man använder typannoteringar med samlingar som listor och set.

# 1. Listor och tuples
# Vi talar om att possible_words ska vara en lista.
possible_words: list = ["apa", "banan", "citron"]

# Vi skulle kunna vara extra tydliga och specificera att possible_words ska
#   vara en lista av strängar. Detta görs genom att ange typen i hakparenteser
#   efter samlingens datatyp.
possible_words: list[str | float] = ["apa", "banan", "citron"]

# tuple[str,...] anger str-typen för varje element och ... anger att tupeln kan
#   ha hur många värden som helst, även noll.
possible_word_tuple : tuple[str, ...] = ("apa", "banan", "citron")


# 2. Funktioner med samlingar
# Här anger vi att funktionen tar emot en sträng och ett set som måste
#   innehålla strängar och att den returnerar en boolean.
def is_word_guessed(secret_word: str, guesses: set[str]) -> bool:
    for letter in secret_word:
        if letter not in guesses:
            return False
    return True
