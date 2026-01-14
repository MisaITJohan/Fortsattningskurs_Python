# Exempel på att använda 'pytest', ett av de mest populära ramverken för 
# testning i Python-världen.

# pytest är känt för att vara enkelt att använda och kräver mindre "boilerplate"
# (extra kod) än unittest. Det använder vanliga 'assert'-uttryck istället för 
# speciella metoder som 'assertEqual'.

import pytest

def add(a, b):
    """En enkel funktion som returnerar summan av två tal."""
    return a + b

# I pytest behöver vi inte ärva från någon klass. 
# Vi skriver bara funktioner vars namn börjar med 'test_'.

def test_add_positive_numbers():
    # Vi använder vanliga assert-uttryck. 
    # Pytest "skriver om" dessa bakom kulisserna för att ge detaljerade 
    # felmeddelanden vid misslyckande.
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(5, 0) == 5

# För att köra dessa tester skriver man vanligtvis 'pytest' i terminalen.
# (Notera: pytest måste vara installerat, t.ex. via 'pip install pytest')
# Detta stycke gör att vi kan köra filen direkt för att starta testerna.
if __name__ == "__main__":
    pytest.main()
