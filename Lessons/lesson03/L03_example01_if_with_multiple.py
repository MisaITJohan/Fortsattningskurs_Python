# Exempel på hur man kan ha flera delar i en if-sats.
# Vi tittar med på "and" och "or" i nästa exempel.

x = 42
false_bool = False
true_bool = True

if x == 42 and true_bool:  # I grundkursen hade jag skrivit true_bool == True
    print("x är 42 och vår bool är sann")

if x == 42 and false_bool is False:  # I grundkursen hade jag skrivit false_bool == False
    print("x är 42 och vår bool är falsk")

if x == 42 and false_bool:
    print("Detta kommer inte att skrivas ut")
