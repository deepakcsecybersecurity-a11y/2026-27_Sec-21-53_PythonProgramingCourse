 # Program to calculate Compound Interest
#Taking inputs from the user
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time in years: "))
#computing Compound interest using the below formula
CI = P * (1 + R / 100) ** T - P
#printing the output(Compound interest)
print("Compound Interest =", CI)
