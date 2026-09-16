# Exempel på kedjade kontroller, alltså kontroller på resultatet av kontroller.

def check_even_and_dividable_by_3(my_int: int) -> bool:
    is_even: bool = my_int % 2 == 0
    is_dividable_by_3: bool = my_int % 3 == 0
    return is_even and is_dividable_by_3


my_list: list[int] = [x for x in range(101)]

my_checked_list: list[int] = [x for x in my_list if check_even_and_dividable_by_3(x)]

print(my_checked_list)