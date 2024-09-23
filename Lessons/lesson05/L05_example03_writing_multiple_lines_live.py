# Om vi vill skriva flera rader till en fil kan man använda writelines().
# Notera att, trots namnet, läggs inte radbyten in automatiskt.
rader = ["Rad 1\n", "Rad 2\n", "Rad 3\n"]
with open("new_file.txt", "w", encoding="utf-8") as file:
    file.writelines(rader)
