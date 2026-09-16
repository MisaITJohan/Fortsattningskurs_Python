# Exempel på hur man kan ha kontroller på många olika sätt.

def check_even1(my_int: int) -> bool:
    if my_int % 2 == 0:
        return True
    else:
        return False

def check_even2(my_int: int) -> bool:
    check: bool = True if my_int % 2 == 0 else False
    return check

def check_even3(my_int: int) -> bool:
    return my_int % 2 == 0

def check_even4(my_int: int) -> str:
    return "Sant" if my_int % 2 == 0 else "Falskt"


my_list: list[int] = [1, 2, 3, 4, 5, 6, 7]

my_even_list1: list[int] = [x for x in my_list if check_even1(x)]
my_even_list2: list[int] = [x for x in my_list if check_even2(x)]
my_even_list3: list[int] = [x for x in my_list if check_even3(x)]
my_even_list4: list[str] = [check_even4(x) for x in my_list]

print(my_even_list1)
print(my_even_list2)
print(my_even_list3)
print(my_even_list4)