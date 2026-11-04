#Taking value from the user
n = int(input("Enter the value of N "))
#using for loop to print the numbers
for number in range(1, n + 1):
    print(f"{number}", end=" ")

#Using while loop to print the numbers
n = int(input("Enter N: "))
i = 1
while i <= n:
    print(i)
    i = i + 1
