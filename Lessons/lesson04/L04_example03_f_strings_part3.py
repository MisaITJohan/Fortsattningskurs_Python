# Exempel på ytterligare lite mer av f-strängars funktionalitet.

name = input("Namn: ")
age = input("Ålder: ")

# Någonting som bl.a. är väldigt praktiskt när man ska felsöka ett program är att
# skriva in ett = (likamedtecken) efter det som ska tolkas av Python men innanför
# måsvingarna. Det ser oftast inte lika snyggt ut men kan användas på flera
# olika sätt.
print(f"Hej {name=}! Du är {age=} år gammal.")

print("----" * 4)

# Det gäller att tänka på exakt hur man skriver när man håller på med f-strängar.
print(f"{1+1=}")
print(f"{1+1 = }")
print(f"{1 + 1= }")
# Notera skillnaden i det som skrivs ut. Mellanslagen som man lägger innanför
# måsvingarna följer med när utskriften sker. Ibland vill man att det ska vara
# mellanrum, ibland inte. Det gäller att tänka på hur man vill att det ska se ut.

print(f"{"----" * 4}")

# Följande skulle kunna vara ett fall där man faktiskt vill använda sig av detta
# med likamedtecken-syntaxen även i "vanligt" bruk och inte bara i felsökning.
x = 42
y = 84
print(f"{x = }\n{y = }\n{x + y = }")

print(f"{"----"} * 4")  # Medvetet fel som en påminnelse om att tänka sig för.


# En sak som är väldigt praktisk i vissa situationer är att använda sig av
# något som ni kunde se ett exempel på under förra workshoppen, hur or-klausuler
# beter sig, i kombination med det vi tittar på nu.
print(f"Hej {name or "du namnlösa främling"}! Du är {age or "okänd mängd"} år gammal.")
