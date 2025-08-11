# using loop

list = [1,3,5,66,8]

box =[]

for i in list:
    if i % 3 ==0:
        print(i,"- this is of factor of 3")
        box.append(i)
print(box)

# without a loop

box =[i for i in list if i % 3 ==0 ]
print(box)

# sting with list comprehensive

words =["hello","world"]

new_list =[j.upper() for j in words]
print(new_list)


