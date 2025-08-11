num1 =int(input("enter a 1st num here: "))
num2 =int(input("enter a 2nd num here: "))
num3 =int(input("enter a 3rd num here: "))

if (num1 > num2) and (num1 > num3):
    print(num1,"is the biggest num")

elif (num2 > num1) and (num2 > num3):
    print(num2,"is the biggest num")
else:
    print(num3,"is the biggest num")

