# using enumerate method
#
# list=[1,5,7,3,5]
#
# for index,value in enumerate(list):
#     print(index,value)


#without enumerate

list=[1,5,7,3,5]

for index in range(len(list)):
    value =list[index]
    print(index,"-",value)