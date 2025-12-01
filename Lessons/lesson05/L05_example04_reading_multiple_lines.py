# Läsa radvis från en fil på två olika sätt

with open("new_file.txt", "r", encoding="utf-8") as file:
    for row in file:
        print(row.strip())  # Tar bort eventuella mellanslag och radbrytningar

    # Nästa rad är bortkommenterad p.g.a. hur filer läses.
    #print(file.readlines())


with open("new_file.txt", "r", encoding="utf-8") as file:
    print(file.readlines())
