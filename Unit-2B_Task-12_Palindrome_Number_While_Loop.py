n = int(input("enter the number: "))
o = n
work = n
rev = 0
while work > 0:
    digit = work % 10
    rev = rev * 10 + digit
    work = work // 10
if rev == o:
    print("palindrome")
else:
    print("Not a palindreome")
