# Creating an empty list
numbers = []

n = int(input("Enter the number of elements: "))

# Getting elements from the user
for i in range(n):
    num = int(input("Enter a number: "))
    numbers.append(num)

# Traversing and displaying the list


for i in numbers:
    print(i, end=" ")