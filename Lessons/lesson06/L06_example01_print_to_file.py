# Exempel på hur systemfunktioner, såsom att läsa och skriva text, hanteras
# som filliknande objekt.

with open("test/test.txt", "w", encoding="utf-8") as fh:  # fh står för File Handle

    print("HEJ!", file=fh)