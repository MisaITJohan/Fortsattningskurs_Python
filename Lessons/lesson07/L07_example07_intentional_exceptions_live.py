# Vi skapar en klass, baserad på int, som enbart kan adderas med andra av sin
# egen typ.

class MyInt(int):

    def __add__(self, other):
        if not type(self) == type(other):
            raise NotImplementedError("Inte implementerat ännu.")
        return MyInt(int(self) + int(other))


x = MyInt(2)
y = MyInt(3)
print(f"{x = }")
print(f"{y = }")


z = x + y
print(f"{z = }")


q = x + 3
print(f"{q = }")
