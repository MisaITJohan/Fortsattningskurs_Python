# Oordnat exempel på unpacking och packing.

number_list = ["1", "2", "3", "4"]

print(*number_list)

a, b, c, d = number_list
print("Separata variabler:", a, b, c, d)

a, b, *c = number_list
print("Separata variabler med stjärnat c:", a, b, c)
print(type(c))


def my_func(*args):
    for arg in args:
        print(arg)


my_func(1,2,3,4,5,6,7)