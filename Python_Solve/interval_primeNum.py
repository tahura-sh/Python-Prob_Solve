lower = int(input("enter a lower num: "))
upper = int(input("enter a upper num: "))

for num in range(lower,upper+1):
    if num >1:
               for i in range(2,num):
                      if num % i == 0:
                            break
               else:
                   print(num,"these are prime num")


