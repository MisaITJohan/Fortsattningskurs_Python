# Exempel på hur man skapar ett simpelt fönster med hjälp av tkinter.

# När man importerar tkinter så är det väldigt vanligt att man gör det med
# namnet tk. Antagligen för tydliggöra att det är Tk-verktygen man använder.
import tkinter as tk

# När man skapar huvudfönstret så använder man, per standard, namnet "root".
root = tk.Tk()


# Med hjälp av metoder på Tk-objektet så kan vi ändra på egenskaper hos vårt
# fönster.
# title() ändrar texten som står i överkant av fönstret.
root.title("Ett simpelt fönster")


# Med hjälp av geometry() så kan vi styra hur stort fönstret ska vara.
# Storleken skickas, förvirrande nog, som en sträng. I dess simplaste form är
# strängen "BREDDxHÖJD".
# Just för att vi ska ha det där x:et i mitten måste vi använda en sträng.
root.geometry("400x300")


# Om vi vill visa lite text så passar en Label väldigt bra.
# När vi skapar en ny Widget, utöver tk.Tk, så måste vi skicka med vilken
# tidigare Widget som den nya ska tillhöra. Det görs som det första
# positionsargumentet.
# Därefter kan man skicka med flera nyckelordsargument för att konfigurera,
# alltså ställa in, önskade värden för den nya Widgeten.
label = tk.Label(root, text="Etikett med text!")

# För att vår etikett ska synas måste vi använda en av de tre layouthanterarna
# för att placera den i vårt fönster. Vi tittar på hur det fungerar i nästa
# exempel.
label.pack(pady=20)

# mainloop() sätter igång tk-instansen och gör att programmet fortsätter att
# svara på input.
root.mainloop()