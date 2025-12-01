# Vi skriver till samma fil. Vi testar även vad som händer om man försöker
# läsa samtidigt.

data = "Detta är innehållet som ska skrivas till filen."
with open("new_file.txt", "w", encoding="utf-8") as file:
    file.write(data)
    print(file.read())