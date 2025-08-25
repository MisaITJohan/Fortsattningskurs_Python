# Ett exempel på hur man använder slicing.

name_list = [
    "Anna Andersson",
    "Bertil Bengtsson",
    "Harold Hasselblad",
    "Gustav Grip",
    "Felicia Fagerholm",
    "Emma Eriksson",
    "Caesar Carlander",
    "David Dahlgren",
    ]

person_list = [
    ("Anna Andersson", 23, 172),
    ("Bertil Bengtsson", 27, 186),
    ("Harold Hasselblad", 52, 184),
    ("Gustav Grip", 47, 176),
    ("Felicia Fagerholm", 28, 190),
    ("Emma Eriksson", 21, 185),
    ("Caesar Carlander", 43, 178),
    ("David Dahlgren", 34, 177),
    ]

# Vi hämtar och skriver ut första två personerna i name_list:
print(name_list[0:2])


# Vi hämtar och skriver ut de två sista personerna i name_list:
print(name_list[-2:])


# Vi hämtar och skriver ut varannan person från name_list:
print(name_list[::2])


# Vi hämtar och skriver ut namnet på den sista personen i person_list:
print(person_list[-1][0])
print(person_list[-1:][0][0])
# Notera den pyttelilla skillnaden som gör att vi behöver en extra [0] på raden
# ovanför.