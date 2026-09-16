# Ett exempel på "comprehensions".

my_list: list[int] = [1, 2, 3, 4, 5, 6, 7]

# my_second_list = []
# for x in my_list:
#     my_second_list.append(x)
# print(my_second_list)

# Nedanstående kod är både snabbare, kortare och tydligare.
my_second_list: list[int] = [x for x in my_list]
print(my_second_list)

# Det måste inte vara en variabel som man använder för att bygga sin lista
my_third_list: list[int] = [x for x in range(10)]
print(my_third_list)

my_fourth_list: list[int] = [x for x in [1, 2, 3, 4, 5]]


# I de fall där man ska ha en exakt kopia av en lista finns det bättre sätt att
#   göra det på, men dessa fungerar inte i alla situationer där man kan
#   använda comprehensions.

# my_second_list = my_list[:]
# my_second_list = my_list.copy()


# Dictionary comprehensions ser nästan likadana ut.
my_square_dict: dict[int, int] = {x:x**2 for x in range(1, 11)}
print(my_square_dict)

numbers_to_combine: list[list[int]] = [[1, 2], [3, 4], [5, 6]]
my_combined_dict1: dict[int, int] = {x[0]:x[1] for x in numbers_to_combine}
print(my_combined_dict1)


number_list1: list[int] = [1, 2, 3]
number_list2: list[int] = [4, 5, 6]

my_combined_dict2: dict[int, int] = {x:y for x, y in zip(number_list1, number_list2)}
print(my_combined_dict2)