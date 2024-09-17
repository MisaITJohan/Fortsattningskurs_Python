# Detta är tre ledtrådar för W04_exercise10_extra.py.
# Försök att bara titta på en ledtråd i taget och försök lösa uppgiften innan
# du tittar på nästa.

# TIPS 1: Data-listan består av en lista av listor vilket gör det möjligt
#         att iterera över listan med hjälp av en for-loop:
#
#         for row in data:
#           print(row)
#
#         Koden ovan skriver ut följande rader:
#
#         ['2024-09-16', 100, 42.99]
#         ['2024-09-15', 42, 49.99]
#         ['2024-09-14', 37, 51.99]
#         ['2024-09-13', 200, 24.42]
#         ['2024-09-12', 100, 42.99]
#         ['2024-09-11', 100, 42.99]
#         ['2024-09-10', 135, 41.41]
#         ['2024-09-09', 90, 44.44]
#         ['2024-09-08', 10, 54.99]
#
#         Varje rad består alltså av en lista med tre element.








# TIPS 2: En rad i tabellen kan formateras t.ex. så här:
#
#           |2024-09-16     |    100.00|         42.99|
#
#         Första kolumnen är ett datum som vi skriver ut
#         som en vänsterställd sträng. Formatkoden för en
#         sträng är 's'. Om vi vill specificera att
#         strängen ska skrivas ut med tio teckens bredd
#         blir formatkoden '10s' (man behöver egentligen
#         inte s:et i just detta fall men det kan göra
#         saker lättare att tolka).
#
#
#         Kolumn två och tre är tal som vi skriver ut
#         högerställt med två decimaler på tio teckens bredd.
#         Formatkoden blir: '>10.2f'.













# TIPS 3: Om du vill kan du använda koden nedan:
#
#               for row in data:
#                   print(f"|{row[0]:10s}\t|{row[1]:>10.2f}|{row[2]:>10.2f})")