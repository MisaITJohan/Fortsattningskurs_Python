# INLINES
# TODO: FINISH

def check_even(my_int):
    if my_int % 2 == 0:
        return True
    else:
        return False

def check_even2(my_int):
    return True if my_int % 2 == 0 else False

def check_even3(my_int):
    check = True if my_int % 2 == 0 else False
    return check


my_list = [1, 2, 3, 4, 5, 6, 7]

my_even_list = [x for x in my_list if check_even2(x)]
my_even_list2 = [x for x in my_list if check_even3(x)]

print(my_even_list)
print(my_even_list2)