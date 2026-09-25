#Operator precedence and associativity
#Example for Operator_Precedence
a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

example_1 = (a + b) * c 
print(f"example 1 = {example_1}")

example_2 = a ** b + c
print(f"example 2 = {example_2}")

#Example for Operator_Associatiity
example_3 = a * b / c
print(f"example 3 = {example_3}")

example_4 = a // b % c
print(f"example 4 = {example_4}")