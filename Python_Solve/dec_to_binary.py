def decBinary(n):
    if n> 1:
        decBinary(n//2)
        print(n%2, end=" ")

(decBinary(15))



