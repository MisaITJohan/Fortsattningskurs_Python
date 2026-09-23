"""
Ämnesexempel: Grundläggande lambda-funktioner i Python
======================================================

Detta skript visar vad en lambda-funktion (anonym funktion) är, hur syntaxen
fungerar och hur den skiljer sig från vanliga funktioner definierade med 'def'.

DISCLAIMER: Denna fil togs fram med hjälp av AI för formatering, formuleringar
    och exempelidéer.


Huvudkoncept:
1. En lambda-funktion är en anonym, kort funktion skriven på en enda rad.
2. Syntax: lambda parameter1, parameter2: uttryck
3. Lambda-funktioner returnerar automatiskt resultatet av uttrycket utan 'return'.
4. En lambda kan bara innehålla ett enda uttryck (inga kodblock eller flera rader).
"""

# OBS: Typannoteringen Callable[[indata], returtyp] nedan är överkurs (avancerad typning)
#   och ingår inte i fortsättningskursens obligatoriska moment. Vill du lära dig mer om Callable
#   och andra avancerade typannoteringar finns en kort beskrivning i referensfilen:
#       Lessons/lesson02/L02_example04_advanced_type_hints.py
from typing import Callable

# =============================================================================
# 1. Vad är en lambda-funktion? Syntax och grundidé
# =============================================================================
print("--- 1. Vad är en lambda-funktion? ---")

# Vanlig funktion med 'def':
def square_def(number: int) -> int:
    return number ** 2

# Motsvarande funktion med 'lambda':
# (Här sparar vi den i en variabel enbart för att demonstrera anropet)
# Gör inte så här i praktiken, använd 'def' istället för 'lambda' när en
#   funktion ska
square_lambda: Callable[[int], int] = lambda number: number ** 2

input_value: int = 5
result_def: int = square_def(input_value)
result_lambda: int = square_lambda(input_value)

print(f"Indata: {input_value}")
print(f"Resultat från vanlig funktion (square_def): {result_def}")
print(f"Resultat från lambda-funktion (square_lambda): {result_lambda}")
print()


# =============================================================================
# 2. Jämförelse mellan 'def' och 'lambda'
# =============================================================================
print("--- 2. Jämförelse mellan def och lambda ---")

# Exempel A: Dubblera ett tal
def double_def(value: int) -> int:
    return value * 2

double_lambda: Callable[[int], int] = lambda value: value * 2

number_to_double: int = 7
print(f"Tal att dubblera: {number_to_double}")
print(f"Vanlig def:   {double_def(number_to_double)}")
print(f"Lambda:       {double_lambda(number_to_double)}")

# Exempel B: Formatera en hälsningsfras
def greet_def(name: str) -> str:
    return f"Hej {name}, välkommen till lektionen!"

greet_lambda: Callable[[str], str] = lambda name: f"Hej {name}, välkommen till lektionen!"

student_name: str = "Alex"
print(f"def-hälsning:    {greet_def(student_name)}")
print(f"lambda-hälsning: {greet_lambda(student_name)}")
print()


# =============================================================================
# 3. Parametrar i lambda-funktioner
# =============================================================================
print("--- 3. Parametrar i lambda-funktioner ---")

# A. Inga parametrar (anropas med tomma parenteser)
get_standard_greeting: Callable[[], str] = lambda: "Hej allihop!"
print(f"Noll parametrar: {get_standard_greeting()}")

# B. En parameter
calculate_cube: Callable[[int], int] = lambda value: value ** 3
cube_input: int = 3
print(f"En parameter (kuben av {cube_input}): {calculate_cube(cube_input)}")

# C. Flera parametrar (separeras med kommatecken)
calculate_rectangle_area: Callable[[int, int], int] = lambda width, height: width * height
rect_width: int = 4
rect_height: int = 8
print(
    f"Flera parametrar (area för {rect_width}x{rect_height}): "
    f"{calculate_rectangle_area(rect_width, rect_height)}"
)

# D. Flera parametrar för att kombinera text
format_full_name: Callable[[str, str], str] = (
    lambda first_name, last_name: f"{first_name} {last_name}"
)
print(f"Kombinera namn: {format_full_name('Sam', 'Svensson')}")
print()


# =============================================================================
# 4. Villkorssatser i lambda (Ternary expressions)
# =============================================================================
print("--- 4. Villkorssatser i lambda ---")

# I en lambda-funktion kan vi inte använda vanliga 'if / else'-block på flera rader.
# Istället använder vi ett inline-villkorsuttryck (ternary operator):
#   värde_om_sant if villkor else värde_om_falskt

check_even_or_odd: Callable[[int], str] = lambda number: "Jämnt" if number % 2 == 0 else "Udda"

test_numbers: list[int] = [2, 7, 10, 15]
for number in test_numbers:
    status: str = check_even_or_odd(number)
    print(f"Talet {number} är: {status}")

# Exempel: Bedöm godkänt/underkänt baserat på poänggräns
check_pass_status: Callable[[int], str] = lambda score: "Godkänd" if score >= 50 else "Underkänd"

test_scores: list[int] = [45, 50, 78]
for score in test_scores:
    print(f"Poäng {score}: {check_pass_status(score)}")
print()


# =============================================================================
# 5. Direkt anrop av anonyma funktioner (utan att spara i en variabel)
# =============================================================================
print("--- 5. Direkt anrop utan variabelnamn ---")

# Eftersom lambda-funktioner är anonyma uttryck kan de anropas direkt genom att
#   omsluta hela lambda-uttrycket med parenteser och skicka argument i nästa parentes:
direct_result: int = (lambda x, y: x + y)(12, 8)
print(f"Resultat av direktanrop (12 + 8): {direct_result}")
print()


# =============================================================================
# 6. När ska man använda vanliga funktioner ('def') istället?
# =============================================================================
print("--- 6. Riktlinjer och PEP 8 ---")
print("Riktlinjer för god kodstil:")
print("1. Använd 'def' om funktionen har ett namn eller används på flera ställen.")
print("2. Använd 'def' om logiken kräver flera steg, loopar eller felhantering.")
print("3. Enligt Python-standarden PEP 8 bör man undvika att tilldela lambdas till")
print("   variabler (t.ex. 'f = lambda x: x'). Använd 'def f(x):' istället.")
print("4. Lambda glänser när funktionen är kort och skickas som argument till")
print("   en annan funktion (se del 2 i 'Lambda_in_depth.py').")
