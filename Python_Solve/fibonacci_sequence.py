def fibo(n):
    if n <=1:
        return n
    else:
        return (fibo(n-1)+fibo(n-2))

print(fibo(5))

# n = int(input("enter a number: "))
#
#
# if n<=0 :
#     print("enter a positive number:")
# else:
#     print("fibonacci sequence")
#
#     for i in range(n):
        # print(fibo(i))
#



