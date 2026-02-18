# Exempel på kedjade kontroller, alltså kontroller på resultatet av kontroller.

def check_even_and_dividable_by_3(my_int):
    check_even = my_int % 2 == 0
    dividable_by_3 = my_int % 3 == 0
    return check_even and dividable_by_3


my_list = [x for x in range(101)]

my_checked_list = [x for x in my_list if check_even_and_dividable_by_3(x)]

print(my_checked_list)
