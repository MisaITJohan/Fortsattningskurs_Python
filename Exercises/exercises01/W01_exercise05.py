# Den här uppgiften går ut på att du ska skapa en klass som beskriver en användare.
# Läs varje punkt noggrant.

# Du ska skapa en klass som heter "User".
# Klassen ska följa dessa regler:

# 1. Varje användare ska ha tre variabler:
#    - Ett användarnamn (username), som är text (en sträng).
#    - En e-postadress (email), som också är text (en sträng).
#    - En ålder (age), som är ett heltal (en integer).

# 2. Klassen ska ha en klassvariabel som heter "programing_language".
#    - Den ska ha värdet "Python".
#    - Det betyder att alla användare ska lära sig samma språk.
#    - OBS: Den ska vara en klassvariabel, inte en instansvariabel.

# 3. Klassen ska ha en metod som heter "info".
#    - Den ska returnera en text som ser ut så här:
#       "alice (22) - alice@example.com"
#    - Texten ska innehålla användarnamn, ålder och e-postadress.

# 4. Klassen ska ha en metod som heter "is_adult".
#    - Den ska returnera True om användaren är 18 år eller äldre.
#    - Den ska annars returnera False.

# Du ska skriva din klass här nedanför.





# ÄNDRA INTE KODEN NEDANFÖR. DEN TESTAR OM DIN KLASS FUNGERAR.
try:
    test_user = User("alice", "alice@example.com", 22)

    # Kontroll av attribut
    assert hasattr(test_user, "username"), "Instansen har inget attribut som heter username."
    assert getattr(test_user, "username") == "alice", "Instansens username blir felaktigt"
    assert hasattr(test_user, "email"), "Instansen har inget attribut som heter email."
    assert getattr(test_user, "email") == "alice@example.com", "Instansens email blir felaktig"
    assert hasattr(test_user, "age"), "Instansen har inget attribut som heter age."
    assert getattr(test_user, "age") == 22, "Instansens age blir felaktig"

    # Kontroll av klassvariabel
    assert hasattr(User, "programing_language"), (
        "Klassen har ingen klassvariabel som heter programing_language.")
    assert User.programing_language == "Python", (
        "Klassvariabeln programing_language har fel värde. Den ska vara 'Python'.")
    assert test_user.programing_language == "Python", (
        "Klassvariabeln programing_language har fel värde eller är en instansvariabel.")


    # Kontroll att programing_language är en klassvariabel (inte instansvariabel)
    # (På två olika sätt om någon läser detta.)
    User.programing_language = "NewLanguage"
    assert test_user.programing_language == "NewLanguage", (
        "programing_language ska vara en klassvariabel, inte en instansvariabel")
    assert "programing_language" not in vars(test_user), (
        "programing_language ska vara en klassvariabel, inte en instansvariabel")

    # Kontroll av metoder
    correct_info_value = "alice (22) - alice@example.com"

    assert isinstance(test_user.info(), str), "info() måste returnera en textsträng"
    assert test_user.info() == correct_info_value, (
        f"info() returnerar fel värde. Kontrollera att formateringen är korrekt."
        f"\nJämför dessa: \nFel:\t{test_user.info()}\nKorrekt:{correct_info_value}")

    assert test_user.is_adult() is True, "is_adult() returnerar inkorrekt värde"

    print("Alla tester är godkända! Bra jobbat.")
except AssertionError as e:
    print("Ett test misslyckades:", e)
except Exception as e:
    print("Ett fel uppstod:", e)
