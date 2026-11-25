str1 = input("Enter a string: ")

for ch in str1:
    if str1.index(ch) == str1.find(ch):
        print(ch, ":", str1.count(ch))