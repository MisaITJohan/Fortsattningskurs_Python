# Exempel på strip() och några av dess varianter.

demonstration_string = "  \n text text\n   "

# Så här ser strängen ut om vi skriver ut den nu.
# Jag lägger in > och < runt strängen för att visa var den börjar och slutar.
print(f">{demonstration_string}<")

stripped_string = demonstration_string.strip()
print(f"Så här ser strängen ut efter strip() >{stripped_string}<")

print()

# Om vi skickar med argument till strip() så kan vi tala om vilka tecken som ska
# tas bort. Nu tar vi även bort bokstaven t, men bara från början och slutet.
print(f"Så här ser strängen ut efter strip(' \\nt')"
      f">{demonstration_string.strip(' \nt')}<")

print()

# rstrip() och lstrip() fungerar precis som strip() utöver att de bara ändrar
# ena sidan.
print(f"Så här ser strängen ut efter rstrip() >{demonstration_string.rstrip()}<")
print(f"Så här ser strängen ut efter lstrip() >{demonstration_string.lstrip()}<")
