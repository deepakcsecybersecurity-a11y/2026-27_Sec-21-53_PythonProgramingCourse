#Explaining the use of "Break" in python
Number = int(input("Enter the Number: "))

for num in range(Number):
    if num == 20:
        print(f"The loop is stoped at the number {num}")
        break
    else:
        print(num)

n = int(input("Enter N : "))

i = 1  # start a counter from 1

while i <= n:
    if i == 5:
        print(f"Breaking while loop at number {i} (N was {n})")
        break

    print(f"while loop number = {i} (up to {n})")

    i = i + 1  # move to the next number