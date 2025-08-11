punc =".,;:?!'-–—()[]{}/\@ %&*_~^|<>=+$"

strg = input("enter your word :")

empty_str = ""

for i in (strg):
    if i not in punc:
        empty_str +=i

print(empty_str)