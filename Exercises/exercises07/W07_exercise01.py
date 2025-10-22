# Komplettera koden nedan så att när användaren
# trycker CTRL-C (och därmed genererar ett KeyboardInterrupt-exception)
# så fångas detta och kör kod som ber användaren bekräfta att den vill
# avsluta programmet.
# Koden ska dock fortfarande fånga alla andra exceptions.
#
# Om användarens svar börjar på "j" (eller "y" om man
# föredrar engelska) ska programmet avslutas.

# Ledtråd: Endast KeyboardInterrupt ska fångas av den bit som du lägger till.

# Ledtråd: Kontrollen av användarens svar kan t.ex. lösas med en metod i str.

while True:
    try:
        x = input("Skriv in ett värde som ska skrivas ut: ")
        print(x)
    except:
        print("Fångade ett fel! Hurra!")
