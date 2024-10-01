# Kopiera över koden som du skrev i W06_exercise01.py till denna fil.
#
#   Lägg till en kontroll om filen redan finns och be i så fall användaren
#   bekräfta (genom att skriva in "ja") att filen får skrivas över (ersättas
#   med nytt innehåll). Om användaren svarar "nej", avsluta programmet.
#
#   TIPS 1:
#       Använd funktionen os.path.exists() för att kontrollera om filen
#       existerar. Eller, ännu hellre, använd .exists() på ett Path-object
#       (Path kommer från modulen pathlib).
#       
#   TIPS 2:
#       Ett alternativ till "quit()" för att avsluta programmet är: 
#           raise SystemExit(1)
#
#       Då kommer programmet avslutas och returnera koden 1, vilket
#       indikerar att körningen avslutades p.g.a. att något "fel" 
#       inträffade (när programmet körts utan att något fel uppstått 
#       returneras normalt sett koden 0: raise SystemExit(0)).
#
#   TIPS 3:
#       Du kan basera din kod för att kontrollera att någon inmatning gjorts på följande
#       kod:
#
#           out_file = "fil_1.txt"
#           # Kolla om filen redan finns och be användaren skriva in 
#           # "ja" eller "nej". Om användaren skriver in något annat än "ja"
#           avslutas programmet.
#           if os.path.exists(out_file):
#               confirm = input(f"Filen {out_file} finns redan. Vill du skriva över (ja/NEJ)? ")
#               if confirm.lower() != "ja":
#                   raise SystemExit(1)  # Avsluta programmet