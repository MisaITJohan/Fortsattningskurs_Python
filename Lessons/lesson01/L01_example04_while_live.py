# Exempel på en simpel while-loop som körs så många gånger som användaren
# säger.

input_value = int(input("Skriv in hur många varv vi ska köra: "))

i = 0
while i < input_value:
    print("Nuvarande varv är nummer", i + 1)
    i += 1