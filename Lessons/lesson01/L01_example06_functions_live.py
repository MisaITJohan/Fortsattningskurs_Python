# Ett exempel på hur man skapar och använder funktioner.

def greet(name="namnlös"):
    print("Hej " + name + "!")

def greet_with_input():
    input_name = input("Vad heter du? ")
    greet(input_name)


# Anropar vi greet() med ett argument sätts variabeln name till värdet som vi
# skickar in.
greet("Johan")

print("\n")  # För att skapa utrymme mellan anropen.

# Anropar vi greet() utan argument sätts variabeln name till standardvärdet
# "namnlös".
greet()

print("\n")  # För att skapa utrymme mellan anropen.

# När vi anropar greet_with_input() så anropar den funktionen greet() under
# sin körning.
greet_with_input()