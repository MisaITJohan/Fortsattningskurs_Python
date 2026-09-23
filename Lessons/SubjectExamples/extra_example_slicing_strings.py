# Ett simplistiskt exempel på hur man kan använda slicing på strängar.

indata = [
    "Name: Anna",
    "Name: Bertil",
    "Name: Caesar",
    "Name: David",
    "Name: Emma",
    "Name: Frank",
    "Name: Gerald",
    ]

for person in indata:
    print(person)


print()
clean_data = []
for person in indata:
    clean_data.append(person[6:])

for person in clean_data:
    print(person)


print()
translated_data = []
for person in indata:
    translation = "Namn: " + person[6:]
    translated_data.append(translation)

for person in translated_data:
    print(person)
