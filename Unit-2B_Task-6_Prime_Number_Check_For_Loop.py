n = int(input("Enter a number between 1 and 100: "))
count = 0
for x in range(1, n + 1):
    if n % x == 0:
        count += 1
if count == 2:
    print(n, "is a Prime Number")
else:
    print(n, "is Not a Prime Number")