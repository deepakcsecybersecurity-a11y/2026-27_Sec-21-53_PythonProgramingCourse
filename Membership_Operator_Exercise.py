#Membership_Operator_Exercise
#Using (in) Operator
fruits=["apple","banana","rusberry","mulberry",]
fruit=input("Enter the fruit: ")

if fruit in fruits:
    print("fruit is available")
else:
    print("fruit is not available")

#Using (not in) Operator
cars=["BMW","BYD","AUDI","MERCEDES","KOENiGSEGG"]
car=input("Enter the car: ")

if car not in cars:
    print("car is not available")
else:
    print("car is available")