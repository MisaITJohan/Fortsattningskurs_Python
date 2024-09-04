# Exempel på "or" och "and"
# TODO: Skriva färdigt

x = 42
false_bool = False
true_bool = True

if x == 42 and true_bool:
    print("x är 42 och vår bool är sann")

if x == 43 or true_bool:
    print("x är 43 men vår bool är sann")

if x == 42 or false_bool:
    print("Vår bool är falsk men x är 42")

if x == 42 and false_bool:
    print("Detta kommer inte att skrivas ut")

print("------"*3)

# Följande är väldigt otydlig då man måste hålla koll på vilken prioritet
# saker har i jämförelsen.
if x == 43 and true_bool or false_bool is False:
    print("x är inte 43 men våra bools är korrekta")

# Följande är hur Python tolkar ovanstående if-sats. Notera hur parenteserna
# är runt början av satsen.
if (x == 43 and true_bool) or false_bool is False:
    print("x är inte 43 men vår bool är falsk")

# Följande är hur man måste skriva om man vill att Python ska prioritera en
# or-kontroll
if x == 43 and (true_bool or false_bool is False):
    print("Våra bools är korrekta men x är inte 43")

