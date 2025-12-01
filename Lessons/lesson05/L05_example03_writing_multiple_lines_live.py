# Om vi vill skriva flera rader till en fil kan man använda .writelines().
# Notera att, trots namnet, läggs inte radbyten in automatiskt så man får lägga
# till det i slutet av de strängar som ska skrivas in.

rader = ["Rad 1\n", "Rad 2\n", "Rad 3\n"]
# rader = ["Rad 1", "Rad 2", "Rad 3"]
with open("new_file.txt", "w", encoding="utf-8") as file:
    file.writelines(rader)
