word =input("enter your word:")

new =word.split()

for i in range(len(new)):
    new[i]=new[i].lower()

# print(new)
new.sort()
print(new)

for j in new:
    print(j)

