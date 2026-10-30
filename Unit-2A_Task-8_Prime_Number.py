#python program to check whether the given number is a prime number or not
prime_number = int(input("Enter the number: "))

if prime_number <= 1:
    print("Not a prime number")
else:
    for i in range(2, prime_number):
        if prime_number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")