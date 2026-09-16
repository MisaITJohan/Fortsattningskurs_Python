# Ett exempel på hur man kan ha kontroller i en comprehension.

def is_even(my_int: int) -> bool:
    if my_int % 2 == 0:
        return True
    else:
        return False
    # return my_int % 2 == 0


my_list = [1, 2, 3, 4, 5, 6, 7]

my_list_without_3 = [x for x in my_list if x != 3]
print(my_list_without_3)


# Kod utan comprehension:
# my_even_list = []
# for x in my_list:
#     if is_even(x):
#         my_even_list.append(x)
# print(my_even_list)

my_even_list = [x for x in my_list if is_even(x)]
print(my_even_list)