# Vi öppnar en fil för läsning. Notera vad som händer om filen inte existerar.

with open("new_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)