# Då "w" tar bort det gamla innehållet i en fil, kan vi använda "a" för att öppna
# en befintlig fil och lägga till mer data i slutet av den.

with open('new_file.txt', 'a', encoding="utf-8") as file:
    file.write('Mer data som läggs till i slutet av filen.')

# Notera att ovanstående kod inte lägger in något radbyte.
