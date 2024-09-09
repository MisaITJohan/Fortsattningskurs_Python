# Exempel på hur man kan ha kontroller på många olika sätt.

def check_even(my_int):
    if my_int % 2 == 0:
        return True
    else:
        return False


def check_even2(my_int):
    check = True if my_int % 2 == 0 else False
    return check


def check_even3(my_int):
    return True if my_int % 2 == 0 else False


def check_even4(my_int):
    return "Sant" if my_int % 2 == 0 else "Falskt"


my_list = [1, 2, 3, 4, 5, 6, 7]

my_even_list = [x for x in my_list if check_even(x)]
my_even_list2 = [x for x in my_list if check_even2(x)]
my_even_list3 = [x for x in my_list if check_even3(x)]
my_even_list4 = [check_even4(x) for x in my_list]

print(my_even_list)
print(my_even_list2)
print(my_even_list3)
print(my_even_list4)
