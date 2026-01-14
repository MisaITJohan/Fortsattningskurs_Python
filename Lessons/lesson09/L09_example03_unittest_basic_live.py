# Exempel på att använda den typ av automatiserade tester som finns i Pythons
# inbyggda bibliotek: modulen 'unittest'.
#
# 'unittest' är ett kraftfullt ramverk som gör det enkelt att skriva,
# organisera och köra stora mängder tester. Det har länge varit standard i Python
# och är inspirerat av liknande verktyg i andra språk.

import unittest


def add(a, b):
    """En enkel funktion som returnerar summan av två tal."""
    return a + b


# För att använda unittest skapar vi en klass som ärver från unittest.TestCase.
# Varje metod som börjar med ordet 'test_' kommer att köras som ett eget test.

class TestAdd(unittest.TestCase):

    def test_add_positive_numbers(self):
        # Vi använder self.assertEqual istället för assert.
        # Det ger oss bättre felmeddelanden om testet misslyckas.
        self.assertEqual(add(2, 3), 5)


    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)


    def test_add_zero(self):
        self.assertEqual(add(5, 0), 5)


# Detta stycke gör att vi kan köra filen direkt för att starta testerna.
if __name__ == '__main__':
    unittest.main()
