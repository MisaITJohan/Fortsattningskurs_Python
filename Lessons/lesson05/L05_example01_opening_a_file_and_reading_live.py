# Vi öppnar en fil för läsning. Notera vad som händer om filen inte existerar
# och vad som händer om vi försöker läsa från filen igen.

with open("new_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    content2 = file.read()
    print(content)
    print(f"{content2 = }")