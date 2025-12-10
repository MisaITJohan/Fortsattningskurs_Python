# Oordnat exempel på unpacking och packing.

number_list = ["1", "2", "3", "4"]

print(number_list)
for x in number_list:
    print(x, end=" ")

print()

print(*number_list)

a, b, c, d, *e = number_list
print(f"Separata variabler: {a} {b} {c} {d} {e}")

a, b, *c = number_list
print(f"Separata variabler med stjärnat c: {a} {b} {c}")
print(type(c))


def my_func(*args, **kwargs):
    for arg in args:
        print(arg)

    print("End of args.")

    for kwarg in kwargs:
        print(kwargs[kwarg])

    print("End of kwargs.")


my_func(1,2,3,4,5,6,7, eight=8)