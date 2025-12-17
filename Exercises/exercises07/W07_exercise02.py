# Denna övning består av två delar:
#
#   I första delen vill jag att ni läser igenom nedanstående kod och sen
#   försöker svara på frågorna INNAN ni kör koden
#   eller ändar något.
#
#   Det är fullt tillåtet att kolla dokumentationen, förslagsvis
#   på Pythons hemsida eller via help()-funktionen, om ni
#   inte kan svaren utantill.
#
#   Skriv ditt svar på raden där det står "Ditt svar:"
#
# TIPS:
#   Läs mer om vilka exception-typer det finns på
#       https://docs.python.org/3/library/exceptions.html#concrete-exceptions
#
#
#
#   I den andra delen så är tanken att ni kör koden och fixar de problem som
#   uppstår när den körs.
#   I denna del får ni också reda på om ni svarade rätt i första delen.
#
# NOTERA:
#   Koden kommer avslutas när
#   varje fel inträffar.

# Del 1:
#
#   Fråga 1:
#       Vilket Exception kommer första felet att skapa?
#
#       Ditt svar:
#
#   Fråga 2:
#       Vilket Exception kommer andra felet att skapa?
#
#       Ditt svar:
#
#   Fråga 3:
#       Vilket Exception kommer tredje felet att skapa?
#
#       Ditt svar:
#
#   Fråga 4:
#       Vilket Exception kommer fjärde felet att skapa?
#
#       Ditt svar:


# Del 2:
#
#   Ändra koden nedan så att varje orsakat problem inte får programmet att krascha.
#
#   Att ändra koden så att felen aldrig sker överhuvudtaget är inte rätt.
#   Det är inte heller rätt att fånga in mer än vad man behöver.


print(10 / 0)         # Första felet


print('10' / 0)       # Andra felet


lista = []
print(lista[10])      # Tredje felet


import math
print(math.sqrt(-1))  # Fjärde felet
