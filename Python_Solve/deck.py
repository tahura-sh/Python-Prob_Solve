import random,itertools

deck =list(itertools.product(range(1,14),["spade","club","hearts","diamond"]))
# print(deck)

random.shuffle(deck)
print(deck)

# shuffle randomly change koree
# itertools.product pair iteration koreee


