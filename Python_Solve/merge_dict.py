dict1 ={'tahura':10,'muaz':24}
dict2 ={'tahura':5,'ibrahim':5}

# using | operator
# print(dict1|dict2)

# using && operator
# print({**dict1, **dict2})

# using copy & update method
dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)
