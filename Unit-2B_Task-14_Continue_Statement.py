#for loop
N = int(input("Enter N: "))
for i in N:
    if i == 5:
        continue #the code continues
    print(i)

#while loop
n = int(input("Enter n:"))
i = 1

while i <= n:
    if i == 5:
        i = i + 1
        continue

    print(i)
    i = i + 1