# "Augmented assignment" är när man använder den utökade syntaxen vid
#   tilldelningar när man även utför en operation "samtidigt" som tilldelningen
#   sker.

# Förklaringen är delvis överkurs, men grunden ligger inom ramarna för denna
#   kurs.

# För OFÖRÄNDERLIGA datatyper så är detta enbart en genväg för att få kod som,
#   för många, ser snyggare ut.
# För FÖRÄNDERLIGA datatyper så fungerar det lite annorlunda.

# Om man vill ha den tekniska förklaringen så används t.ex. .__iadd__() istället
#   för .__add__(). i:et står för In-place.

# Det som händer är, vid en vanlig tilldelning så skapas "alltid", det finns
#   kanske något undantag, ett nytt objekt.
# Med en augmented assignment så försöker Python använda ett redan existerande
#   objekt.

# Nedan skapar jag två listor.

# Med den första konkatenerar jag till det redan existerande objektet och
#   behåller därmed samma id. Vad det innebär är att det är EXAKT SAMMA objekt
#   som tidigare och kommer då ändras för alla andra ställen som referenserar
#   det objektet.

# Med den andra så skapas ett nytt objekt som sedan tilldelas samma namn som
#   originalobjektet hade.


# Första listan (Augmented assignment)
list_ = [1, 2]
print(id(list_))

list_ += [3]
print(id(list_))
print(list_)

# Andra listan (Vanlig tilldelning)
list2_ = [1, 2]
print(id(list2_))

list2_ = list2_ + [3]
print(id(list2_))
print(list2_)
