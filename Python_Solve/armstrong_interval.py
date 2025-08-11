upper =int(input("enter a upper number:"))
lower =int(input("enter a lower number:"))

for num in range(lower,upper+1):
     power =len(str(num))
     temp =num
     sum =0
     while temp >0:
         digit = temp % 10
         sum +=digit ** power
         temp //=10

     if sum == num:
         print(num, "this is armstrong")
     # if sum != num:
         # print(num, "this is not armstrong")


