# Exempel på replace()

string_with_spaces = "1 2 3 4 5"

# Vi använder samma namn på den nya strängen så det ser ut som om vi har ändrat
# den befintliga.
string_with_spaces = string_with_spaces.replace(" ", "_")
print(f"{string_with_spaces = }")