# Ett exempel på hur man kan ha kontroller i en comprehension.

def check_even(my_int):
    if my_int % 2 == 0:
        return True
    else:
        return False


my_list = [1, 2, 3, 4, 5, 6, 7]

my_list_without_3 = [x for x in my_list if x != 3]
print(my_list_without_3)

my_even_list = [x for x in my_list if check_even(x)]
print(my_even_list)
