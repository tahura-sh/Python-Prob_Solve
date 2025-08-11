nterms = int(input("enter a number: "))

result=(list(map(lambda x :2 ** x,range(nterms+1))))

print(result)

for i in range(nterms+1):
    print("the 2 raised of power",i,"is",result[i])
