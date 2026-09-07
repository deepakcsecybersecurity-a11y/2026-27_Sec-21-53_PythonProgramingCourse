# Program to calculate Simple Interest

# Input from the user
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (% per year): "))
t = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (p * r * t) / 100

# Display the result
print("Simple Interest =", simple_interest)