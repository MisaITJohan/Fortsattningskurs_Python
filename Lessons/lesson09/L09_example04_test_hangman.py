# L09_example04_test_hangman.py
# 
# Detta är en komplett testsvit för Hangman-spelet i L09_example04_hangman_gui.py.
# Vi använder oss av 'unittest' och 'unittest.mock' för att kunna testa 
# GUI-komponenter utan att faktiskt behöva klicka på knappar.
#
# Här demonstreras:
# 1. Hur man testar en klass med interna tillstånd.
# 2. Hur man använder 'setUp' och 'tearDown' för att förbereda tester.
# 3. Hur man "mockar" (härmar) funktioner som random.choice och fetch_words.
# 4. Hur man kontrollerar att UI-komponenter (som Labels) uppdateras korrekt.

import unittest
from unittest.mock import patch
import tkinter as tk

# Vi importerar klassen vi vill testa. 
# Se till att filnamnet stämmer överens med kopian i lesson09.
from L09_example04_hangman_gui import HangmanGameGUI

class TestHangmanGUI(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Körs en gång innan alla tester i klassen."""
        # Vi skapar en Tk-instans för att kunna skapa widgets.
        # withdraw() gör att fönstret inte dyker upp på skärmen under testerna.
        cls.root = tk.Tk()
        cls.root.withdraw()

    @classmethod
    def tearDownClass(cls):
        """Körs en gång efter att alla tester är klara."""
        cls.root.destroy()

    def setUp(self):
        """Körs före varje enskilt testfall."""
        # Vi vill ha en kontrollerad miljö för varje test.
        # Vi mockar random.choice så att vi alltid vet vilket ord som väljs.
        # Vi mockar även fetch_words så att vi inte är beroende av externa filer eller wordlists.
        with patch('random.choice', return_value="python"):
            with patch.object(HangmanGameGUI, 'fetch_words'):
                self.game = HangmanGameGUI(self.root)
                # Vi sätter manuellt de möjliga orden och startar om spelet (setup)
                # för att säkerställa att vi har vår kontrollerade miljö.
                self.game.possible_words = ["python"]
                self.game.setup()

    def test_initial_state(self):
        """Kontrollerar att spelet startar med rätt initialvärden."""
        self.assertEqual(self.game.word_to_guess, "python")
        self.assertEqual(self.game.incorrect_guesses_made, 0)
        self.assertEqual(len(self.game.guessed_letters), 0)
        self.assertFalse(self.game.game_finished)
        # Kontrollera att displayen visar rätt antal understreck med mellanslag.
        self.assertEqual(self.game.word_display.cget("text"), "_ _ _ _ _ _")

    def test_correct_guess(self):
        """Testar vad som händer vid en korrekt gissning."""
        # Vi simulerar att användaren skriver in 'p' i textfältet.
        self.game.guess_entry.insert(0, "p")
        # Vi anropar metoden som körs när man klickar på "Gissa" eller trycker Enter.
        self.game.make_guess()
        
        self.assertIn("p", self.game.guessed_letters)
        self.assertEqual(self.game.incorrect_guesses_made, 0)
        # Kontrollera att den gissade bokstaven nu visas i ordet.
        self.assertEqual(self.game.word_display.cget("text"), "p _ _ _ _ _")
        self.assertIn("P finns i det hemliga ordet", self.game.message_label.cget("text"))

    def test_incorrect_guess(self):
        """Testar vad som händer vid en felaktig gissning."""
        self.game.guess_entry.insert(0, "x")
        self.game.make_guess()
        
        self.assertIn("x", self.game.guessed_letters)
        self.assertEqual(self.game.incorrect_guesses_made, 1)
        # Inga bokstäver ska ha avslöjats i ord-displayen.
        self.assertEqual(self.game.word_display.cget("text"), "_ _ _ _ _ _")
        self.assertIn("X finns inte i det hemliga ordet", self.game.message_label.cget("text"))

    def test_invalid_guess_already_guessed(self):
        """Testar att man inte kan gissa samma bokstav två gånger."""
        # Första gissningen (korrekt)
        self.game.guess_entry.insert(0, "p")
        self.game.make_guess()
        
        # Andra gissningen (samma bokstav igen)
        self.game.guess_entry.insert(0, "p")
        self.game.make_guess()
        
        self.assertIn("Ogiltig gissning", self.game.message_label.cget("text"))
        # Antalet felaktiga gissningar ska inte ha ökat.
        self.assertEqual(self.game.incorrect_guesses_made, 0)

    def test_invalid_guess_not_alpha(self):
        """Testar att siffror eller andra tecken ger en ogiltig gissning."""
        self.game.guess_entry.insert(0, "1")
        self.game.make_guess()
        self.assertIn("Ogiltig gissning", self.game.message_label.cget("text"))

    def test_win_condition(self):
        """Testar att man vinner när alla bokstäver i ordet är gissade."""
        # Gissa alla unika bokstäver i "python"
        for char in "python":
            self.game.guess_entry.delete(0, tk.END)
            self.game.guess_entry.insert(0, char)
            self.game.make_guess()
            
        self.assertTrue(self.game.game_finished)
        self.assertIn("Du vann", self.game.message_label.cget("text"))

    def test_loss_condition(self):
        """Testar att spelet tar slut när man gissat fel för många gånger."""
        wrong_letters = ["a", "b", "c", "d", "e"] # 5 felaktiga gissningar (standard)
        for char in wrong_letters:
            self.game.guess_entry.delete(0, tk.END)
            self.game.guess_entry.insert(0, char)
            self.game.make_guess()
            
        self.assertTrue(self.game.game_finished)
        self.assertIn("Game over", self.game.message_label.cget("text"))
        # Hela ordet ska avslöjas när man förlorar.
        self.assertEqual(self.game.word_display.cget("text"), "python")

    def test_empty_guess_exits_game(self):
        """Testar att en tom gissning avslutar omgången enligt programmets logik."""
        # guess_entry är tom som standard.
        self.game.make_guess()
        self.assertTrue(self.game.game_finished)
        self.assertIn("Spelet avslutades", self.game.message_label.cget("text"))

if __name__ == '__main__':
    unittest.main()
