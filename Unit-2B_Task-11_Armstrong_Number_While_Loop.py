n = int(input("Enter the number: "))
b = n
total = 0
while n > 0:
    digit = n % 10
    total = total + digit ** 3
    n = n // 10
if total == b:
    print("it is an Armstrong number")
else:
    print("it is not an Armstrong number")
