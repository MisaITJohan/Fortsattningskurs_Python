# Då filer skapas automatiskt av open() så kan det vara bra att kontrollera om
# en fil existerar innan man försöker läsa den.

import os
if os.path.exists('new_file.txt'):
    print("Filen existerar.")
    with open("new_file.txt", "r", encoding="utf-8") as file:
        print(file.read())
else:
    print("Filen existerar inte.")
