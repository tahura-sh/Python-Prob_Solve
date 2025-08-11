# num =int(input("enter a num:"))
# fact = 1
#
# if num < 0:
#     print("the factorial does not exits")
# if num == 0:
#     print("the factorial is ",1)
# if num > 0:
#     for i in range(1,num+1):
#         fact *= i
# print("the factorial is",fact)


# using recursion

def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))

num =int(input("enter a num here: "))
result = fact(num)
print("the factorial result is:",result)

