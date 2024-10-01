#   Skriv ett program som ber användaren skriva in text (valfri längd) och 
#   som sedan skriver den inmatade texten till en fil (t.ex. fil_1.txt).
#
#   Om ingen text matas in ska filen inte skapas.
#
#   I bägge fallen så ska programmet skriva ut beskrivande text av vad som gjordes. Ett exempel
#   har lämnats nedan.
#
#   Använd gärna f-strängar i din input-prompt och i den beskrivande texten.
#
#
#   W06_exercise_extra01.py handlar om att lägga till extra funktionalitet för detta program.
#
#
#   TIPS 1: Kom ihåg att använda "with open(...)" så att filen stängs automatiskt.
#
#   TIPS 2: För att kontrollera att text skrivits in, kan du använda "if [my_text]:" (där
#   [my_text] står för namnet på variabeln du använde i input()-satsen.

out_file = 'fil_1.txt'


    print(f"Ingen text skrevs in. Filen {out_file} lämnades orörd")


