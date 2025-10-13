# Oordnat exempel på unpacking och packing.

name_list = ["1", "2", "3", "4"]

print(*name_list)

a, b, c, d = name_list
print("Separata variabler:", a, b, c, d)

a, b, *c = name_list
print("Separata variabler med stjärnat c:", a, b, c)
print(type(c))


def my_func(*args):
    for arg in args:
        print(arg)


my_func(1,2,3,4,5,6,7)