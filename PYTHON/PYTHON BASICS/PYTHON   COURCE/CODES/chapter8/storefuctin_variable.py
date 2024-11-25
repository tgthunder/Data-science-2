def function1(a,b):
    average=(a+b)/2
    return average
c,d=[int(x) for x in input("Enter two numbers:").split(",")]
# print("THe average of given number is ",function1(c,d))
v=function1(c,d)
print("The average of a given number is" ,v)  #like this we can call any function
