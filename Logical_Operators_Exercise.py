#Logical_operators_Exercise.
a=5
result= a > 2 and a < 10 #Logical AND Operator
print("result of" ,a, "> 2 and ", a ,"<10: ", result)

result= a<2 and a>10 #Logical AND Operator
print("result of",a,"<2 and",a,">10:",result)

result=a>1 or a<3 #Logical OR Operator
print("result of",a,">1 or",a,"<3:",result)

result=a>1 or a>3 #Logical OR Operator
print("result of",a,">1 or",a,"<3;",result)

result=a<1 or a<3 #Logical OR Operator
print("result of",a,"<1 or",a,"<3;",result)

result=not( a<2 and a>10)    #Logical NOT Operator
print("result of",a,"<2 not",a,">10:",result)