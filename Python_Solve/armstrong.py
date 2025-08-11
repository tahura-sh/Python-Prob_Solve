num =int(input("enter a number: "))
power =len(str(num))
temp = num
sum = 0

while temp >0:
    digit = temp% 10
    cube =digit ** power
    sum +=cube
    temp //= 10

if sum ==num:
    print(num,"this is armstrong")
else:
    print(num,"this is not armstrong")