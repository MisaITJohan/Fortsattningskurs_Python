# Exempel på att använda 'assert'.

# Det reserverade ordet 'assert' används för att automatisera kollen av
# våra antaganden.
# Det är som att säga: "Jag påstår att det här uttrycket är sant".

# Om uttrycket är True händer ingenting och programmet fortsätter.
# Om uttrycket är False kraschar programmet med ett AssertionError.

# Ni kunde se exempel på detta i W01_exercise05.py


def add(a, b):
    """En enkel funktion som returnerar summan av två tal."""
    return a + b

# Istället för att bara printa och titta själva, använder vi nu assert.
print("Kör automatiska tester med assert...")

# Om något av dessa påståenden inte stämmer kommer programmet att krascha.
assert add(2, 3) == 5, "Ska bli 5"
assert add(-1, 1) == 0, "Ska bli 0"
assert add(0, 0) == 0, "Ska bli 0"

# Om vi ser detta meddelande vet vi att alla assert-rader ovanför stämde.
print("Alla tester gick igenom!")

# TIPS: Prova att ändra returvärdet i funktionen 'add' (t.ex. till a - b)
# och kör programmet igen för att se hur ett misslyckat test ser ut.
