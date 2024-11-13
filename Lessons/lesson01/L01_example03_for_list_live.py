# Exempel där vi itererar över en lista med en for-loop men vi har även något
# som händer vid vissa specifika värden.

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    item += 1  # Detta betyder item = item + 1
    # Vi kontrollerar om det nya värdet på item är 2.
    if item == 2:
        # Är item 2 så sänker vi item med 2.
        item -= 2  # item = item - 2

    elif item == 4:
        # Är item 4 så skriver vi ut "Fyra"
        print("Fyra")

    elif item == 2:
        # Vi kommer aldrig att nå nästa rad
        item = "Två"

    if item == 4:
        # Eftersom detta är en ny if-sats så kommer nästa rad att köras.
        item = "Fyra igen"

    print(item)
    print("Slut på varvet\n")