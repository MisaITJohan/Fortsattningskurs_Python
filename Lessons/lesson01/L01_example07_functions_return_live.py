# Ett exempel på hur man skapar och använder funktioner som returnerar värden.

def greet(name=None):
    if name is None:
        name = get_name()
    print("Hej " + name + "!")

def get_name():
    input_name = input("Vad heter du? ")
    return input_name

# Anropar vi greet() med ett argument sätts variabeln "name" (i funktionens
# namnrymd) till värdet som vi skickar in.
print("\ngreet() med ett argument:")
greet("Johan")


# Anropar vi greet() utan argument så anropar den get_name() under sin körning.
print("\ngreet() utan argument:")
greet()

# När vi anropar get_name() direkt syns ingenting då det returnerade värdet
# inte används på något sätt.
print("\nget_name() utan att göra något med returvärdet:")
get_name()

# Vill vi använda oss av det returnerade värdet måste vi göra något med det
# eller lagra det någonstans.
print("\nget_name() där vi direkt skickar returvärdet till print():")
print(get_name())

print("\nget_name() där vi först lagrar returvärdet i en variabel och sen skickar"
      "variabeln till print():")
name = get_name()
print(name)