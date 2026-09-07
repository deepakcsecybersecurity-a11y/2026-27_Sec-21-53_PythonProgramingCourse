 # Program to calculate Compound Interest

P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))

CI = P * (1 + R / 100) ** T - P

print("Compound Interest =", CI)