import keyword
word =["break","tahura","continue","if","muaz","while","ibrahim"]

for i in range(len(word)):
    if keyword.iskeyword(word[i]):
        print(word[i],"is a keyword")
    else:
        print(word[i],"is not a keyword")


print(keyword.kwlist)
# showing all python keyword