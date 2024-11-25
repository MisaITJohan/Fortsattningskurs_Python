# Exempel på "or" och "and".

x = 42
false_bool = False
true_bool = True

# "and" kontrollerar att bägge sidor är Truthy
if x == 42 and true_bool:
    print("x är 42 och vår bool är sann")

# "or" kontrollerar att ÅTMINSTONE en sida är Truthy
if x == 43 or true_bool:
    print("x är inte 43 men vår bool är sann")

if x == 42 or false_bool:
    print("Vår bool är falsk men x är 42")

# Eftersom ena sidan är Falsy så stämmer inte följande
if x == 42 and false_bool:
    print("Detta kommer inte att skrivas ut")