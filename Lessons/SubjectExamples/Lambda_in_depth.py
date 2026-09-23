"""
Ämnesexempel: Fördjupning i lambda-funktioner i Python
======================================================

I detta skript går vi igenom praktiska användningsområden där lambda-funktioner
är vanliga och användbara i verklig Python-kod.

DISCLAIMER: Denna fil togs fram med hjälp av AI för formatering, formuleringar
    och exempelidéer.

Huvudområden:
1. Sortering med 'sorted()' och '.sort()' med 'key=lambda ...'
2. Hitta extremvärden med 'min()' och 'max()' med 'key=lambda ...'
3. Datatransformering och filtrering med 'map()' och 'filter()' vs list comprehension
4. Händelsehantering och callbacks (varför lambdas används i GUI:er som tkinter)
5. Riktlinjer för läsbarhet: när lambda underlättar och när det försvårar
"""

# OBS: Typannoteringen Callable nedan är överkurs (avancerad typning)
#   och ingår inte i fortsättningskursens obligatoriska moment. Vill du lära
#   dig mer om Callable och mer avancerad typannotering av funktioner finns en
#   kort beskrivning i referensfilen:
#       Lessons/lesson02/L02_example04_advanced_type_hints.py
from typing import Callable

# =============================================================================
# 1. Lambda som sorteringsnyckel ('key=' i sorted() och .sort())
# =============================================================================
print("--- 1. Lambda som sorteringsnyckel ---")

# Exempel A: Sortera en lista med tuples (namn, poäng) efter poäng
students_scores: list[tuple[str, int]] = [
    ("Anna", 85),
    ("Björn", 92),
    ("Cecilia", 78),
    ("David", 95)
]

# Vi vill sortera efter poäng (index 1 i tuppeln):
sorted_by_score: list[tuple[str, int]] = sorted(students_scores, key=lambda student: student[1])
print("Ursprunglig lista (tupler):")
print(f"  {students_scores}")
print("Sorterad efter poäng (lägst till högst):")
print(f"  {sorted_by_score}")

# Sortera i fallande ordning med reverse=True:
sorted_by_score_descending: list[tuple[str, int]] = sorted(
    students_scores, key=lambda student: student[1], reverse=True
)
print("Sorterad efter poäng (högst till lägst):")
print(f"  {sorted_by_score_descending}")
print()

# Exempel B: Sortera en lista med dictionaries
products: list[dict[str, str | int]] = [
    {"name": "Bordslampa", "price": 249, "stock": 12},
    {"name": "Skrivbord", "price": 1299, "stock": 3},
    {"name": "Kontorsstol", "price": 899, "stock": 7},
    {"name": "Musmatta", "price": 99, "stock": 25}
]

# Sortera produkterna efter pris:
sorted_by_price: list[dict[str, str | int]] = sorted(
    products, key=lambda product: product["price"])
print("Produkter sorterade efter pris:")
for product in sorted_by_price:
    print(f"  {product['name']:<15} {product['price']:>6} kr (lager: {product['stock']})")

# Sortera produkterna efter lagerantal:
sorted_by_stock: list[dict[str, str | int]] = sorted(
    products, key=lambda product: product["stock"])
print("Produkter sorterade efter lagerantal:")
for product in sorted_by_stock:
    print(f"  {product['name']:<15} {product['stock']:>4} st i lager")
print()

# Exempel C: Sortera strängar baserat på längd
words: list[str] = ["programmering", "kod", "utvecklare", "python", "ai"]
sorted_by_length: list[str] = sorted(words, key=lambda word: len(word))
print(f"Ord sorterade efter längd: {sorted_by_length}")
print()


# =============================================================================
# 2. Hitta extremvärden med min() och max() med 'key='
# =============================================================================
print("--- 2. Hitta extremvärden med min() och max() ---")

# Hitta den dyraste och billigaste produkten:
most_expensive_product: dict[str, str | int] = max(
    products, key=lambda product: product["price"])
cheapest_product: dict[str, str | int] = min(
    products, key=lambda product: product["price"])

print(f"Dyrast produkt:  {most_expensive_product['name']} ({most_expensive_product['price']} kr)")
print(f"Billigast produkt: {cheapest_product['name']} ({cheapest_product['price']} kr)")

# Hitta studenten med högst poäng:
top_student: tuple[str, int] = max(
    students_scores, key=lambda student: student[1])
print(f"Högsta provresultat: {top_student[0]} med {top_student[1]} poäng")
print()


# =============================================================================
# 3. Transformering och filtrering: map() och filter() vs List Comprehension
# =============================================================================
print("--- 3. map() och filter() jämfört med list comprehension ---")

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Ursprungliga tal: {numbers}")

# Filtrera ut endast jämna tal:
# A. Med filter() och lambda:
even_with_filter: list[int] = list(filter(lambda x: x % 2 == 0, numbers))
# B. Med list comprehension (ofta mer läsbart i modern Python):
even_with_comp: list[int] = [x for x in numbers if x % 2 == 0]

print(f"Jämna tal med filter():           {even_with_filter}")
print(f"Jämna tal med list comprehension: {even_with_comp}")

# Multiplicera alla tal med 10:
# A. Med map() och lambda:
multiplied_with_map: list[int] = list(
    map(lambda x: x * 10, numbers))
# B. Med list comprehension:
multiplied_with_comp: list[int] = [x * 10 for x in numbers]

print(f"Gånger 10 med map():             {multiplied_with_map}")
print(f"Gånger 10 med list comprehension:{multiplied_with_comp}")

# Pedagogisk slutsats:
# I Python rekommenderas oftast list comprehensions framför map/filter + lambda
#   eftersom de är tydligare och lättare att läsa för de flesta utvecklare.
print()


# =============================================================================
# 4. Lambda i händelsehantering (Callbacks)
# =============================================================================
print("--- 4. Lambda i händelsehantering och callbacks ---")

# Problem i GUI-ramverk (t.ex. tkinter):
# När vi skapar en knapp förväntar sig 'command' en funktion utan argument.
# Om vi skriver 'command=handle_click("knapp_1")' anropas funktionen DIREKT
#   när knappen skapas, istället för när användaren klickar på den!
#
# Lösning: Skicka en lambda som 'slår in' anropet och väntar på att knappen klickas:
#   command=lambda: handle_click("knapp_1")

def handle_button_click(button_name: str) -> None:
    print(f"  -> Händelse utlöst: Knappen '{button_name}' klickades!")

# Demonstration av hur en callback-anropare fungerar (simulerat GUI-system):
class SimulatedButton:
    def __init__(self, label: str, on_click_callback: Callable[[], None] | None) -> None:
        self.label: str = label
        self.on_click_callback: Callable[[], None] | None = on_click_callback

    def trigger_click(self) -> None:
        print(f"[Användaren klickar på '{self.label}']")
        if self.on_click_callback:
            self.on_click_callback()

# Vi skapar två knappar med anpassade argument via lambda:
save_button: SimulatedButton = SimulatedButton(
    "Spara", lambda: handle_button_click("Spara-knapp")
)
cancel_button: SimulatedButton = SimulatedButton(
    "Avbryt", lambda: handle_button_click("Avbryt-knapp")
)

# Simulera knapptryck:
save_button.trigger_click()
cancel_button.trigger_click()
print()

# Exempel på hur motsvarande kod ser ut i ett faktiskt tkinter-GUI:
print("Exempel på tkinter-kod (koncept):")
print("""
    import tkinter as tk

    def select_item(item_name):
        print(f"Valde: {item_name}")

    root = tk.Tk()
    btn_apple = tk.Button(root, text="Äpple", command=lambda: select_item("Äpple"))
    btn_banana = tk.Button(root, text="Banan", command=lambda: select_item("Banan"))
""")


# =============================================================================
# 5. Sammanfattning: När är lambda bäst och när ska man undvika det?
# =============================================================================
print("--- 5. Sammanfattning och läsbarhet ---")
print("Använd lambda när:")
print("  [+] Du behöver en engångsfunktion som skickas som argument (t.ex. key i sorted/min/max).")
print("  [+] Du behöver skicka med parametrar till en callback i ett GUI.")
print("  [+] Uttrycket är mycket kort och lättläst.")
print()
print("Undvik lambda när:")
print("  [-] Logiken sträcker sig över flera steg eller villkor.")
print(
    "  [-] Du behöver dokumentera eller felsöka funktionen "
    "(lambdas har inget namn vid traceback)."
)
print("  [-] Koden blir svårläst eller svår att förstå för andra utvecklare.")
