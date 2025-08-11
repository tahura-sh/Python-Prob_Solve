# num=int(input("enter a number :"))
#
# for i in range(num+1):
#     if i % 3 == 0:
#         print("the remainder are :",i)
#
#

# using anonymous function & filter

a =[12,27,36,15,79,38,93]
# num=int(input("enter a number:"))
# result =list(filter(lambda x: x % 12 == 0,range(num+1)))


result =list(filter(lambda x: x % 12 == 0,a))
print(result)




