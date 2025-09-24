# Exempel på lite mer av f-strängars funktionalitet.

# Självklart så kan vi ha flera placeholders i samma f-sträng:
name = input("Namn: ")
age = input("Ålder: ")

print(f"Hej {name}! Du är {age} år gammal.")

# Man kan även ha uträkningar, funktionsanrop och annan kod inom måsvingarna.
print(f"1 + 1 blir: {1 + 1}")
print(f"{sum(range(10))}")
print(f"{[x for x in range(10)]}")

person = {"name":"Johan", "age":36}

f_string = f"{person["name"]} är {person["age"]} år gammal."
print(f_string)