# Exempel på hur man placerar ut Widgets.

import tkinter as tk

root = tk.Tk()

root.title("Exempel på layouthanterare")
root.geometry("400x300")


label = tk.Label(root, text="Etikett med text!", bg="blue")
label2 = tk.Label(root, text="Ytterligare en etikett med text!", bg="red")
label3 = tk.Label(root, text="En tredje etikett med text!", bg="green")
label4 = tk.Label(root, text="En fjärde etikett med text!", bg="yellow")

# För att vår etikett ska synas måste vi använda en av de tre layouthanterarna
# för att placera den i vårt fönster.
# De tre fungerar på olika sätt, men alla kan ta emot vissa regler för hur
# saker ska sättas ut. Dessa hanteras via argument när man anropar metoden.

# pack() lägger in Widgets enligt givna regler, per standard så hamnar allt
# i en enda lång kolumn. pady och padx ger oss lite utrymme runt Widgeten.
# label.pack(pady=20)

# place() lägger in Widgets enligt x och y värde, eller efter relativt värde.
# Går inte att kombinera med pack().
label2.place(relwidth=0.6,y=50)

# grid() lägger in Widgets enligt ett osynligt rutnät. Per standard tar tomma
# rutor inte upp någon plats, men man kan ställa in sådana regler.
label3.grid(column=1, row=0)
label4.grid(column=2, row=1)


root.mainloop()