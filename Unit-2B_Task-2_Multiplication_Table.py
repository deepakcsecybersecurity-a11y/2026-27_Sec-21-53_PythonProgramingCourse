#for loop
#taking input from the user
number = int(input("Enter the number: "))
#using for loop for the program.
for num in range(1, 11):
    product = number * num
    print(f"{number} x {num} = {product}")

#while loop
#taking input from the user
number = int(input("Enter the number: "))

num = 1
#using while loop for the program
while num <= 10:
    product = number * num
    print(f"{number} x {num} = {product}")
    num += 1