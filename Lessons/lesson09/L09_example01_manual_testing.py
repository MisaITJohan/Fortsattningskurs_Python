# Exempel på att manuellt testa en funktion.

# Detta är det mest grundläggande sättet att testa sin kod på. Vi kör koden,
# matar in värden och tittar sedan manuellt i konsolen för att se om 
# resultatet stämmer överens med vad vi förväntade oss. Nästan alla övningar
# från både grund- och fortsättningskursen fungerar på detta sätt.

def add(a, b):
    """En enkel funktion som returnerar summan av två tal."""
    return a + b

# Vi genomför några manuella tester genom att skriva ut resultatet.
# Notera att vi själva måste veta vad det "rätta" svaret är för att kunna
# avgöra om testet lyckades.

print("Testar add(2, 3):", add(2, 3))
print("Förväntat resultat: 5")

print("-" * 20)

print("Testar add(-1, 1):", add(-1, 1))
print("Förväntat resultat: 0")

# Nackdelar med manuell testning:
# 1. Det är tidskrävande (man måste köra och titta själv varje gång).
# 2. Det är lätt att missa fel om man har många utskrifter.
# 3. Det är svårt att skala upp när programmet blir större.
