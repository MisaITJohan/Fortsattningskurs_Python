# Exempel på hur man kan ha flera delar i en if-sats.
# Vi tittar mer på "and" och "or" i nästa exempel.

x: int = 42
false: bool = False
true: bool = True

if x == 42 and true:  # I grundkursen hade jag skrivit true_bool == True
    print("x är 42 och vår bool är sann")

if x == 42 and false is False:  # I grundkursen hade jag skrivit false_bool == False
    print("x är 42 och vår bool är falsk")

if x == 42 and false:
    print("Detta kommer inte att skrivas ut")

if x == 42 and not true:
    print("Detta kommer inte att skrivas ut")