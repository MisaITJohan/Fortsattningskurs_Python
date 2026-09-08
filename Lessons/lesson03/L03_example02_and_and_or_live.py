# Exempel på "or" och "and".

x: int = 42
false: bool = False
true: bool = True

# "and" kontrollerar att bägge sidor är Truthy
if x == 42 and true:
    print("x är 42 och vår bool är sann")

# "or" kontrollerar att ÅTMINSTONE en sida är Truthy
if x == 43 or true:
    print("x är inte 43 men vår bool är sann")

if x == 42 or false:
    print("Vår bool är inte sann men x är 42")

# Eftersom den ena sidan är Falsy så stämmer inte följande
if x == 42 and false:
    print("Detta kommer inte att skrivas ut")