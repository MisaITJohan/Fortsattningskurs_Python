# Exempel på hur man kan avbryta loopar i förväg och hoppa över varv.


end_number = int(input("Skriv in hur många varv vi ska köra: "))
skip_number = int(input("Skriv in vilket nummer som ska hoppas över: "))
break_number = int(input("Skriv in vilket nummer ska avsluta loopen: "))

i = 0
while i < end_number:
    i += 1

    if i == skip_number:
        print("Vi hoppar över", skip_number)
        continue  # Vi avbryter nuvarande varv (nuvarande iterationen) och fortsätter loopen.

    if i == break_number:
        print("Vi avslutar vid", break_number)
        break  # Vi avslutar loopen trots att vi inte har nått end_number.

    print("Nuvarande värdet på i:", i)
