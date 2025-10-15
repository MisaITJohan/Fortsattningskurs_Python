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


# I de fall där man ska ha en exakt kopia ev en lista finns bättre sätt att
# göra det på, men dessa fungerar inte i alla situationer där man kan använda
# comprehensions.

# my_second_list = my_list[:]
# my_second_list = my_list.copy()



# Dictionary comprehensions ser nästan likadana ut.
my_square_dict = {x:x**2 for x in range(1, 11)}
print(my_square_dict)

numbers_to_combine = [[1, 2], [3, 4], [5, 6]]
my_combined_dict1 = {x[0]:x[1] for x in numbers_to_combine}
print(my_combined_dict1)


number_list1 = [1, 2, 3]
number_list2 = [4, 5, 6]

my_combined_dict2 = {x:y for x, y in zip(number_list1, number_list2)}
print(my_combined_dict2)

numbers_to_combine = [[1, 2, 3], [4, 5, 6]]
my_combined_dict = {x:y for x, y in zip(numbers_to_combine[0], numbers_to_combine[1])}