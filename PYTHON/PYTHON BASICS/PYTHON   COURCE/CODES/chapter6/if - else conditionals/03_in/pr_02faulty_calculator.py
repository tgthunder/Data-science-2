# faulty calculator
# 44*1=55,288+34=355,12/2=7,34-12=87 if user enter this calculate wrong answer 
print("Enter 1st number:")
a=int(input())
print("Enter 2nd number:")
b=int(input())
print("what operation do you want to perform:")
operator=input()
if a==44 and b==1 and operator=="*":
    print("The ans is 55")
elif a==288 and b==34 and operator=="+":
    print("the ans is 355")
elif a==12 and b==2 and operator=="/":
    print("The ans is 7")
elif a==34 and b==12 and operator=="-":
    print("The ans is 87")
elif operator=="+":
    print("The ans is",a+b) 
elif operator=="-":
    print("The ans is",a-b) 
elif operator=="*":
    print("The ans is",a*b)
elif operator=="/":
    print("The ans is",a/b)
else:
    print("operator invalid")                            