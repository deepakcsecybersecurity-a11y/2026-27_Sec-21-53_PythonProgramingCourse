#Identity Operator Exercise
a=[1,2,3,42,424,53]
b=a # is identity operator

if a is b: #is identity operator
    print("a and b are same objects")
else:
    print("a and b are different objects")

a = [1, 2, 3]
b = [1, 2, 3]

if a is not b:
    print("a and b are different objects")
else:
    print("a and b are the same object")
