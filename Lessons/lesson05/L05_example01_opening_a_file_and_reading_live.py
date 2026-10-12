# Vi öppnar en fil för läsning. Notera vad som händer om filen inte existerar
#   och vad som händer om vi försöker läsa från filen igen.

with open("new_file.txt", "r", encoding="utf-8") as file:
    content: str = file.read()
    content2: str = file.read()
    print(f"{content = }")
    print(f"{content2 = }")
