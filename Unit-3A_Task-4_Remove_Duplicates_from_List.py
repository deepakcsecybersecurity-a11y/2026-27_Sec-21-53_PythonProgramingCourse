a = [10, 20, 30, 20, 40, 10, 50]

b = []

for i in a:
    if i not in b:
        b.append(i)

print("Original list:", a)
print("List after removing duplicates:", b)