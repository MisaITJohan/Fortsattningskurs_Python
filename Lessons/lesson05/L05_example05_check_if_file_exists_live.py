# Då filer skapas automatiskt av open() med write-läge så kan det vara bra att
# kontrollera om en fil existerar innan man försöker öppna den. Detsamma gäller
# om vi vill försäkra oss om att vårt program inte kraschar om man försöker
# läsa en fil som inte finns.

import os
if os.path.exists("new_file.txt"):
    print("Filen existerar.")
    with open("new_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
else:
    print("Filen existerar inte.")