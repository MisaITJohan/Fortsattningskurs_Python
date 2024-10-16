# Skriv om nedanstående kod så att den
# inte kontrollerar i förväg om den
# angivna filen existerar utan i stället
# fångar felet (Exception) som uppstår om
# filen inte existerar.
#
# TIPS:
#   Tänk på vilken typ av Exception du behöver fånga.

import pathlib

test_file = "testfile.txt"
path = pathlib.Path(test_file)
if path.is_file():
    print(f"Filen {test_file} existerar och innehåller nedanstående text")
    print("\t" + path.read_text())

else:
    print(f"Skapar filen {test_file}")
    path.write_text("Det här är innehållet i filen test_file.txt")