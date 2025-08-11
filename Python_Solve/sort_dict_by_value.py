dict ={'tahura':20,'ibrahim':500,'muaz':100}


# sorted by dict items
# x[0]-----means key dara sort
# x[1]-----means value dara sort

dict_sort =sorted(dict.items() ,key=lambda x :x[1])
print(dict_sort)


# sorted only by value
# dict_sort =sorted(dict.values())
# print(dict_sort)
