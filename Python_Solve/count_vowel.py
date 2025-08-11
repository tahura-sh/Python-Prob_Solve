word = "Hello World !! How are you"
word =word.casefold()
print(word)
vowels ="aeiou"
dict = {}.fromkeys(vowels,0)
print(dict)

for i in word:
    if i in dict:
        dict[i]+=1

print(dict)









