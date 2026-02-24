# Exempel som demonstrerar de tre sätten man kan formatera strängar.

a_number = 42
some_text = "Hiya!"
a_list = [1, 2, 3]

# Variant 1, f-strängar:
print("f-strängar:")
print(f"Ett nummer: {a_number}\nLite text: {some_text}\nEn lista: {a_list}")

print()

# Variant 2, .format()-metoden:
print(".format()-metoden:")
print("Ett nummer: {}\nLite text: {}\nEn lista: {exempel}".format(
    a_number, some_text, exempel=a_list,
    ))

print()

# Variant 3 (det äldsta sättet), %-mönstret:
print("%-mönstret:")
print("Ett nummer: %d\nLite text: %s\nEn lista: %s" % (a_number, some_text, a_list))

# Använd ALDRIG variant 3.

print()

# Variant 2 kan vara den mest passande i vissa situationer.
# Exempel på när man ska hämta från en dict:
a_dict = {"name":"Johan", "age":36}

# Med f-sträng:
print(f"Hämtat från en dict: {a_dict['name']} är {a_dict['age']} år gammal.")

# Med .format()
print("Hämtat från en dict: {0[name]} är {0[age]} år gammal.".format(a_dict))
# alternativ
print("Hämtat från en dict: {name} är {age} år gammal.".format(**a_dict))
