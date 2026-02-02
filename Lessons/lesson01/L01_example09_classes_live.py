# Ett exempel på hur man skapar klasser och instansierar objekt.

class Person:

    def __init__(self, name, age, height):
        self._name = name
        self._age = age
        self._height = height

    def get_data(self):
        return self._name, self._age, self._height

    def __repr__(self):
        return self._name + " " + str(self._age) + " " + str(self._height)



my_obj = Person("Anna", 23, 172)
print(my_obj)
print()


# DÅLIG IDÉ: Använd inte "skyddade" attribut utanför objektet
print(my_obj._name)
print(my_obj._age)
print(my_obj._height)
print()

print(my_obj.get_data())