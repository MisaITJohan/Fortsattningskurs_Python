# Ett exempel på "comprehensions".

my_list = [1, 2, 3, 4, 5, 6, 7]


# my_second_list = []
# for x in my_list:
#     my_second_list.append(x)


# Nedanstående kod är både snabbare, kortare och tydligare.
my_second_list = [x for x in my_list]
print(my_second_list)

# Det måste inte vara en variabel som man använder för att bygga sin lista.
my_third_list = [x for x in range(10)]
print(my_third_list)

my_fourth_list = [x for x in [1, 2, 3, 4, 5]]
print(my_fourth_list)
