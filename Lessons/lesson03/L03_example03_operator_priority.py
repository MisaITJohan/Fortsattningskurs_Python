# Exempel på hur prioritering kan påverkas och att saker kan bli otydliga
# om man har flera delar i en jämförelse.

x = 42
false_bool = False
true_bool = True


# Följande är väldigt otydligt då man måste hålla koll på vilken prioritet
# saker har i jämförelsen.
if x == 43 and true_bool or false_bool is False:
    print("x är inte 43 men våra bools är korrekta")

# Följande är hur Python tolkar ovanstående if-sats. Notera hur parenteserna
# är runt början av satsen.
if (x == 43 and true_bool) or (false_bool is False):
    print("x är inte 43 men vår bool är falsk")

# Följande är hur man måste skriva om man vill att Python ska prioritera en
# or-kontroll.
if x == 43 and (true_bool or false_bool is False):
    print("Detta skrivs inte ut. Våra bools är korrekta men x är inte 43")
