
text = input("enter a word: ")

try:
    num =int(input("enter your number :"))
    print(text + num)

except(TypeError,ValueError) as  show_mistake:
    print(show_mistake) 