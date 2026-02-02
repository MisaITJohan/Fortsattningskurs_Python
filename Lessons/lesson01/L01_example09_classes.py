# Ett exempel på hur man skapar klasser och instansierar objekt.

class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.length = height

    def get_data(self):
        return self.name, self.age, self.length


my_obj = Person("Anna", 23, 172)
print(my_obj)
print()

print(my_obj.name)
print(my_obj.age)
print(my_obj.length)
print()

print(my_obj.get_data())
